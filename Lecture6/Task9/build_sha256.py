import hashlib
from sha256_ready import IV, pad, compress, state_to_bytes

# TODO 1: predict first, then check: how many 64-byte blocks does pad() make from messages of
#         3, 55, 56 and 64 bytes? For each n: padded = pad(bytes(n)), blocks = len(padded) // 64
#         print("%2d bytes -> %3d bytes after padding, %d block(s)" % (n, len(padded), blocks))
print("not done yet: TODO 1")


def my_sha256(message):
    """SHA-256 built from its parts (Merkle-Damgard): pad, then one compress per block."""
    # TODO 2: padded = pad(message); state = IV
    #         for every block (i = 0, 64, 128, ... below len(padded)): state = compress(state, padded[i:i + 64])
    #         print the first word of the state after each block: print("  after block %d: %08x ..." % (k, state[0]))
    #         at the end: return state_to_bytes(state)
    return None


# The test is ready: it compares my_sha256 with hashlib for two messages (one block and two blocks).
tests = [b"abc", b"The quick brown fox jumps over the lazy dog, then over the lazy cat, then home."]
for m in tests:
    print(len(m), "bytes:", m)
    mine = my_sha256(m)
    if mine is None:
        print("not done yet: TODO 2")
    else:
        print("  mine:   ", mine.hex())
        print("  hashlib:", hashlib.sha256(m).hexdigest())
        print("  the same:", mine == hashlib.sha256(m).digest())
