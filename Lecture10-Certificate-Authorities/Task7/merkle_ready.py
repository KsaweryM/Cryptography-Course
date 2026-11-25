# Ready helpers for Task 7 (a Certificate Transparency log as a Merkle tree).
# Treat this file as a black box: you only need the names listed here.
# The hashing is the one of RFC 6962 (Certificate Transparency), section 2.1:
# the Merkle tree of Lecture 6 with one more byte in front (its 'Good to know' slide).
#
#   leaf_hash(entry)          SHA-256(0x00 || entry): the hash of one entry of the log (bytes in, 32 bytes out)
#   node_hash(left, right)    SHA-256(0x01 || left || right): the hash of a node from its two children
#   tree_root(entries)        the root of the Merkle tree over a list of entries (32 bytes)
#   load_log(path)            the entries of a log, one per line (a list of bytes)
#   load_sth(path)            the Signed Tree Head published by the log: (tree size, root)
#   load_hash(path)           one hash from a file (32 bytes)
#   short(h)                  the first 8 hex digits of a hash, for printing
#
# The bytes 0x00 and 0x01 in front keep a leaf and a node apart: nobody can pass a node off as an entry.

import hashlib


def leaf_hash(entry):
    return hashlib.sha256(b"\x00" + entry).digest()


def node_hash(left, right):
    return hashlib.sha256(b"\x01" + left + right).digest()


def tree_root(entries):
    # RFC 6962: split at the largest power of two smaller than the number of entries
    n = len(entries)
    if n == 0:
        return hashlib.sha256(b"").digest()
    if n == 1:
        return leaf_hash(entries[0])
    k = 1
    while k * 2 < n:
        k = k * 2
    return node_hash(tree_root(entries[:k]), tree_root(entries[k:]))


def load_log(path):
    entries = []
    with open(path, "rb") as f:
        for line in f.read().split(b"\n"):
            if line != b"":
                entries.append(line)
    return entries


def load_sth(path):
    size = None
    root = None
    with open(path) as f:
        for line in f:
            words = line.split()
            if len(words) == 2 and words[0] == "tree_size":
                size = int(words[1])
            if len(words) == 2 and words[0] == "root":
                root = bytes.fromhex(words[1])
    return (size, root)


def load_hash(path):
    with open(path) as f:
        return bytes.fromhex(f.read().strip())


def short(h):
    return h.hex()[:8]
