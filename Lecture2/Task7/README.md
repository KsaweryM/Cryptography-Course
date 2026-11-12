# Task 7: watch one bit spread

`chacha.py` is ready; its `block(key, counter, nonce, rounds)` lets you choose the number of rounds.
The program computes two blocks that differ in one bit of the counter.

Before you run it, predict: how many of the 512 output bits change after 1 round? After 20 rounds?

Fill in the `TODO` in `avalanche.py`: count the bits that differ. Hints: `out1[i] ^ out2[i]` has a 1 where the two bytes differ, `(x >> k) & 1` is bit `k` of `x`. It takes less than a second.

## Run

```
python3 avalanche.py
```

Python 3, no extra libraries.
