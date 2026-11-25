# Task 2: jump to the middle.
# chacha.py is ready: chacha20(key, nonce, counter, data).
import time

from chacha import chacha20

key   = bytes.fromhex("5eed" * 16)
nonce = bytes.fromhex("000000000000000000000002")

# film.bin: a ciphertext of 1000 blocks (64 000 bytes)
data = open("film.bin", "rb").read()

block = None     # the 64 bytes of block 700
frame = None     # block 700, decrypted
one = None       # seconds for one block
all701 = None    # seconds for blocks 0 to 700

# TODO 1: cut out block 700         (bytes 700*64 .. 701*64): block = data[...]

# TODO 2: decrypt that block with counter = 700: frame = chacha20(...)

# TODO 3: time it: one block  vs  all 701 blocks (data[0 : 701*64] with counter 0)
#         (time.perf_counter() gives the time in seconds): one = ..., all701 = ...

# The printing is ready: each line says "not done yet" until its TODO is done.
if block is None:
    print("not done yet: TODO 1")
if frame is None:
    print("not done yet: TODO 2")
else:
    print(frame.decode())
if one is None or all701 is None:
    print("not done yet: TODO 3")
else:
    print(f"one block: {one:.5f} s")
    print(f"all 701:   {all701:.5f} s")
