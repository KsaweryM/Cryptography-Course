import random

from rc4 import rc4


def xor(a, b):
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return bytes(out)


key = b"our secret"
m1 = b"Meet at noon."
m2 = b"Bring the map"

# Step 1: the same key for two messages
# TODO 1: c1 = rc4(key, m1) and c2 = rc4(key, m2), then print:
#         xor(c1, c2) == xor(m1, m2)
#         rc4(key, m1) == rc4(key, m1)      # the same message, sent twice
#         When is this dangerous?

# Step 2: a public value, new for every message
# TODO 2: for every message make a new 3-byte value: random.randbytes(3)
#         It does not have to be secret: it is sent together with the ciphertext.
#         Use it so that:
#         a) xor(c1, c2) == xor(m1, m2) is False
#         b) m1 sent twice, with two new values, gives two different ciphertexts
#         c) your friend, who knows the key and the value, can decrypt c1
# Hint: b"ab" + b"cd" == b"abcd"
