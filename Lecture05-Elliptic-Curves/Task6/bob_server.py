"""Bob's side. Ready to use: you do not need to read it.
(As Mallory you could not read it anyway: Bob's private key d is in here.)"""
import hashlib

a, p = 2, 17        # Bob's curve y^2 = x^3 + 2x + 2 mod 17; the formulas below never use b
_d = 17             # Bob's private key: Mallory does not know it


def _add(P, Q):
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
    x3 = (s * s - P[0] - Q[0]) % p
    return (x3, (s * (P[0] - x3) - P[1]) % p)


def key_check(S):
    """A short fingerprint of a point: the first 8 bytes of SHA-256 of "x,y" ("O" for the point at infinity).
    Bob answers with a message encrypted with a key made from S; this fingerprint stands for that answer."""
    text = "O" if S is None else str(S[0]) + "," + str(S[1])
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def bob_reply(P):
    """Bob computes S = d P with the point he received, without any check, and answers with key_check(S)."""
    S = None
    for i in range(_d):
        S = _add(S, P)
    return key_check(S)


def is_bob_secret(d):
    """Only for checking the answer at the end."""
    return d == _d
