import hashlib

# The test value of FIPS 202 (the SHA-3 standard, NIST 2015) for the message "abc".
FIPS_SHA3_ABC = "3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532"
DATA = b"Hello, Bob!"

# TODO 1: compute SHA3-256 of b"abc": hashlib.sha3_256(data).hexdigest(), like hashlib.sha256 in Task 1.
#         print("SHA3-256(abc):", abc)
#         print("the same as FIPS 202:", abc == FIPS_SHA3_ABC)
print("not done yet: TODO 1")

# TODO 2: predict first: SHAKE256 gives an output of any length you ask for:
#         hashlib.shake_256(DATA).hexdigest(n) gives n bytes as 2n hex digits.
#         Is the 16-byte output related to the 32-byte one? Then for n = 16, 32 and 64:
#         print("SHAKE256, %2d bytes: %s" % (n, out))
print("not done yet: TODO 2")

# TODO 3: predict first: are SHA3-256(DATA) and the 32-byte SHAKE256(DATA) the same? Both use the same
#         permutation and the same 136-byte blocks. Print both, then whether they are equal:
#         print("SHA3-256:          ", a)
#         print("SHAKE256, 32 bytes:", b)
#         print("the same:", a == b)
print("not done yet: TODO 3")
