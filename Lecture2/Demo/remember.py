# Ready example: does the output remember the key?
# Many random keys. For each key: is the first output byte equal to key[0]?
#   RC4:      S[0] after the key schedule (Lecture 1, Task 7)
#   ChaCha20: the first keystream byte
# If the output forgets the key, this happens by chance: 1 in 256 = 0.39%.
import random

from rc4 import ksa
from chacha import chacha20

random.seed(2026)        # the same keys in every run
KEYS = 100_000
nonce = bytes(12)        # 12 zero bytes

rc4_hits = 0
chacha_hits = 0
for n in range(KEYS):
    key = random.randbytes(16)
    S = ksa(key)
    if S[0] == key[0]:
        rc4_hits += 1

    key = random.randbytes(32)
    z = chacha20(key, nonce, 0, bytes(1))   # the first keystream byte
    if z[0] == key[0]:
        chacha_hits += 1

print(f"{KEYS} random keys: first output byte == key[0] ?")
print(f"  RC4      S[0] == key[0]          {100 * rc4_hits / KEYS:5.2f}%")
print(f"  ChaCha20 first byte == key[0]    {100 * chacha_hits / KEYS:5.2f}%")
print(f"  chance                           {100 / 256:5.2f}%")
