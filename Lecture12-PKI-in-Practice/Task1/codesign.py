# Ready helper for Task 1: code signing and timestamps. Treat it as a black box.
#
#   load_cert(path)                         -> a certificate (cryptography x509.Certificate)
#   load_updates(path)                      -> a list of updates; each one is a dict:
#        u["file"]       the file name (str)
#        u["data"]       the bytes of the file
#        u["signature"]  Alice's signature over the bytes
#        u["timestamp"]  the timestamp token (a dict) or None if there is none
#   verify_signature(cert, data, signature) -> True / False, with the public key of cert
#   verify_timestamp(tsa_cert, signature, token)
#                                           -> the time written in the token (a datetime) if the TSA signed it,
#                                              None if the token was changed or not made by this TSA
#   valid_from(cert), valid_until(cert)     -> the validity period of cert (datetimes in UTC)
#   NOW                                     -> the current date and time (UTC)
#   load_crl(path)                          -> the revocation list (CRL) of Trusty Code CA
#   revoked_since(crl, cert)                -> None if cert is not revoked; otherwise the time since when
#                                              its key must not be trusted (a datetime in UTC)
#
# Simplified: a real timestamp (RFC 3161) is a signed ASN.1 structure; here the TSA signs
# SHA-256(signature) followed by the time as text. The idea is the same.
# The certificates and the CRL were already checked against Trusty Code CA (the chain is fine).
# revoked_since gives the "invalidity date" of the CRL entry (RFC 5280, 5.3.2): the day the key was
# known to be compromised, which can be earlier than the day the CA revoked the certificate.
import datetime
import hashlib
import json

from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

NOW = datetime.datetime.now(datetime.timezone.utc)


def load_cert(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificate(f.read())


def load_updates(path):
    with open(path) as f:
        items = json.load(f)
    updates = []
    for i in range(len(items)):
        it = items[i]
        updates.append({"file": it["file"], "data": bytes.fromhex(it["data"]),
                        "signature": bytes.fromhex(it["signature"]), "timestamp": it["timestamp"]})
    return updates


def verify_signature(cert, data, signature):
    try:
        cert.public_key().verify(signature, data, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


def verify_timestamp(tsa_cert, signature, token):
    message = hashlib.sha256(signature).digest() + token["time"].encode()
    try:
        tsa_cert.public_key().verify(bytes.fromhex(token["tsa_signature"]), message, ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        return None
    t = datetime.datetime.strptime(token["time"], "%Y-%m-%dT%H:%M:%SZ")
    return t.replace(tzinfo=datetime.timezone.utc)


def _utc(t):
    return t.replace(tzinfo=datetime.timezone.utc)


def valid_from(cert):
    # cryptography 42+ has not_valid_before_utc; 41 only has the naive not_valid_before (also UTC)
    if hasattr(cert, "not_valid_before_utc"):
        return cert.not_valid_before_utc
    return _utc(cert.not_valid_before)


def valid_until(cert):
    if hasattr(cert, "not_valid_after_utc"):
        return cert.not_valid_after_utc
    return _utc(cert.not_valid_after)


def load_crl(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_crl(f.read())


def revoked_since(crl, cert):
    entry = crl.get_revoked_certificate_by_serial_number(cert.serial_number)
    if entry is None:
        return None
    try:
        return _utc(entry.extensions.get_extension_for_class(x509.InvalidityDate).value.invalidity_date)
    except x509.ExtensionNotFound:
        if hasattr(entry, "revocation_date_utc"):
            return entry.revocation_date_utc
        return _utc(entry.revocation_date)
