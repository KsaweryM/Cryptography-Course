import hashlib

from alice_key import n, e, d, short


def read_file(path):
    # like fopen(path, "rb") + fread in C: the whole file as bytes
    with open(path, "rb") as f:
        return f.read()


def hash_number(data):
    # TODO 1: the SHA-256 of data, read as one big-endian number:
    #         int.from_bytes(hashlib.sha256(data).digest(), "big")
    return None


update = read_file("update.bin")     # 100 000 bytes: far more than the 256 bytes of n

# TODO 2: Alice signs the hash of the file: s = hash_number(update)^d mod n
s = None

# TODO 3: Bob checks: he hashes the file he got himself and compares: pow(s, e, n) == hash_number(update)
check = None

# TODO 4: Mallory flips one bit: copy the file into a bytearray (like a uint8_t buffer in C),
#         flip the lowest bit of byte 50000 with ^= 1, then check s on bytes(changed) as in TODO 3.
check_changed = None

# Alice signed the hashes of two orders for Mallory: sig_20 and sig_50, read from signed_orders.txt (hex).
order_20 = b"Pay Mallory 20 pounds. Alice"
order_50 = b"Pay Mallory 50 pounds. Alice"
order_1000 = b"Pay Mallory 1000 pounds. Alice"
lines = read_file("signed_orders.txt").decode().split("\n")
sig_20 = int(lines[0], 16)
sig_50 = int(lines[1], 16)

# TODO 5: the trick of Task 5 against hash-and-sign: Mallory multiplies the two signatures,
#         forged = sig_20 * sig_50 % n, and the bank checks forged on order_1000, as in TODO 3.
check_forged = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if hash_number(update) is None:
    print("not done yet: TODO 1")
else:
    print("file:", len(update), "bytes, its hash as a number:", short(hash_number(update)))
if s is None:
    print("not done yet: TODO 2")
else:
    print("s =", short(s))
if check is None:
    print("not done yet: TODO 3")
else:
    print("Bob checks the file:        ", check)
if check_changed is None:
    print("not done yet: TODO 4")
else:
    print("Bob checks the changed file:", check_changed)
if check_forged is None:
    print("not done yet: TODO 5")
else:
    print("the bank checks the forged 1000:", check_forged)
