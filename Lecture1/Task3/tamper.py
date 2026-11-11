from server import receive

ciphertext = bytearray.fromhex("D23FBFD09C33F19D")

# TODO: change the ciphertext

receive(bytes(ciphertext))
