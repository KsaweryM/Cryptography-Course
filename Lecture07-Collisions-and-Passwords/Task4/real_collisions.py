# Task 4: two real collisions.
#   md5_a.bin,  md5_b.bin   128 bytes each: the MD5 collision of Wang, Feng, Lai and Yu (2004)
#   sha1_a.bin, sha1_b.bin  320 bytes each: the start of the two SHAttered PDF files (2017)
import hashlib


def load_file(path):
    with open(path, "rb") as f:
        return f.read()


def count_different(a, b):
    # TODO 1: count the positions i where a[i] != b[i] (an index loop over range(len(a)), as in C)
    return None


PAIRS = [("md5_a.bin", "md5_b.bin"), ("sha1_a.bin", "sha1_b.bin")]
SUFFIX = b"Any text that Mallory adds to the end of both files."

for k in range(len(PAIRS)):
    a = load_file(PAIRS[k][0])
    b = load_file(PAIRS[k][1])
    n = count_different(a, b)
    if n is None:
        print(f"{PAIRS[k][0]} and {PAIRS[k][1]}: {len(a)} bytes each, not done yet: TODO 1")
    else:
        print(f"{PAIRS[k][0]} and {PAIRS[k][1]}: {len(a)} bytes each, {n} bytes differ")
    # TODO 2: print the MD5, the SHA-1 and the SHA-256 of a and of b, one line each, for example
    #   print("  MD5     a:", hashlib.md5(a).hexdigest()) and the same for b; hashlib.sha1, hashlib.sha256
    print("  not done yet: TODO 2")
    # TODO 3: add SUFFIX to the end of both (a + SUFFIX, b + SUFFIX) and print their MD5 and SHA-1 again
    print("  not done yet: TODO 3")
