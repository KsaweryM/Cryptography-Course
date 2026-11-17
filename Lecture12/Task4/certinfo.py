# Ready helper for Task 4: reading certificates. Treat it as a black box.
#
#   load_folder(folder)  -> a list of (file name, certificate), sorted by file name
#   subject_cn(cert)     -> the common name in the subject, e.g. "www.carol-corp.example"
#   issuer_cn(cert)      -> the common name of the issuer, e.g. "Trusty CA"
#   expires(cert)        -> the end of the validity period (a datetime in UTC)
#   key_info(cert)       -> (key type, bits), e.g. ("RSA", 2048), ("EC", 256), ("Ed25519", 256)
#   hash_name(cert)      -> the hash in the CA's signature: "sha256", "sha1", "md5", ...
#                           "none" for Ed25519, which hashes inside the signature itself
import datetime
import os

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519


def load_folder(folder):
    names = sorted(os.listdir(folder))
    out = []
    for i in range(len(names)):
        if names[i].endswith(".pem"):
            with open(os.path.join(folder, names[i]), "rb") as f:
                out.append((names[i], x509.load_pem_x509_certificate(f.read())))
    return out


def subject_cn(cert):
    return cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def issuer_cn(cert):
    return cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def expires(cert):
    # cryptography 42+ has not_valid_after_utc; 41 only has the naive not_valid_after (also UTC)
    if hasattr(cert, "not_valid_after_utc"):
        return cert.not_valid_after_utc
    return cert.not_valid_after.replace(tzinfo=datetime.timezone.utc)


def key_info(cert):
    k = cert.public_key()
    if isinstance(k, rsa.RSAPublicKey):
        return ("RSA", k.key_size)
    if isinstance(k, ec.EllipticCurvePublicKey):
        return ("EC", k.key_size)
    if isinstance(k, ed25519.Ed25519PublicKey):
        return ("Ed25519", 256)
    return ("other", 0)


def hash_name(cert):
    h = cert.signature_hash_algorithm
    if h is None:
        return "none"
    return h.name
