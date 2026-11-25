from server import receive

ciphertext = bytearray.fromhex("D23FBFD09C33F19D")
original = bytes(ciphertext)

i = None  # TODO 1: the index of the byte that holds the digit you want to change
x = None  # TODO 2: the value to XOR it with (the digit d in ASCII is the byte 0x30 + d)

if i is None:
    print("not done yet: TODO 1")
elif x is None:
    print("not done yet: TODO 2")
else:
    # TODO 3: change that one byte: ciphertext[i] = ciphertext[i] ^ x
    if bytes(ciphertext) == original:
        print("not done yet: TODO 3")
    else:
        receive(bytes(ciphertext))   # Bob decrypts and prints the price he accepts
