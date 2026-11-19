import hashlib

NAME = "editor-2.4.1-installer.bin"
MIRRORS = ["mirror-a", "mirror-b", "mirror-c"]


def read_sums(path):
    """The first digest in a SHA256SUMS file (a line: 64 hex digits, two spaces or " *", the file name). Ready."""
    with open(path) as f:
        return f.readline().split()[0]


def sha256_of_file(path):
    """The SHA-256 of a file as 64 hex digits, read in pieces of 4096 bytes."""
    h = hashlib.sha256()
    # TODO 1: open the file with open(path, "rb") as f, then in a loop:
    #         piece = f.read(4096); stop when piece is empty (b""); otherwise h.update(piece)
    #         (like fread() into a 4096-byte buffer in C, until it returns 0)
    #         at the end: return h.hexdigest()
    return None


# The digest that Alice published on her website (saved in website/SHA256SUMS)
published = read_sums("website/SHA256SUMS")
print("Alice's website says:", published)

if sha256_of_file("website/SHA256SUMS") is None:
    print("not done yet: TODO 1")
else:
    # TODO 2: for every mirror m in MIRRORS: compute sha256_of_file(m + "/" + NAME) and compare it with published.
    #         print("%s: %s" % (m, "OK" if ... else "CHANGED"))
    print("not done yet: TODO 2")

    # TODO 3: now check every mirror against the SHA256SUMS file on the mirror itself: read_sums(m + "/SHA256SUMS")
    #         print("%s against its own SHA256SUMS: %s" % (m, "OK" if ... else "CHANGED"))
    print("not done yet: TODO 3")
