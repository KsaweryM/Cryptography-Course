# Ready for you: digital signatures as a black box (Ed25519, from the library "cryptography").
# We do not look inside. Ed25519 is a signature on edwards25519, another form of Curve25519 (Lecture 5).
#
#   sign(private_key, data)               -> signature (64 bytes)
#   verify(public_key, data, signature)   -> True or False
#   key_hex(public_key)                   -> the 32 bytes of the public key as hex text
#   load_private_key(path), load_public_key(path)   read a key from a PEM file

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization


def load_private_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def load_public_key(path):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def sign(private_key, data):
    return private_key.sign(data)


def verify(public_key, data, signature):
    try:
        public_key.verify(signature, data)
        return True
    except InvalidSignature:
        return False


def key_hex(public_key):
    raw = public_key.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    return raw.hex()
