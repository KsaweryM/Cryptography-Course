"""Three signature schemes with the same four functions. Ready to use: you do not need to read it.

    NAMES                                   ["RSA-2048", "ECDSA P-256", "Ed25519"]
    load_keys(name)                         -> (private_key, public_key) of Alice, from the PEM files
    sign(name, private_key, data)           -> the signature as bytes
    verify(name, public_key, data, sig)     -> True or False
    public_key_size(name, public_key)       -> the size of the public key in bytes

RSA-2048 is RSA-PSS with SHA-256 (as used in practice). ECDSA P-256 uses SHA-256; its signature is
returned as the two numbers r and s, 32 bytes each. Ed25519 hashes with SHA-512 inside.
"""
import os

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature

NAMES = ["RSA-2048", "ECDSA P-256", "Ed25519"]
_FILES = {"RSA-2048": "alice_rsa_private.pem", "ECDSA P-256": "alice_ecdsa_private.pem",
          "Ed25519": "alice_ed25519_private.pem"}
_PSS = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32)
_here = os.path.dirname(os.path.abspath(__file__))


def load_keys(name):
    with open(os.path.join(_here, _FILES[name]), "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    return private_key, private_key.public_key()


def sign(name, private_key, data):
    if name == "RSA-2048":
        return private_key.sign(data, _PSS, hashes.SHA256())
    if name == "ECDSA P-256":
        r, s = decode_dss_signature(private_key.sign(data, ec.ECDSA(hashes.SHA256())))
        return r.to_bytes(32, "big") + s.to_bytes(32, "big")
    return private_key.sign(data)


def verify(name, public_key, data, sig):
    try:
        if name == "RSA-2048":
            public_key.verify(sig, data, _PSS, hashes.SHA256())
        elif name == "ECDSA P-256":
            r = int.from_bytes(sig[:32], "big")
            s = int.from_bytes(sig[32:], "big")
            public_key.verify(encode_dss_signature(r, s), data, ec.ECDSA(hashes.SHA256()))
        else:
            public_key.verify(sig, data)
        return True
    except InvalidSignature:
        return False


def public_key_size(name, public_key):
    if name == "RSA-2048":
        return public_key.key_size // 8                      # the modulus n (e = 65537 is the same for all)
    if name == "ECDSA P-256":
        raw = public_key.public_bytes(serialization.Encoding.X962, serialization.PublicFormat.CompressedPoint)
        return len(raw)                                       # the point Q: x and one bit of y
    raw = public_key.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    return len(raw)
