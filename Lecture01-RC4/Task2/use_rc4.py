from rc4 import keystream

key = b"Kangaroo"
ciphertext = bytes.fromhex("24F8BF0ADE0C16426D343A28"
                           "F5558755720EF505F96EB7C0972B61E7")

ks = b""
# TODO 1: make a keystream as long as the ciphertext:
#         ks = keystream(key, len(ciphertext))

if len(ks) == 0:
    print("not done yet: TODO 1")
else:
    print(len(ks))

message = ""
for i in range(len(ks)):
    # TODO 2: XOR ciphertext byte i with keystream byte i, turn the result
    #         into a character with chr and add it to message
    pass

if message == "":
    print("not done yet: TODO 2")
else:
    print(message)

# TODO 3: print keystream(key, 8) and keystream(b"Kangarop", 8) in hex,
#         one line each (data.hex(" ") gives "69 9d da ..."). How many bytes are the same?
#         Replace the line below with your two print lines.
print("not done yet: TODO 3")
