# Task 7: does S remember the key?

**Goal:** measure whether the table `S` after the KSA still remembers the first byte of the key, and compare it with a fair shuffle.

**Ready:** `rc4.py`: `ksa(key)` returns the table `S` after the KSA. `remember.py` has the loop over 10 000 random keys of 16 bytes and prints both percentages.

## Steps

Write the code in place of the `TODO` lines in `remember.py`:

1. `S = ksa(key)`: count how often `S[0] == key[0]` (add 1 to `ksa_hits`).
2. The same with a fair random shuffle instead of the KSA: `S = list(range(256))`, then `random.shuffle(S)` (it shuffles the list `S` in place). Count in `shuffle_hits`.
3. Compare the two percentages.

Bonus: why is the first one so high? Look at the step `i = 0` of the KSA on the slides.

Hint: `ksa_hits += S[0] == key[0]` works, because `True` counts as 1.

## Run

```
python3 remember.py
```

It takes about a second. About 5 minutes. Python 3.9 or newer (for `random.randbytes`), no extra libraries.
