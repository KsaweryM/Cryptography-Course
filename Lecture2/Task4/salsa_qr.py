MASK = 0xFFFFFFFF


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def salsa_quarter_round(a, b, c, d):
    # TODO: the four lines of the Salsa20 quarter round
    #   b ^= rotl(a + d, 7)
    #   c ^= rotl(b + a, 9)
    #   d ^= rotl(c + b, 13)
    #   a ^= rotl(d + c, 18)
    # use add32 for + and rotl32 for rotl;
    # print a, b, c, d after every line
    return a, b, c, d


a, b, c, d = salsa_quarter_round(0x00000001, 0x00000000, 0x00000000, 0x00000000)
print("result:", " ".join(f"{w:#010x}" for w in (a, b, c, d)))
for w in (a, b, c, d):
    print(f"{w:032b}  ones: {bin(w).count('1')}")
