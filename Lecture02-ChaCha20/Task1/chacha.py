# ChaCha20 (RFC 8439) in plain Python, ready to use.
# Treat this file as a black box: you only need chacha20(key, nonce, counter, data).
#   key:     32 bytes
#   nonce:   12 bytes
#   counter: the number of the first 64-byte block
#   data:    the bytes to encrypt or to decrypt (the same call does both)

MASK = 0xFFFFFFFF   # keeps 32 bits


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(s, a, b, c, d):
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 16)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 12)
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 8)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 7)


def word(data, i):
    # the 32-bit word number i of data, lowest byte first (little-endian)
    return int.from_bytes(data[4 * i:4 * i + 4], "little")


def initial_state(key, counter, nonce):
    # the 4 by 4 table: 4 constants, 8 words of key, the counter, 3 words of nonce
    s = [0x61707865, 0x3320646E, 0x79622D32, 0x6B206574]
    for i in range(8):
        s.append(word(key, i))
    s.append(counter)
    for i in range(3):
        s.append(word(nonce, i))
    return s


def rounds(s, n):
    # n rounds on the table s: odd rounds mix the 4 columns, even rounds the 4 diagonals
    for r in range(1, n + 1):
        if r % 2 == 1:
            quarter_round(s, 0, 4, 8, 12)    # column round
            quarter_round(s, 1, 5, 9, 13)
            quarter_round(s, 2, 6, 10, 14)
            quarter_round(s, 3, 7, 11, 15)
        else:
            quarter_round(s, 0, 5, 10, 15)   # diagonal round
            quarter_round(s, 1, 6, 11, 12)
            quarter_round(s, 2, 7, 8, 13)
            quarter_round(s, 3, 4, 9, 14)


def block(key, counter, nonce):
    # one 64-byte block of keystream: 20 rounds, then add the starting table back
    start = initial_state(key, counter, nonce)
    s = list(start)
    rounds(s, 20)
    out = b""
    for i in range(16):
        out += add32(s[i], start[i]).to_bytes(4, "little")
    return out


def chacha20(key, nonce, counter, data):
    out = bytearray(len(data))
    for i in range(len(data)):
        if i % 64 == 0:
            ks = block(key, counter + i // 64, nonce)
        out[i] = data[i] ^ ks[i % 64]
    return bytes(out)
