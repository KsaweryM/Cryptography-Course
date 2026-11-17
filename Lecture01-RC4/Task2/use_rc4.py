from rc4 import keystream

key = b"Kangaroo"
ciphertext = bytes.fromhex("24F8BF0ADE0C16426D343A28"
                           "F5558755720EF505F96EB7C0972B61E7")

# TODO 1: make a keystream as long as the ciphertext
#         and print its length

# TODO 2: XOR each ciphertext byte with its keystream byte,
#         turn each result into a character, print the message

# TODO 3: print keystream(key, 8) and keystream(b"Kangarop", 8)
#         in hex. How many bytes are the same?
