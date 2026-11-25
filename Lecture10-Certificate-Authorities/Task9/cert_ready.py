# Ready helpers for the tasks of Lecture 10. Treat this file as a black box:
# you only need the names listed here. They wrap the `cryptography` library
# (pip install cryptography) and the ssl module of Python.
#
#   load_cert(path)              one certificate from a PEM file
#   load_certs(path)             every certificate of a PEM file (a list)
#   save_cert(cert, path)        write a certificate as PEM
#   load_csr(path), save_csr(csr, path)
#   subject_of(x), issuer_of(cert)   the names as text, e.g. "CN=WE1,O=Google Trust Services,C=US"
#   dns_names_of(x)              the DNS names in the subjectAltName of a certificate or CSR (a list)
#   valid_from(cert), valid_until(cert)   dates and times in UTC
#   ca_flag(cert)                (True or False, path length or None) from Basic Constraints
#   key_type(cert)               "RSA 4096", "EC P-384", ...
#   key_id(public_key)           the first 8 bytes of the SHA-256 of the public key, in hex
#   signed_by(child, parent)     True if parent's key signed child (names and signature)
#   new_key()                    a new private key (elliptic curve P-256)
#   make_cert(...)               build and sign a certificate (see below)
#   make_csr(key, cn, dns_names) build and sign a certificate signing request
#   scts_of(cert)                the Signed Certificate Timestamps inside a certificate (a list)
#   sct_time(sct)                the time of an SCT in UTC
#   tls_check(leaf_key, chain, root, hostname)
#                                a TLS client that trusts only `root` connects to a server that
#                                sends `chain`: returns "OK" or the reason why the client said no

import datetime
import os
import ssl
import tempfile
import warnings

from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

UTC = datetime.timezone.utc


# ---------- files ----------

def load_cert(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificate(f.read())


def load_certs(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificates(f.read())


def save_cert(cert, path):
    with open(path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def load_csr(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_csr(f.read())


def save_csr(csr, path):
    with open(path, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


def save_key(key, path):
    with open(path, "wb") as f:
        f.write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                  serialization.NoEncryption()))


# ---------- reading ----------

def subject_of(x):
    return x.subject.rfc4514_string()


def issuer_of(cert):
    return cert.issuer.rfc4514_string()


def dns_names_of(x):
    try:
        san = x.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
    except x509.ExtensionNotFound:
        return []
    return san.get_values_for_type(x509.DNSName)


def _utc(t):
    if t.tzinfo is None:
        return t.replace(tzinfo=UTC)
    return t


def valid_from(cert):
    if hasattr(cert, "not_valid_before_utc"):      # cryptography 42 and newer
        return cert.not_valid_before_utc
    return _utc(cert.not_valid_before)


def valid_until(cert):
    if hasattr(cert, "not_valid_after_utc"):
        return cert.not_valid_after_utc
    return _utc(cert.not_valid_after)


def ca_flag(cert):
    try:
        bc = cert.extensions.get_extension_for_class(x509.BasicConstraints).value
    except x509.ExtensionNotFound:
        return (False, None)
    return (bc.ca, bc.path_length)


def key_type(cert):
    key = cert.public_key()
    if isinstance(key, rsa.RSAPublicKey):
        return "RSA " + str(key.key_size)
    if isinstance(key, ec.EllipticCurvePublicKey):
        names = {"secp256r1": "P-256", "secp384r1": "P-384", "secp521r1": "P-521"}
        return "EC " + names.get(key.curve.name, key.curve.name)
    return type(key).__name__


def key_id(public_key):
    der = public_key.public_bytes(serialization.Encoding.DER,
                                  serialization.PublicFormat.SubjectPublicKeyInfo)
    h = hashes.Hash(hashes.SHA256())
    h.update(der)
    return h.finalize()[:8].hex()


def signed_by(child, parent):
    # the issuer name of child must be the subject name of parent, and the signature
    # on child must verify with the public key of parent
    try:
        child.verify_directly_issued_by(parent)
        return True
    except (ValueError, TypeError, InvalidSignature):
        return False


def scts_of(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.PrecertificateSignedCertificateTimestamps)
    except x509.ExtensionNotFound:
        return []
    result = []
    for sct in ext.value:
        result.append(sct)
    return result


def sct_time(sct):
    with warnings.catch_warnings():      # old versions of cryptography warn inside .timestamp
        warnings.simplefilter("ignore")
        t = sct.timestamp
    return _utc(t)


# ---------- making keys, requests and certificates ----------

def new_key():
    return ec.generate_private_key(ec.SECP256R1())


def _name(cn):
    return x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cn)])


