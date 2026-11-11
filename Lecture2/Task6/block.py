import struct

MASK = 0xFFFFFFFF
CONSTANTS = [0x61707865, 0x3320646E, 0x79622D32, 0x6B206574]   # "expand 32-byte k"


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(s, a, b, c, d):
    """Ready. Changes the words s[a], s[b], s[c], s[d] of the list s."""
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 16)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 12)
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 8)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 7)


def chacha20_block(key, counter, nonce):
    # TODO 1: the initial state, 16 words:
    #         CONSTANTS + 8 key words + counter + 3 nonce words
    #         struct.unpack("<8I", key) reads 8 little-endian words
    start = []

    # TODO 2: copy the state and run 10 double rounds on the copy:
    #   a column round:
    #     (0, 4, 8, 12) (1, 5, 9, 13) (2, 6, 10, 14) (3, 7, 11, 15)
    #   a diagonal round:
    #     (0, 5, 10, 15) (1, 6, 11, 12) (2, 7, 8, 13) (3, 4, 9, 14)
    s = start[:]

    # TODO 3: add the initial state to the result, word by word, with add32

    # TODO 4: return the 16 words as 64 bytes: struct.pack("<16I", *s)
    return b""


# Test vector from RFC 8439, section 2.3.2
key = bytes(range(32))
nonce = bytes.fromhex("000000090000004a00000000")
got = chacha20_block(key, 1, nonce)
expected = bytes.fromhex(
    "10f1e7e4d13b5915500fdd1fa32071c4c7d1f4c733c068030422aa9ac3d46c4e"
    "d2826446079faa0914c2d705d98b02a2b5129cd1de164eb9cbd083e8a2503c4e"
)
print("got:     ", got.hex())
print("expected:", expected.hex())
print("OK" if got == expected else "FAIL")
