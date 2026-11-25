import random

from rc4 import ksa, prga

KEYS = 100_000
counts = [0, 0, 0]

for _ in range(KEYS):
    key = random.randbytes(16)   # random is fine for a measurement (never for real keys)
    z = prga(ksa(key), 3)
    # TODO 1: for n = 0, 1, 2: if z[n] is 0, add 1 to counts[n]

if counts == [0, 0, 0]:
    print("not done yet: TODO 1")
else:
    for n in range(3):
        print(f"byte {n + 1}: {100 * counts[n] / KEYS:.3f}%")
