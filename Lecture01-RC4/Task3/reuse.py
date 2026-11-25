c1 = bytes.fromhex("A6DA32D597798F52E64D6A1147E60F")
c2 = bytes.fromhex("BFD732A1E77D8452EE4A6A1C568170")
p1 = b"MEET ME AT 9 PM"


def xor_bytes(a, b):
    out = []
    for i in range(len(a)):
        pass  # TODO 1: append a[i] ^ b[i] to out
    return bytes(out)


z = b""
# TODO 2: get the keystream from c1 and p1.
#         C1 = P1 XOR Z, so Z = C1 XOR P1: z = xor_bytes(c1, p1)

if xor_bytes(b"\x01", b"\x03") != b"\x02":
    print("not done yet: TODO 1")
elif len(z) == 0:
    print("not done yet: TODO 2")
else:
    # TODO 3: decrypt c2 with z and print it as text (.decode() turns bytes into text).
    #         Replace the line below.
    print("not done yet: TODO 3")
