ciphertext = [0xA3, 0xFA, 0x1B, 0xED,
              0xD8, 0x14, 0xBE, 0x1A,
              0xC2, 0x6B, 0x2F]
pad        = [0xEB, 0x9F, 0x77, 0x81,
              0xB7, 0x34, 0xCA, 0x72,
              0xA7, 0x19, 0x4A]

x = None
plaintext = ""
for i in range(len(ciphertext)):
    # TODO 1: XOR the ciphertext byte with the pad byte at the same position:
    #         x = ciphertext[i] ^ pad[i]        (^ is XOR, as in C)
    # TODO 2: x is an ASCII code. Turn it into a letter and add it to the message:
    #         plaintext = plaintext + chr(x)    (chr(x) is the cast (char)x in C)
    pass

if x is None:
    print("not done yet: TODO 1")
elif plaintext == "":
    print("not done yet: TODO 2")
else:
    # TODO 3: print the whole message: replace the line below with print(plaintext)
    print("not done yet: TODO 3")
