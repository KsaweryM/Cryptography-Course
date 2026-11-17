# Task 2: find a collision of a short hash.
# short_hash keeps only the first bits of SHA-256. With fewer bits, a collision comes much sooner.
import hashlib
import time


def short_hash(data, bits):
    """Ready: the first `bits` bits of SHA-256(data), as a whole number (0 to 2^bits - 1)."""
    full = hashlib.sha256(data).digest()
    return int.from_bytes(full, "big") >> (256 - bits)


def find_collision(bits):
    """Returns (i, j): two different numbers whose messages "note i" and "note j" have the same short hash."""
    seen = {}   # short hash -> the number i of the message that gave it (like a hash table in C)
    i = 0
    while True:
        message = ("note %d" % i).encode()
        # TODO 1: h = short_hash(message, bits)
        # TODO 2: if h is already a key in seen (h in seen), return (seen[h], i): the earlier message and this one
        # TODO 3: otherwise remember it: seen[h] = i
        return None   # remove this line when TODO 1 to 3 are done
        i = i + 1


BITS = [24, 32, 40]
for k in range(len(BITS)):
    bits = BITS[k]
    start = time.perf_counter()
    found = find_collision(bits)
    seconds = time.perf_counter() - start
    if found is None:
        print(f"{bits} bits: not done yet: TODO 1 to 3")
        continue
    i = found[0]
    j = found[1]
    h = short_hash(("note %d" % j).encode(), bits)
    predicted = 1.18 * 2 ** (bits / 2)
    # TODO 4: replace the line below with
    #   print(f"{bits} bits: note {i} and note {j} -> {h:x}, after {j + 1} messages (predicted about {predicted:.0f}), {seconds:.2f} s")
    print(f"{bits} bits: not done yet: TODO 4")
