"""Alice's RSA key, 2048 bits, as three numbers. Ready to use: you do not need to read it.

    n, e                the public key {e, n}: everybody may know it
    d                   the private key {d, n}: only Alice has it
    number_to_bytes(x)  the opposite of int.from_bytes(data, "big")
    short(x)            a big number as text: its first and last 12 hex digits
"""
import os

from cryptography.hazmat.primitives import serialization

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "alice_rsa_private.pem"), "rb") as _f:
    _key = serialization.load_pem_private_key(_f.read(), password=None)

n = _key.private_numbers().public_numbers.n
e = _key.private_numbers().public_numbers.e
d = _key.private_numbers().d


def number_to_bytes(x):
    length = (x.bit_length() + 7) // 8
    return x.to_bytes(length, "big")


def short(x):
    text = format(x, "x")
    if len(text) <= 24:
        return text
    return text[:12] + "..." + text[-12:] + " (" + str(len(text)) + " hex digits)"
