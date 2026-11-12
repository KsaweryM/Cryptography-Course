import random

from rc4 import ksa, prga

KEYS = 100_000
counts = [0, 0, 0]

for _ in range(KEYS):
    key = random.randbytes(16)
    z = prga(ksa(key), 3)
    # TODO: count how often z[0], z[1], z[2] are 0

for n in range(3):
    print(f"byte {n + 1}: {100 * counts[n] / KEYS:.3f}%")