def make_csr(key, cn, dns_names):
    builder = x509.CertificateSigningRequestBuilder().subject_name(_name(cn))
    if dns_names:
        alt = []
        for d in dns_names:
            alt.append(x509.DNSName(d))
        builder = builder.add_extension(x509.SubjectAlternativeName(alt), critical=False)
    return builder.sign(key, hashes.SHA256())


def make_cert(cn, key, issuer=None, issuer_key=None, ca=False, path_len=None, days=90,
              dns_names=None, permitted=None, start=None, public_key=None):
    """Build and sign a certificate.
    cn          the common name of the subject, e.g. "Trusty Root CA" or "shop.example"
    key         the private key of the subject (its public half goes into the certificate)
    issuer      the certificate of the CA that signs; None makes a self-signed certificate
    issuer_key  the private key of that CA (None for a self-signed certificate)
    ca          True for a CA certificate (Basic Constraints CA:TRUE), False for a leaf
    path_len    how many CA certificates may stand below this CA (None = no limit)
    days        how long the certificate is valid
    dns_names   the names of a leaf (subjectAltName), e.g. ["shop.example"]
    permitted   Name Constraints of a CA: the only DNS names it may issue for, e.g. ["acme.example"]
    start       when the validity starts (default: now)
    public_key  the public key to certify, if key is None (a CA signing a CSR)"""
    if public_key is None:
        public_key = key.public_key()
    if issuer is None:
        issuer_name = _name(cn)
        issuer_public = public_key
        signing_key = key
    else:
        issuer_name = issuer.subject
        issuer_public = issuer.public_key()
        signing_key = issuer_key
    if start is None:
        start = datetime.datetime.now(UTC) - datetime.timedelta(minutes=5)
    b = x509.CertificateBuilder()
    b = b.subject_name(_name(cn)).issuer_name(issuer_name).public_key(public_key)
    b = b.serial_number(x509.random_serial_number())
    b = b.not_valid_before(start).not_valid_after(start + datetime.timedelta(days=days))
    b = b.add_extension(x509.BasicConstraints(ca=ca, path_length=path_len if ca else None), critical=True)
    b = b.add_extension(x509.KeyUsage(digital_signature=True, content_commitment=False,
                                      key_encipherment=False, data_encipherment=False,
                                      key_agreement=False, key_cert_sign=ca, crl_sign=ca,
                                      encipher_only=False, decipher_only=False), critical=True)
    b = b.add_extension(x509.SubjectKeyIdentifier.from_public_key(public_key), critical=False)
    b = b.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(issuer_public), critical=False)
    if not ca:
        b = b.add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False)
    if dns_names:
        alt = []
        for d in dns_names:
            alt.append(x509.DNSName(d))
        b = b.add_extension(x509.SubjectAlternativeName(alt), critical=False)
    if permitted:
        subtrees = []
        for d in permitted:
            subtrees.append(x509.DNSName(d))
        b = b.add_extension(x509.NameConstraints(permitted_subtrees=subtrees, excluded_subtrees=None),
                            critical=True)
    return b.sign(signing_key, hashes.SHA256())


# ---------- a TLS client and a TLS server, in memory (no network) ----------

def _pem(cert):
    return cert.public_bytes(serialization.Encoding.PEM).decode()


def tls_check(leaf_key, chain, root, hostname):
    """A TLS server sends `chain` (the leaf first, then the intermediates) and proves it holds
    `leaf_key`. A TLS client that trusts only `root` checks the chain and the name `hostname`,
    as a browser would. Returns "OK" or the reason given by OpenSSL."""
    server_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    with tempfile.TemporaryDirectory() as folder:
        cert_file = os.path.join(folder, "chain.pem")
        key_file = os.path.join(folder, "key.pem")
        with open(cert_file, "w") as f:
            for c in chain:
                f.write(_pem(c))
        save_key(leaf_key, key_file)
        server_ctx.load_cert_chain(cert_file, key_file)
    client_ctx = ssl.create_default_context(cadata=_pem(root))
    client_ctx.verify_flags |= ssl.VERIFY_X509_STRICT
    c_in = ssl.MemoryBIO()
    c_out = ssl.MemoryBIO()
    s_in = ssl.MemoryBIO()
    s_out = ssl.MemoryBIO()
    client = client_ctx.wrap_bio(c_in, c_out, server_hostname=hostname)
    server = server_ctx.wrap_bio(s_in, s_out, server_side=True)
    for step in range(10):
        try:
            client.do_handshake()
            return "OK"
        except ssl.SSLWantReadError:
            pass
        except ssl.SSLCertVerificationError as e:
            return e.verify_message
        except ssl.SSLError as e:
            return e.reason
        s_in.write(c_out.read())
        try:
            server.do_handshake()
        except ssl.SSLWantReadError:
            pass
        except ssl.SSLError:
            pass
        c_in.write(s_out.read())
    return "no answer"
