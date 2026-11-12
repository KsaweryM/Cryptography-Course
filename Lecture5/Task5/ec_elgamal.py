# The small curve from the slides: y^2 = x^3 + 2x + 2 mod 17, G = (5, 1), 19 points
a, b, p = 2, 2, 17
G = (5, 1)
O = None


def add(P, Q):
    """Ready: point addition."""
    if P is O:
        return Q
    if Q is O:
        return P
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]
    if x1 == x2 and (y1 + y2) % p == 0:
        return O
    if P == Q:
        s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (s * s - x1 - x2) % p
    return (x3, (s * (x1 - x3) - y1) % p)


def mul(k, P):
    """Ready: k P = P + P + ... + P (k times)."""
    R = O
    for _ in range(k):
        R = add(R, P)
    return R


def neg(P):
    """Ready: -P, the point with the opposite y. P + (-P) = O."""
    return (P[0], -P[1] % p)


d = 7              # Bartek's private key
Q = mul(d, G)      # Bartek's public key
M = (13, 10)       # the message, already turned into a point of the curve


def encrypt(M, Q, k):
    # TODO 1: C1 = k G,  C2 = M + k Q.  Return (C1, C2).
    return None


def decrypt(C1, C2, d):
    # TODO 2: S = d C1,  M = C2 - S  (that is: C2 + neg(S)).  Return M.
    return None


C = encrypt(M, Q, 4)
print("Q =", Q)
print("ciphertext (C1, C2):", C)
if C is not None:
    print("decrypted:", decrypt(C[0], C[1], d))
