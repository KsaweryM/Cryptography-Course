from math import gcd

# Small numbers, as on the slides: p = 23, g = 5, Bartek's private x = 6, public y = g^x mod p = 8
p, g, x = 23, 5, 6
y = pow(g, x, p)


def sign(m, k):
    # TODO 1: k must be coprime with p - 1 (check with gcd).
    #         r = g^k mod p
    #         s = (m - x * r) * (inverse of k mod p - 1)  mod (p - 1)
    #         return (r, s)
    return None


def verify(m, r, s):
    # TODO 2: a signature is valid if  g^m mod p  ==  y^r * r^s mod p
    return None


m = 10
signature = sign(m, 3)
print("signature (r, s):", signature)
if signature is not None:
    r, s = signature
    print("valid for m = 10:", verify(10, r, s))
    print("valid for m = 11:", verify(11, r, s))
