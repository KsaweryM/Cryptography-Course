import hashlib

# Alice's secret seed: only Alice's phone knows it.
ALICE_SEED = bytes.fromhex("a3f1c2d4e5b60718293a4b5c6d7e8f90")

# What Bob's server stored when Alice signed up: x100, the seed hashed 100 times.
SERVER_STORED = bytes.fromhex("48e65d057174a2b686556baa3467311b14d7a1348d1a55693b7ff3243afddce1")

# Five logins that arrived at Bob's server, in this order (32 bytes each, in hex).
LOGINS = [
    "775a180a29500feffceacd21ccc31f4bf6497c23197343706acca99aefb2297e",
    "701c86087b23ab9df81fabcda75902cbe48f6233af06909e28f8b62e25cb1fb9",
    "701c86087b23ab9df81fabcda75902cbe48f6233af06909e28f8b62e25cb1fb9",
    "6d616c6c6f727920747269657320746869732076616c75652031323334353637",
    "a683a514c3d179933b7699d1a0c4920646fd808943c7f71956a88466c879c1e5",
]


def H(x):
    """SHA-256 of x, as 32 bytes. Ready."""
    return hashlib.sha256(x).digest()


# TODO 1: Alice's phone: hash the seed 100 times (x = ALICE_SEED, then 100 times x = H(x)) to get x100
x100 = None

# TODO 2: the server, for each login in LOGINS (in order): value = bytes.fromhex(login);
#         if H(value) == stored: print("login %d: OK" % n) and from now on stored = value
#         else: print("login %d: REJECTED" % n)
#         Start with stored = SERVER_STORED; n counts the logins from 1.

# The printing for TODO 1 is ready.
if x100 is None:
    print("not done yet: TODO 1")
else:
    print("x100 from the seed:", x100.hex())
    print("the same as on the server:", x100 == SERVER_STORED)
print("not done yet: TODO 2")
