import hashlib
import time

# Alice's door lock stores only the first k bits of the SHA-256 digest of her secret phrase.
PHRASE = b"Alice: the door code is 0886"


def short_hash(data, k):
    """The first k bits of SHA-256(data), as a number (k is at most 32). Ready, no TODO here."""
    d = hashlib.sha256(data).digest()
    first32 = (d[0] << 24) | (d[1] << 16) | (d[2] << 8) | d[3]
    return first32 >> (32 - k)


def invert(target, k):
    """Try the inputs b"0", b"1", b"2", ... until one has short_hash(input, k) == target.
    Return the number of tries and that input."""
    tries = 0
    i = 0
    # TODO 1: the loop: make the input str(i).encode() (like sprintf(buf, "%d", i) in C), add 1 to tries,
    #         return (tries, the input) when short_hash(input, k) == target, else go on with i + 1
    return None


# TODO 2: for k = 12, 16 and 20: target = short_hash(PHRASE, k), then (tries, found) = invert(target, k);
#         measure the time with t0 = time.perf_counter() before and time.perf_counter() - t0 after.
#         Print one line per k:  print("k = %2d: %9d tries (2^k = %9d), %6.2f s, found %s" % (...))
#         Keep the last tries and seconds: you need them in TODO 3.
last_tries = None
last_seconds = None

# TODO 3: your speed: rate = last_tries / last_seconds (hashes per second).
#         The full 256 bits need about 2^256 tries: years = 2**256 / rate / (365 * 24 * 3600)
rate = None
years = None

# The printing is ready.
if invert(short_hash(b"x", 8), 8) is None:
    print("not done yet: TODO 1")
if last_tries is None:
    print("not done yet: TODO 2")
if rate is None:
    print("not done yet: TODO 3")
else:
    print("your speed: %.0f hashes per second" % rate)
    print("all 256 bits: about %.1e years" % years)
