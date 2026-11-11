import random, sys
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "Task8"))
from rc4 import ksa, prga
random.seed(2026)
counts = [0] * 256
for _ in range(100_000):
    z = prga(ksa(random.randbytes(16)), 2)
    counts[0x61 ^ z[1]] += 1
top = sorted(range(256), key=lambda v: -counts[v])[:4]
print([(hex(v), counts[v]) for v in top])
