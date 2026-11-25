import hashlib
from sha256_ready import pad, compress, state_to_bytes

# Alice keeps a note m secret. She published only its SHA-256 and its length.
DIGEST = bytes.fromhex("778f6ad42722dd774c220d32698fef05f2940678a97374ef79c04e9f18ddab78")
LENGTH = 38
# Mallory wants the digest of a longer message that starts with Alice's note and ends with her own bytes.
EXTRA = b" P.S. Give Mallory the key."


def pad_continued(extra, done):
    """Ready: extra, then the padding of a whole message of done + len(extra) bytes (0x80, zeros, the length).
    Use it when the first done bytes of the message have already gone through compress."""
    out = bytearray(extra)
    out.append(0x80)
    while (done + len(out)) % 64 != 56:
        out.append(0)
    out += ((done + len(extra)) * 8).to_bytes(8, "big")
    return bytes(out)


# TODO 1: the digest is the whole last state. Turn the 32 bytes of DIGEST back into the 8 words of the state:
#         word i is int.from_bytes(DIGEST[4 * i:4 * i + 4], "big"), for i = 0 to 7 (like reading 8 big-endian
#         uint32_t from a buffer in C). Then: print("state from the digest: %08x ..." % state[0])
state = None
print("not done yet: TODO 1")

# TODO 2: the padding of Alice's note depends only on its length. glue = the bytes that pad() puts after a
#         message of LENGTH bytes: pad(bytes(LENGTH))[LENGTH:] (bytes(LENGTH) is LENGTH zero bytes; the content
#         does not matter, only the length). Then: print("glue:", len(glue), "bytes:", glue.hex())
glue = None
print("not done yet: TODO 2")

# TODO 3: continue the chain without the note: tail = pad_continued(EXTRA, LENGTH + len(glue)), then
#         for i = 0, 64, ... below len(tail): state = compress(state, tail[i:i + 64]).
#         forged = state_to_bytes(state); print("Mallory's digest:", forged.hex())
forged = None
print("not done yet: TODO 3")

# The check is ready. Only the check knows Alice's note; Mallory's code above never uses it.
SECRET_NOTE = b"Alice's note: the vault code is 7319.\n"
if forged is not None:
    real = hashlib.sha256(SECRET_NOTE + glue + EXTRA).digest()
    print("SHA-256(note + glue + extra):", real.hex())
    print("the same:", forged == real)
