import time

from chacha import chacha20

key = bytes.fromhex("5eed" * 16)
nonce = bytes.fromhex("000000000000000000000002")
film = open("film.bin", "rb").read()       # 1000 blocks of 64 bytes
# Encrypted starting with counter 0: block n used counter n.

start = time.perf_counter()
everything = chacha20(key, nonce, 0, film)
print("whole film:", everything[700 * 64:701 * 64].decode().strip())
print(f"  took {1000 * (time.perf_counter() - start):.1f} ms")

start = time.perf_counter()
# TODO 1: cut block 700 out of the film
#         (bytes 700*64 to 701*64 of the film).

# TODO 2: decrypt ONLY that block.
#         Which counter do you need?
one_block = b""
print("one block:  ", one_block.decode().strip())
print(f"  took {1000 * (time.perf_counter() - start):.1f} ms")
