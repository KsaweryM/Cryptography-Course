# Task 6: a cheap generator

## The situation

A company saved money on its stream cipher. A good generator, like RC4, makes a keystream that never repeats. Theirs makes only **4 numbers** (0 to 255) and repeats them forever: `k1 k2 k3 k4 k1 k2 k3 k4 ...`. So `k1` encrypts bytes 0, 4, 8, ..., `k2` encrypts bytes 1, 5, 9, ..., and so on. You intercepted a ciphertext and know that the message starts with the name `Anna`: 4 known letters give the 4 numbers, and the 4 numbers open everything.

![Top: the cheap generator gives k1 k2 k3 k4 again and again, while RC4 gives 69 9D DA 7E FE 61 73 62 97 C5 8C AB and never repeats. Bottom: positions 0 to 11, i % 4 going 0 1 2 3 0 1 2 3, the ciphertext F6 44 8B 01 9B 0A 91 08 D2 0A 96 01, the keystream k1 to k4 repeated, and the message starting with Anna. Example: k1 = F6 XOR A = B7.](figure.svg)

## Goal

Find the 4 numbers and print the whole message.

## Ready for you

- `cheap.py`: the intercepted `ciphertext` (28 bytes) and the known start `known = b"Anna"`:

```
F6448B019B0A9108D20A9601D14FC503D84E8040DE59C5578413D44E
```

## Steps

Write your code in place of the `TODO` comments in `cheap.py`:

1. Find the 4 numbers: `k1 = ciphertext[0] ^ known[0]`, and so on up to `k4 = ciphertext[3] ^ known[3]`. Keep them in a list `numbers` of 4 elements.
2. Decrypt the whole ciphertext: XOR byte `i` with `numbers[i % 4]`. Turn each result into a character with `chr` and print the message.

Hint: `i % 4` is the remainder after dividing `i` by 4, so it goes around 0, 1, 2, 3:

| `i`     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |
|---------|---|---|---|---|---|---|---|---|-----|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | ... |

## Expected output

One line: the message, 28 characters, starting with `Anna`.

<details>
<summary>Check your answer</summary>

```
Anna, the safe code is 7391.
```

</details>

## Run

```
python3 cheap.py
```

About 5 minutes. Python 3, no extra libraries.
