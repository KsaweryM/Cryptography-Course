# Ready example: how often is the second keystream byte 0?
# A random byte is 0 in 1 of 256 cases = 0.39%.
import random

from rc4 import prga, ksa
from chacha import chacha20

random.seed(2026)        # the same keys in every run
KEYS = 100_000
nonce = bytes(12)        # 12 zero bytes

rc4_zeros = 0
chacha_zeros = 0
for n in range(KEYS):
    key = random.randbytes(16)
    z = prga(ksa(key), 2)
    if z[1] == 0:
        rc4_zeros += 1

    key = random.randbytes(32)
    z = chacha20(key, nonce, 0, bytes(2))   # the first two keystream bytes
    if z[1] == 0:
        chacha_zeros += 1

print(f"{KEYS} random keys: how often is the second keystream byte 0 ?")
print(f"  RC4       {100 * rc4_zeros / KEYS:.2f}%   ({rc4_zeros} keys)")
print(f"  ChaCha20  {100 * chacha_zeros / KEYS:.2f}%   ({chacha_zeros} keys)")
print(f"  chance    {100 / 256:.2f}%")
