# Task 6: does S remember the key?

`rc4.py` is ready: `ksa(key)` returns the table `S` after the KSA. Fill in the `TODO`s in `remember.py`:

1. For 10 000 random keys of 16 bytes, run `S = ksa(key)` and count how often `S[0] == key[0]`.
2. Do the same with a fair random shuffle instead of the KSA: `S = list(range(256))`, then `random.shuffle(S)`.

Compare the two percentages. Bonus: why is the first one so high? Look at the step `i = 0` of the KSA.

## Run

```
python3 remember.py
```

It takes about a second. Python 3.9 or newer (for `random.randbytes`), no extra libraries.
