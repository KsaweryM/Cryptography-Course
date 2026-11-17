import time

def add(P, Q, a, p):
    """Ready: adds two points of the curve y^2 = x^3 + ax + b mod p. None is the point at infinity O."""
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


# Each line: the curve (p, a, b), the base point G and the public point T = k G. The secret k is unknown.
PROBLEMS = [
    (50459, 13422, 27875, (1710, 42410), (49665, 28300)),   # p has 16 bits
    (896107, 808927, 241789, (119763, 855066), (490971, 493613)),   # p has 20 bits
    (9788083, 4564841, 5425030, (7065671, 8730247), (619167, 4946861)),   # p has 24 bits
]
BITS = [16, 20, 24]   # the number of bits of each p


def find_k(p, a, G, T):
    # TODO: start with R = G and k = 1, keep adding G (R = add(R, G, a, p))
    #       and counting (k = k + 1) until R == T, then return k
    return None


for i in range(len(PROBLEMS)):
    p = PROBLEMS[i][0]
    a = PROBLEMS[i][1]
    G = PROBLEMS[i][3]
    T = PROBLEMS[i][4]
    start = time.perf_counter()
    k = find_k(p, a, G, T)
    seconds = time.perf_counter() - start
    if k is None:
        print(f"{BITS[i]} bits: not done yet: TODO in find_k")
    else:
        print(f"{BITS[i]} bits: k = {k}   {seconds:.3f} s")
