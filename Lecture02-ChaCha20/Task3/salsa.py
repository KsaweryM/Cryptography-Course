# Salsa20 (Bernstein, 2005) in plain Python, ready to use. The older sibling of ChaCha20.
# You do not need to read this file; you need:
#   quarter_round(s, a, b, c, d)   one Salsa20 quarter round on the words s[a], s[b], s[c], s[d]
#   rounds(s, n)                   n rounds on the 4 by 4 table s (odd: columns, even: rows)
#   initial_state(key, counter, nonce)   the start table: key 32 bytes, nonce 8 bytes, counter 64-bit
#   block(key, counter, nonce)     one 64-byte block of keystream (20 rounds + the start table)

MASK = 0xFFFFFFFF   # keeps 32 bits


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(s, a, b, c, d):
    # each word changes once: b, then c, then d, then a
    s[b] ^= rotl32(add32(s[a], s[d]), 7)
    s[c] ^= rotl32(add32(s[b], s[a]), 9)
    s[d] ^= rotl32(add32(s[c], s[b]), 13)
    s[a] ^= rotl32(add32(s[d], s[c]), 18)


def word(data, i):
    # the 32-bit word number i of data, lowest byte first (little-endian)
    return int.from_bytes(data[4 * i:4 * i + 4], "little")


def initial_state(key, counter, nonce):
    # the 4 by 4 table: the constants on the diagonal (words 0, 5, 10, 15),
    # the key in words 1-4 and 11-14, the nonce in 6-7, the counter in 8-9
    s = [0] * 16
    s[0], s[5], s[10], s[15] = 0x61707865, 0x3320646E, 0x79622D32, 0x6B206574
    for i in range(4):
        s[1 + i] = word(key, i)
        s[11 + i] = word(key, 4 + i)
    s[6] = word(nonce, 0)
    s[7] = word(nonce, 1)
    s[8] = counter & MASK
    s[9] = (counter >> 32) & MASK
    return s


def rounds(s, n):
    # n rounds on the table s: odd rounds mix the 4 columns, even rounds the 4 rows
    for r in range(1, n + 1):
        if r % 2 == 1:
            quarter_round(s, 0, 4, 8, 12)    # column round
            quarter_round(s, 5, 9, 13, 1)
            quarter_round(s, 10, 14, 2, 6)
            quarter_round(s, 15, 3, 7, 11)
        else:
            quarter_round(s, 0, 1, 2, 3)     # row round
            quarter_round(s, 5, 6, 7, 4)
            quarter_round(s, 10, 11, 8, 9)
            quarter_round(s, 15, 12, 13, 14)


def block(key, counter, nonce):
    start = initial_state(key, counter, nonce)
    s = list(start)
    rounds(s, 20)
    out = b""
    for i in range(16):
        out += add32(s[i], start[i]).to_bytes(4, "little")
    return out
