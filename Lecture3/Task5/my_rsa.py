# Two secret primes, about 20 digits each
p = 37908704904578413183
q = 58606630333925820283
e = 65537

message = 2026   # the number we want to send; it must be smaller than n

# TODO 1: n = ...
# TODO 2: phi = ...
# TODO 3: d = ...          (the inverse of e mod phi: pow(e, -1, phi))
# TODO 4: C = ...          (encrypt message with the public key e, n)
# TODO 5: P = ...          (decrypt C with the private key d, n)
# Then print n, d, C and P. P must be 2026.
