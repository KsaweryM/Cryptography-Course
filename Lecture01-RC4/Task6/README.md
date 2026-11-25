# Task 6: a cheap generator

## The situation

A company saved money on its stream cipher. A good generator, like RC4, makes a keystream that does not repeat in any time we could wait (its state has about 2<sup>1700</sup> values). Theirs makes only **4 numbers** (0 to 255) and repeats them forever: `k1 k2 k3 k4 k1 k2 k3 k4 ...`. So `k1` encrypts bytes 0, 4, 8, ..., `k2` encrypts bytes 1, 5, 9, ..., and so on. You intercepted a ciphertext and know that it is a letter for Bob that starts with `Dear`: 4 known letters give the 4 numbers, and the 4 numbers open everything.

![Top: the cheap generator gives k1 k2 k3 k4 again and again, while RC4 gives 69 9D DA 7E FE 61 73 62 97 C5 8C AB and does not repeat. Bottom: positions 0 to 11, i % 4 going 0 1 2 3 0 1 2 3, the ciphertext F3 4F 84 12 97 68 8A 02 9B 0A 91 08, the keystream k1 to k4 repeated, and the message starting with Dear. Example: k1 = F3 XOR D = B7.](figure.svg)

## Goal

Find the 4 numbers and print the whole message.

## Ready for you

- `cheap.py`: the intercepted `ciphertext` (32 bytes) and the known start `known = b"Dear"`:

```
F34F841297688A029B0A9108D20A9601D14FC503D84E8040DE59C5578413D44E
```

## Steps

Write your code in place of the `TODO` comments in `cheap.py`:

1. Find the 4 numbers: `numbers[0] = ciphertext[0] ^ known[0]`, and so on up to `numbers[3] = ciphertext[3] ^ known[3]` (a loop over `k = 0, 1, 2, 3`).
2. Decrypt the whole ciphertext: XOR byte `i` with `numbers[i % 4]`, turn the result into a character with `chr` and add it to `message`. The program prints the message.

Until a step is done, the program prints `not done yet: TODO n` for it.

Hint: `i % 4` is the remainder after dividing `i` by 4, so it goes around 0, 1, 2, 3:

| `i`     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |
|---------|---|---|---|---|---|---|---|---|-----|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | ... |

## Expected output

One line: the message, 32 characters, starting with `Dear`.

<details>
<summary>Check your answer</summary>

```
Dear Bob, the safe code is 7391.
```

</details>

## Run

```
python3 cheap.py
```

About 5 minutes. Python 3, no extra libraries.
