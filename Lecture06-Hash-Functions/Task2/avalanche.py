import hashlib

MESSAGE = b"Meet Carol at the library at 10:00"


def flip_bit(data, i):
    """A copy of data with bit number i changed (bit 0 is the lowest bit of byte 0). Ready, no TODO here."""
    out = bytearray(data)
    out[i // 8] = out[i // 8] ^ (1 << (i % 8))
    return bytes(out)


def count_diff_bits(a, b):
    """The number of bit positions where a and b differ (a and b have the same length)."""
    count = 0
    # TODO 1: for every index i: x = a[i] ^ b[i] (1 where the bits differ), then count the ones in x:
    #         while x != 0: count = count + (x & 1); x = x >> 1
    return None


# TODO 2: one change: hash MESSAGE and flip_bit(MESSAGE, 0) with SHA-256 (.digest(), 32 bytes each),
#         then count the differing bits of the two digests
d1 = None
d2 = None
one_pair = None

# TODO 3: 1000 trials. Trial t (t = 0 .. 999):
#           m1 = MESSAGE + t.to_bytes(4, "big")       (a different message for every trial)
#           m2 = flip_bit(m1, t % (8 * len(m1)))      (the same message with one bit changed)
#           diff = count_diff_bits(SHA-256 of m1, SHA-256 of m2)
#         keep the smallest diff, the largest diff and the sum (for the average);
#         also add 1 to histogram[diff]
smallest = None
largest = None
total = 0
histogram = [0] * 257

# The printing is ready: each line says "not done yet" until its TODO is done.
if count_diff_bits(b"\x0f", b"\x01") is None:
    print("not done yet: TODO 1")
else:
    print("test: 0x0f and 0x01 differ in", count_diff_bits(b"\x0f", b"\x01"), "bits (should be 3)")
if one_pair is None:
    print("not done yet: TODO 2")
else:
    print("digest 1:", d1.hex())
    print("digest 2:", d2.hex())
    print("one bit changed in the message,", one_pair, "of 256 bits changed in the digest")
if smallest is None:
    print("not done yet: TODO 3")
else:
    print("1000 trials: smallest", smallest, " largest", largest, " average", total / 1000)
    print("how many trials gave each number of changed bits (one # per 5 trials):")
    for diff in range(100, 157, 4):
        n = 0
        for j in range(diff, diff + 4):
            n = n + histogram[j]
        print("  %3d to %3d: %s %d" % (diff, diff + 3, "#" * (n // 5), n))
