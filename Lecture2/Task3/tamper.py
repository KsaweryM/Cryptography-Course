# Task 3: change one byte.
from aead import seal, open_          # aead.py is ready

key   = bytes.fromhex("0badc0de" * 8)
nonce = bytes.fromhex("000000000000000000000001")

# TODO 1: packet = seal(key, nonce, b"Pay Bob 100")

# TODO 2: flip one byte of the packet

# TODO 3: try open_(key, nonce, packet) and print what happens
#         try: ... except ValueError as e: print(e)
