from bob_server import bob_reply, key_check, is_bob_secret

# Bob's curve, the small curve of the slides: y^2 = x^3 + 2x + 2 mod 17, G = (5, 1)
a, b, p = 2, 2, 17
G = (5, 1)
O = None


def add(P, Q):
    """Ready: point addition, the same as in Bob's code. Look: it uses a and p, never b."""
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
    """Ready: k P = P + P + ... + P (k times); 0 P = O."""
    R = O
    for i in range(k):
        R = add(R, P)
    return R


# Mallory's fake points: none of them is on Bob's curve
FAKE = [(3, 2), (0, 8), (2, 3)]


def order(P):
    # TODO 1: the order of P: add P again and again (R = P, then R = add(R, P), ...) and count
    #         until R is O. Return the count n, the smallest n with n P = O.
    return None


def piece(P, n, reply):
    # TODO 2: Bob's point d P is one of O, P, 2P, ..., (n - 1) P. Try j = 0, 1, ..., n - 1:
    #         when key_check(mul(j, P)) == reply, then d mod n = j. Return j.
    return None


def combine(pieces):
    # TODO 3: pieces is a list of pairs (n, r), one per fake point: d mod n = r.
    #         Try d = 1, 2, 3, ... up to the product of all n, and return the first d
    #         with d % n == r for every pair.
    return None


def on_curve(P):
    # TODO 4: you are now Bob's programmer. Return True when y^2 = x^3 + a x + b mod p, else False.
    #         Here b is needed.
    return None


def bob_receives(P):
    """Ready: Bob's front door. A point that fails on_curve is refused (None); any other goes to Bob."""
    if on_curve(P) is False:
        return None
    return bob_reply(P)


# The printing is ready: each line says "not done yet" until its TODO is done.
# The tests use the example of the slides: (7, 1) has order 3, and d mod 3 = 1, 4 = 3, 11 = 7 give d = 7.
done = True
if order(FAKE[0]) is None:
    print("not done yet: TODO 1")
    done = False
if piece((7, 1), 3, key_check((7, 1))) is None:
    print("not done yet: TODO 2")
    done = False
if combine([(3, 1), (4, 3), (11, 7)]) is None:
    print("not done yet: TODO 3")
    done = False
if on_curve(G) is None:
    print("not done yet: TODO 4 (until then Bob accepts every point)")
if done:
    pieces = []
    for i in range(len(FAKE)):
        P = FAKE[i]
        n = order(P)
        reply = bob_receives(P)
        if reply is None:
            print("Mallory sends " + str(P) + ": Bob refuses it, not on the curve")
        else:
            r = piece(P, n, reply)
            print("Mallory sends " + str(P) + ": order " + str(n) + ", Bob's reply " + reply + ", d mod " + str(n) + " = " + str(r))
            pieces.append((n, r))
    if len(pieces) == len(FAKE):
        d = combine(pieces)
        print("Bob's private key: d = " + str(d) + ", correct:", is_bob_secret(d))
    else:
        print("Mallory learned nothing about d")
    if on_curve(G) is not None:
        print("Bob still answers a point of the curve:", bob_receives(G) is not None)
