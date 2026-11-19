# Task 4: two real collisions.
#   md5_a.bin,  md5_b.bin   128 bytes each: the MD5 collision of Wang, Feng, Lai and Yu (2004)
#   sha1_a.bin, sha1_b.bin  320 bytes each: the start of the two SHAttered PDF files (2017)
# Part 1 (TODO 1 to 3): which function does each pair break? Part 2 (TODO 4): a viewer that shows two contents.
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


# Part 2: a tiny "viewer". Both files get the same two pages at the end; one byte of the collision block
# decides which page the viewer shows. Both pages are 31 bytes long.
PAGE_1 = b"Alice pays Mallory 100 pounds. "
PAGE_2 = b"Alice pays Mallory 1000 pounds."


def show(data):
    # TODO 4: the viewer. The file is: 128 collision bytes, then PAGE_1, then PAGE_2.
    #   If data[19] == 0x87, return the bytes of page 1: data[128:128 + 31] (a slice: like memcpy of
    #   31 bytes from offset 128 in C); otherwise return the bytes of page 2: data[159:159 + 31].
    return None


a = load_file("md5_a.bin") + PAGE_1 + PAGE_2
b = load_file("md5_b.bin") + PAGE_1 + PAGE_2
if show(a) is None:
    print("viewer: not done yet: TODO 4")
else:
    print("viewer on md5_a.bin + both pages:", show(a).decode())
    print("viewer on md5_b.bin + both pages:", show(b).decode())
    print("  MD5 a:", hashlib.md5(a).hexdigest())
    print("  MD5 b:", hashlib.md5(b).hexdigest())
