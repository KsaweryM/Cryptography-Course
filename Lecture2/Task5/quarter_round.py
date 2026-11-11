MASK = 0xFFFFFFFF


def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(a, b, c, d):
    # TODO: the four lines of the ChaCha20 quarter round
    #   a += b; d ^= a; d = rotl(d, 16)
    #   c += d; b ^= c; b = rotl(b, 12)
    #   a += b; d ^= a; d = rotl(d, 8)
    #   c += d; b ^= c; b = rotl(b, 7)
    # use add32 for += and rotl32 for rotl
    return a, b, c, d


# Test vector from RFC 8439, section 2.1.1
got = quarter_round(0x11111111, 0x01020304, 0x9B8D6F43, 0x01234567)
expected = (0xEA2A92F4, 0xCB1CF8CE, 0x4581472E, 0x5881C4BB)
print("got:     ", " ".join(f"{w:#010x}" for w in got))
print("expected:", " ".join(f"{w:#010x}" for w in expected))
print("OK" if got == expected else "FAIL")
