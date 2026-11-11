import struct

MASK = 0xFFFFFFFF


def sub32(a, b):
    return (a - b) & MASK


def rotr32(x, n):
    """Rotation to the RIGHT: undoes rotl32(x, n)."""
    return ((x >> n) | (x << (32 - n))) & MASK


# A broken ChaCha20: 20 rounds, but WITHOUT adding the initial state at the end.
# You intercepted one output block (16 words). The key is secret.
output = [
    0xED7CAF84, 0xEC59AB67, 0x182353F4, 0x51B53075,
    0xAFB4B0A5, 0x9D9A8A93, 0xDD172DE6, 0x23A7A16E,
    0x38E2E4CA, 0xA52D3212, 0x2D79C87F, 0x382257EC,
    0x83607414, 0x11654B3C, 0xA14846FD, 0x36134694,
]


def inverse_quarter_round(s, a, b, c, d):
    # TODO: undo the quarter round. Go through its 12 steps backwards:
    #   a += b; d ^= a; d = rotl(d, 16)
    #   c += d; b ^= c; b = rotl(b, 12)
    #   a += b; d ^= a; d = rotl(d, 8)
    #   c += d; b ^= c; b = rotl(b, 7)
    # The last step goes first: b = rotr32(b, 7), then b ^= s[c], then c = sub32(c, d), ...
    # Use s[a], s[b], s[c], s[d] (the list s is changed in place).
    pass


s = output[:]
for _ in range(10):
    # undo one diagonal round, then one column round (in the opposite order)
    inverse_quarter_round(s, 3, 4, 9, 14)
    inverse_quarter_round(s, 2, 7, 8, 13)
    inverse_quarter_round(s, 1, 6, 11, 12)
    inverse_quarter_round(s, 0, 5, 10, 15)
    inverse_quarter_round(s, 3, 7, 11, 15)
    inverse_quarter_round(s, 2, 6, 10, 14)
    inverse_quarter_round(s, 1, 5, 9, 13)
    inverse_quarter_round(s, 0, 4, 8, 12)

print("constants:", " ".join(f"{w:08x}" for w in s[0:4]))
print("key:      ", struct.pack("<8I", *s[4:12]))
