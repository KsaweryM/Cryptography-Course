"""ECDSA on the curve P-256 (FIPS 186-5), with SHA-256. Ready to use: you do not need to read it.

    q                      the order of G: every ECDSA number (k, d, r, s, z) is taken mod q
    hash_number(data)      z: the SHA-256 of the data, read as one big-endian number
    public_key(d)          the public key Q = d x G, as a pair (x, y)
    sign(d, data)          a new signature (r, s) with the private key d (a fresh random k inside)
    verify(Q, data, r, s)  True or False; the check is done by the library "cryptography"
"""
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature

# the curve y^2 = x^3 + a x + b mod p, the starting point G and its order q (FIPS 186-5 / SP 800-186, P-256)
p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a = p - 3
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
G = (0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
     0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
q = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551


def _add(P, Q):
    # adding two points, as in Lecture 5; None is the point at infinity O
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and (P[1] + Q[1]) % p == 0:
        return None
    if P == Q:
        s = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p) % p
    else:
        s = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p
    x = (s * s - P[0] - Q[0]) % p
    y = (s * (P[0] - x) - P[1]) % p
    return (x, y)


def _mul(k, P):
    # double and add, as in Lecture 5
    R = None
    while k > 0:
        if k & 1:
            R = _add(R, P)
        P = _add(P, P)
        k = k >> 1
    return R


def hash_number(data):
    return int.from_bytes(hashlib.sha256(data).digest(), "big")


def public_key(d):
    return _mul(d % q, G)


def sign_with_k(d, data, k):
    # textbook ECDSA signing with a given k: r = x of kG mod q, s = (z + r d) / k mod q
    z = hash_number(data)
    r = _mul(k, G)[0] % q
    s = (z + r * d) * pow(k, -1, q) % q
    return (r, s)


def sign(d, data):
    key = ec.derive_private_key(d, ec.SECP256R1())
    der = key.sign(data, ec.ECDSA(hashes.SHA256()))
    return decode_dss_signature(der)


def verify(Q, data, r, s):
    public = ec.EllipticCurvePublicNumbers(Q[0], Q[1], ec.SECP256R1()).public_key()
    try:
        public.verify(encode_dss_signature(r, s), data, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False
