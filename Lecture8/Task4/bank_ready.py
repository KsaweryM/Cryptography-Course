"""Alice's public RSA key and the two payment orders Alice signed for Mallory. Ready: you do not need to read it.

    n, e                the public key {e, n} of Alice: everybody may know it (Mallory too)
    amount_1, sig_1     the first order: an amount in pounds and Alice's signature on it
    amount_2, sig_2     the second order
    short(x)            a big number as text: its first and last 12 hex digits
"""
import os

from cryptography.hazmat.primitives import serialization

_here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_here, "alice_rsa_public.pem"), "rb") as _f:
    _key = serialization.load_pem_public_key(_f.read())
n = _key.public_numbers().n
e = _key.public_numbers().e

# each line of orders.txt: the amount, then the signature as hex
with open(os.path.join(_here, "orders.txt")) as _f:
    _lines = _f.read().split("\n")
amount_1 = int(_lines[0].split()[0])
sig_1 = int(_lines[0].split()[1], 16)
amount_2 = int(_lines[1].split()[0])
sig_2 = int(_lines[1].split()[1], 16)


def short(x):
    text = format(x, "x")
    if len(text) <= 24:
        return text
    return text[:12] + "..." + text[-12:] + " (" + str(len(text)) + " hex digits)"
