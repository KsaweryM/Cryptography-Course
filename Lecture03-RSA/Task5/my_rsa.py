# Two secret primes, about 20 digits each
p = 37908704904578413183
q = 58606630333925820283
e = 65537   # step 6 of the README: try 3 here, then put 65537 back

message = 2026   # the number we want to send; it must be smaller than n

# TODO 1: n = p times q
n = None
# TODO 2: phi = (p - 1) times (q - 1)
phi = None
# TODO 3: d = the inverse of e mod phi
d = None
# TODO 4: C = message to the power e mod n (encrypt with the public key e, n)
C = None
# TODO 5: P = C to the power d mod n (decrypt with the private key d, n)
P = None

# The printing is ready: it says "not done yet" until every TODO is done. P must be 2026.
if n is None:
    print("not done yet: TODO 1")
elif phi is None:
    print("not done yet: TODO 2")
elif d is None:
    print("not done yet: TODO 3")
elif C is None:
    print("not done yet: TODO 4")
elif P is None:
    print("not done yet: TODO 5")
else:
    print("n =", n)
    print("d =", d)
    print("C =", C)
    print("P =", P)
