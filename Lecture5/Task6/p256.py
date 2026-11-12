"""ECDSA on the NIST curve P-256 in plain Python. Ready to use: you do not need to read it."""
import hashlib

p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a = p - 3
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
G = (0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
     0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
n = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551   # the order of G


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P == Q:
        s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (s * s - x1 - x2) % p
    return (x3, (s * (x1 - x3) - y1) % p)


def mul(k, P):
    """k P by double-and-add."""
    R = None
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R


def h(message):
    """The SHA-256 hash of the message, as a number."""
    return int.from_bytes(hashlib.sha256(message).digest(), "big")


def sign(message, d, k):
    r = mul(k, G)[0] % n
    s = pow(k, -1, n) * (h(message) + r * d) % n
    return r, s


def verify(message, r, s, Q):
    w = pow(s, -1, n)
    P = add(mul(h(message) * w % n, G), mul(r * w % n, Q))
    return P is not None and P[0] % n == r
