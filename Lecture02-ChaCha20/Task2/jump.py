# Task 2: jump to the middle.
# chacha.py is ready: chacha20(key, nonce, counter, data).
import time

from chacha import chacha20

key   = bytes.fromhex("5eed" * 16)
nonce = bytes.fromhex("000000000000000000000002")

# film.bin: a ciphertext of 1000 blocks (64 000 bytes)
data = open("film.bin", "rb").read()

# TODO 1: cut out block 700         (bytes 700*64 .. 701*64)

# TODO 2: decrypt that block with counter = 700

# TODO 3: time it: one block  vs  all 701 blocks
#         (time.perf_counter() gives the time in seconds)
