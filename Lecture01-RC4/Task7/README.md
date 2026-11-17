# Task 7: does S remember the key?

## The situation

The KSA uses the key to shuffle the table `S` (the numbers 0 to 255). A good shuffle should hide the key: looking at `S` should tell you nothing about it. Here you test one cell. How often does `S[0]` end up equal to `key[0]`? You compare the KSA with a fair random shuffle of the same table.

![A random key of 16 bytes starting with 245 goes through ksa(key). The resulting S starts with 245, the same as the first key byte, so it counts. A fair shuffle of the same table starts with 248, so it does not count. Repeat for 10 000 random keys and count both cases: ksa_hits and shuffle_hits.](figure.svg)

## Goal

Two percentages: how often `S[0] == key[0]` after the KSA, and after a fair shuffle.

## Ready for you

- `rc4.py`: `ksa(key)` returns the table `S` (a list of 256 numbers) after the KSA.
- `remember.py`: the loop over 10 000 random keys of 16 bytes (`key = random.randbytes(16)`), the counters `ksa_hits` and `shuffle_hits`, and the two `print` lines with the percentages.

## Steps

Write your code in place of the `TODO` comments in `remember.py`, inside the loop:

1. `S = ksa(key)`. If `S[0] == key[0]`, add 1 to `ksa_hits`.
2. Now a fair shuffle instead of the KSA: `S = list(range(256))`, then `random.shuffle(S)` (it shuffles the list `S` in place). If `S[0] == key[0]`, add 1 to `shuffle_hits`.
3. Run it and compare the two percentages. Before you run it, guess the second one.

Hint: `ksa_hits += S[0] == key[0]` works, because `True` counts as 1 (as in C, where a comparison gives 1 or 0).

Bonus: why is the first percentage so high? Look at the KSA step `i = 0` on the slides.

## Expected output

Two lines. The numbers change a little on every run, because the keys are random.

<details>
<summary>Check your answer</summary>

```
KSA:     37.25%
shuffle: 0.39%
```

About 37% and about 0.4%.

</details>

## Run

```
python3 remember.py
```

It runs about a second. About 5 minutes. Python 3.9 or newer (for `random.randbytes`), no extra libraries.

Want to see it move? Count it yourself in the simulator: [S remembers the key](https://ksawerym.github.io/Cryptography-simulators/rc4/#4).
