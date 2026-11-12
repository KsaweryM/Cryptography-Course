"""ChaCha20 (RFC 8439) in plain Python. Ready to use: you do not need to read it."""
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
