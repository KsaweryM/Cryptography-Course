# Task 9: measure the second byte

**Goal:** check whether the first keystream bytes of RC4 are uniform. If every value were equally likely, a byte would be 0 with a chance of 1/256 = **0.39%**. Is it?

**Ready:** `rc4.py`: `ksa(key)` and `prga(S, n)`. `measure.py` has the loop over 100 000 random keys of 16 bytes, makes `z = prga(ksa(key), 3)` (the first 3 keystream bytes) and prints each count as a percentage.

## Steps

Write the code in place of the `TODO` line in `measure.py`:

1. Count how often `z[0]`, `z[1]` and `z[2]` are 0 (in `counts[0]`, `counts[1]`, `counts[2]`).
2. Run it and compare the three percentages with 0.39%.

## Run

```
python3 measure.py
```

It takes a few seconds. About 5 minutes. Python 3, no extra libraries.
