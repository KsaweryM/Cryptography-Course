MASK = 0xFFFFFFFF   # 32 ones: keeps only the lowest 32 bits


def add32(a, b):
    # TODO 1: add a and b and keep only 32 bits (addition mod 2**32)
    pass


def rotl32(x, n):
    # TODO 2: rotate the 32-bit word x left by n bits
    #         the bits that fall out on the left come back on the right
    pass


tests = [
    ("add32", add32(0x00000001, 0x00000002), 0x00000003),
    ("add32", add32(0xFFFFFFFF, 0x00000001), 0x00000000),
    ("add32", add32(0x80000000, 0x80000001), 0x00000001),
    ("rotl32", rotl32(0x00000001, 4), 0x00000010),
    ("rotl32", rotl32(0x80000001, 1), 0x00000003),
    ("rotl32", rotl32(0x12345678, 16), 0x56781234),
]
for name, got, expected in tests:
    status = "OK  " if got == expected else "FAIL"
    shown = "nothing" if got is None else f"{got:#010x}"
    print(f"{status} {name}: got {shown}, expected {expected:#010x}")
