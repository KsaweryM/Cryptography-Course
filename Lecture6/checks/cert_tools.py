# Ready for you: the boring parts of working with X.509 certificates (library "cryptography").
# We do not look inside.
#
#   load_private_key(path), load_public_key(path)   read a key from a PEM file
#   load_cert(path), save_cert(cert, path)          read and write a certificate in PEM
#   valid_from(cert), valid_until(cert)             notBefore and notAfter, in UTC
#   find_extension(cert, kind)                      the value of one extension, or None
#   ext_name(ext), oid_name(oid)                    a short name of an extension or of an OID
#   key_name(public_key)                            for example "EC P-256" or "RSA 2048"
#   make_cert(subject, issuer, public_key, signing_key)   a certificate as in Task 3
#   show(cert)                                      print the main fields and the fingerprint

import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, rsa

UTC = datetime.timezone.utc


def load_private_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def load_public_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def load_cert(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificate(f.read())


def save_cert(cert, path):
    with open(path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def valid_from(cert):
    # cryptography 42 and newer: not_valid_before_utc; version 41: not_valid_before (no time zone)
    if hasattr(cert, "not_valid_before_utc"):
        return cert.not_valid_before_utc
    return cert.not_valid_before.replace(tzinfo=UTC)


def valid_until(cert):
    if hasattr(cert, "not_valid_after_utc"):
        return cert.not_valid_after_utc
    return cert.not_valid_after.replace(tzinfo=UTC)


def find_extension(cert, kind):
    # kind is a class such as x509.SubjectAlternativeName; None when the certificate has no such extension
    try:
        return cert.extensions.get_extension_for_class(kind).value
    except x509.ExtensionNotFound:
        return None


NAMES = {
    "2.5.29.17": "subjectAltName",
    "2.5.29.19": "basicConstraints",
    "2.5.29.15": "keyUsage",
    "2.5.29.37": "extendedKeyUsage",
    "2.5.29.14": "subjectKeyIdentifier",
    "2.5.29.35": "authorityKeyIdentifier",
    "2.5.29.31": "cRLDistributionPoints",
    "1.3.6.1.5.5.7.1.1": "authorityInfoAccess",
    "2.5.29.32": "certificatePolicies",
    "1.3.6.1.5.5.7.3.1": "serverAuth",
    "1.3.6.1.5.5.7.3.2": "clientAuth",
    "1.3.6.1.5.5.7.3.3": "codeSigning",
    "1.3.6.1.5.5.7.3.4": "emailProtection",
    "1.2.840.10045.4.3.2": "ecdsa-with-SHA256",
    "1.2.840.113549.1.1.11": "sha256WithRSAEncryption",
    "1.3.101.112": "Ed25519",
    "1.3.6.1.4.1.11129.2.4.2": "signedCertificateTimestamps",
}


def oid_name(oid):
    # a short name of an object identifier (OID), or its dotted number when we do not know it
    dotted = oid.dotted_string
    if dotted in NAMES:
        return NAMES[dotted]
    return dotted


def ext_name(ext):
    return oid_name(ext.oid)


def key_name(public_key):
    if isinstance(public_key, ec.EllipticCurvePublicKey):
        if public_key.curve.name == "secp256r1":
            return "EC P-256"
        return "EC " + public_key.curve.name
    if isinstance(public_key, rsa.RSAPublicKey):
        return "RSA " + str(public_key.key_size)
    if isinstance(public_key, ed25519.Ed25519PublicKey):
        return "Ed25519"
    return type(public_key).__name__


def make_cert(subject, issuer, public_key, signing_key):
    # the same builder as in Task 3: serial, 90 days from 1 November 2026, signed with Ed25519
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(issuer)
    builder = builder.serial_number(0x6B1E5A2C9D3F4E70)
    builder = builder.not_valid_before(datetime.datetime(2026, 11, 1, tzinfo=UTC))
    builder = builder.not_valid_after(datetime.datetime(2027, 1, 30, tzinfo=UTC))
    builder = builder.public_key(public_key)
    return builder.sign(signing_key, None)


def colon_hex(data):
    parts = []
    for i in range(len(data)):
        parts.append("%02X" % data[i])
    return ":".join(parts)


def show(cert):
    print("version      ", cert.version.name)
    print("serial       ", hex(cert.serial_number))
    print("issuer       ", cert.issuer.rfc4514_string())
    print("subject      ", cert.subject.rfc4514_string())
    print("not before   ", valid_from(cert))
    print("not after    ", valid_until(cert))
    print("public key   ", key_name(cert.public_key()))
    print("extensions   ", len(cert.extensions))
    print("SHA-256 fingerprint")
    print("   ", colon_hex(cert.fingerprint(hashes.SHA256())))
