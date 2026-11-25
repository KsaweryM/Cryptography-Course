import hashlib
import math

# Alice's release: 8 files, in this order (the leaves 0 to 7 of her Merkle tree).
NAMES = ["README.txt", "editor.py", "fonts.dat", "icons.dat", "plugins.py", "spell-en.dat", "spell-pl.dat", "LICENSE.txt"]

# The one digest on Alice's website: the root of the tree of her 8 files.
ROOT = "34e794e769407be83f9770594c5ba82db229c669b5f0a18a0f0cc9475cb56d76"

# Bob downloaded only spell-en.dat (leaf 5) from a mirror. The mirror also sent him a proof: on every level
# from the leaves up, the digest of the sibling, and on which side of Bob's digest it stands.
BOB_INDEX = 5
PROOF = [
    ("left", "9fa8f3949c94a965abab022e781f1ace7ddee71ba1e0d548138c9d06635025bc"),
    ("right", "d8a5bea8457d3649f9f79fcad6447a5abb63b77513c7cd1a059bb1f9f5fa79f8"),
    ("left", "8045c72a8f87a618a2a034be3c80b0613d36958c59b2242de72ed2fabd5f14ae"),
]


def H(data):
    """SHA-256 as 32 bytes."""
    return hashlib.sha256(data).digest()


def read(name):
    return open(name, "rb").read()


# TODO 1: build the tree of the 8 files in release/ and print its root.
#         The leaves: level = a list with H(file) of every file, in the order of NAMES.
#         Then, while the level has more than one digest, make the next level up: the parent of the
#         digests i and i + 1 (i = 0, 2, 4, ...) is H(left + right). The last single digest is the root.
#         print("my root:", root.hex())
#         print("the same as on Alice's website:", root.hex() == ROOT)
print("not done yet: TODO 1")


def verify(data, proof, root_hex):
    """True when the file data with this proof leads to the root root_hex."""
    # TODO 2: start with h = H(data). For every (side, sibling_hex) in the proof, from the first to the last:
    #         the sibling is bytes.fromhex(sibling_hex); if side is "left", the parent is H(sibling + h),
    #         otherwise H(h + sibling). At the end compare h with the root.
    return None


if verify(b"", PROOF, ROOT) is None:
    print("not done yet: TODO 2")
else:
    print("Bob's spell-en.dat from an honest mirror:", verify(read("release/spell-en.dat"), PROOF, ROOT))
    print("Mallory's spell-en.dat, the same proof:  ", verify(read("mirror-spell-en.dat"), PROOF, ROOT))

# TODO 3: predict first, then compute: how many digests does a proof need for a tree of n files,
#         for n = 8, 1024 and 1 000 000? One per level: math.ceil(math.log2(n)). Compare its size in bytes
#         (32 per digest) with a list of all n digests (32 * n bytes).
#         print("%9d files: proof %2d digests = %4d bytes, a list of all digests %10d bytes" % (n, k, 32 * k, 32 * n))
print("not done yet: TODO 3")
