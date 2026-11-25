# Task 9: is the keystream uniform?

## The situation

A good keystream looks random: every byte value from 0 to 255 is equally likely (**uniform**). Then a keystream byte is 0 with a chance of 1/256 = **0.39%**. Does RC4 keep that promise? You are Eve, looking for any weakness: you test it with 100 000 random keys and count how often each of the first three keystream bytes is 0.

![Seven random keys and their first three keystream bytes. Key 3 gives 00 76 36: a 0 in the first byte, so the first counter grows by 1. Key 6 gives 0A FD 00: a 0 in the third byte. After these 7 keys the counts are 1, 0 and 1. On the right, the three percentages you will measure, each to compare with the uniform line at 1/256 = 0.39%.](figure.svg)

## Goal

Three percentages, one for each of the first three keystream bytes, to compare with 0.39%.

## Ready for you

- `rc4.py`: `ksa(key)` returns the table `S`, `prga(S, n)` returns `n` keystream bytes.
- `measure.py`: the loop over 100 000 random keys of 16 bytes. For each key it makes `z = prga(ksa(key), 3)`, the first 3 keystream bytes. At the end it prints each count as a percentage.

## Steps

Write your code in place of the `TODO` comment in `measure.py`, inside the loop:

1. Count how often `z[0]`, `z[1]` and `z[2]` are 0: for `n = 0, 1, 2`, if `z[n]` is 0, add 1 to `counts[n]`.
2. Run it and compare the three percentages with 0.39%.

Until step 1 is done, the program prints `not done yet: TODO 1`. The module `random` is fine for a measurement like this one; real keys come from `secrets` (see the slides).

## Expected output

Three lines. The numbers change a little on every run, because the keys are random.

<details>
<summary>Check your answer</summary>

```
byte 1: 0.415%
byte 2: 0.832%
byte 3: 0.399%
```

Bytes 1 and 3 stay near 0.39%. Byte 2 is near 0.78%: about **twice** as often as it should be.

Want to see it move? Fill the histogram yourself: [the first bytes](https://ksawerym.github.io/Cryptography-simulators/rc4/#4.2).

</details>

## Run

```
python3 measure.py
```

It runs about 5 seconds. About 5 minutes. Python 3.9 or newer (for `random.randbytes`), no extra libraries.
