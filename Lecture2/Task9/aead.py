"""ChaCha20-Poly1305 (RFC 8439) in plain Python. Ready to use: you do not need to read it."""
import struct

MASK = 0xFFFFFFFF


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(s, a, b, c, d):
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 16)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 12)
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 8)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 7)


def initial_state(key, counter, nonce):
    return ([0x61707865, 0x3320646E, 0x79622D32, 0x6B206574]
            + list(struct.unpack("<8I", key))
            + [counter]
            + list(struct.unpack("<3I", nonce)))


def run_rounds(s, rounds):
    for r in range(rounds):
        if r % 2 == 0:
            quarter_round(s, 0, 4, 8, 12); quarter_round(s, 1, 5, 9, 13)
            quarter_round(s, 2, 6, 10, 14); quarter_round(s, 3, 7, 11, 15)
        else:
            quarter_round(s, 0, 5, 10, 15); quarter_round(s, 1, 6, 11, 12)
            quarter_round(s, 2, 7, 8, 13); quarter_round(s, 3, 4, 9, 14)


def block(key, counter, nonce, rounds=20):
    start = initial_state(key, counter, nonce)
    s = start[:]
    run_rounds(s, rounds)
    s = [add32(x, y) for x, y in zip(s, start)]
    return struct.pack("<16I", *s)


def chacha20(key, nonce, counter, data):
    out = bytearray()
    for i in range(0, len(data), 64):
        ks = block(key, counter + i // 64, nonce)
        out += bytes(x ^ y for x, y in zip(data[i:i + 64], ks))
    return bytes(out)


def poly1305(key, msg):
    r = int.from_bytes(key[:16], "little") & 0x0FFFFFFC0FFFFFFC0FFFFFFC0FFFFFFF
    s = int.from_bytes(key[16:], "little")
    p = (1 << 130) - 5
    acc = 0
    for i in range(0, len(msg), 16):
        n = int.from_bytes(msg[i:i + 16] + b"\x01", "little")
        acc = (acc + n) * r % p
    return ((acc + s) & ((1 << 128) - 1)).to_bytes(16, "little")


def _pad16(x):
    return b"\x00" * (-len(x) % 16)


def _tag(key, nonce, ciphertext, aad):
    one_time_key = block(key, 0, nonce)[:32]          # block 0 gives the Poly1305 key
    mac_data = (aad + _pad16(aad) + ciphertext + _pad16(ciphertext)
                + struct.pack("<QQ", len(aad), len(ciphertext)))
    return poly1305(one_time_key, mac_data)


def seal(key, nonce, plaintext, aad=b""):
    """Encrypt and add a 16-byte tag. Returns ciphertext + tag."""
    ciphertext = chacha20(key, nonce, 1, plaintext)    # the data starts at block 1
    return ciphertext + _tag(key, nonce, ciphertext, aad)


class TagError(Exception):
    pass


def unseal(key, nonce, sealed, aad=b""):
    """Check the tag, then decrypt. Raises TagError if anything was changed."""
    ciphertext, tag = sealed[:-16], sealed[-16:]
    if _tag(key, nonce, ciphertext, aad) != tag:
        raise TagError("the tag does not match: the message was changed")
    return chacha20(key, nonce, 1, ciphertext)
