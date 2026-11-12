from rc4_ready import keystream

key = b"Kangaroo"
ciphertext = bytes.fromhex("24F8BF0ADE0C16426D343A28"
                           "F5558755720EF505F96EB7C0972B61E7")

# TODO 1: decrypt the ciphertext and print it

# TODO 2: compare keystream(key, 8) with keystream(b"Kangarop", 8).
#         Print both in hex. How many bytes match?
