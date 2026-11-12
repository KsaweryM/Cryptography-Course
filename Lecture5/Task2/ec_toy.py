# The small curve from the slides: y^2 = x^3 + 2x + 2 mod 17, with G = (5, 1)
a, b, p = 2, 2, 17
G = (5, 1)
O = None   # the point at infinity


def add(P, Q):
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
    # TODO 1: the slope s
    #   if P == Q (doubling):   s = (3 * x1^2 + a) / (2 * y1)   mod p
    #   otherwise:              s = (y2 - y1) / (x2 - x1)       mod p
    #   "/ v mod p" means "* pow(v, -1, p)"
    # TODO 2: x3 = s^2 - x1 - x2 mod p,   y3 = s * (x1 - x3) - y1 mod p
    return O


# TODO 3: print G, 2G, 3G, ... by adding G again and again,
#         until you reach O. How many points do you get?
