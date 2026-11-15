# Task 6: a cheap generator

**Goal:** a company uses a stream cipher with a weak generator. Your analysis shows that its keystream is just **4 numbers** (0 to 255), repeated again and again: `k1 k2 k3 k4 k1 k2 k3 k4 ...`. You know that the plaintext starts with the name `Anna`. Decrypt the whole message.

**Ready:** `cheap.py` holds the intercepted ciphertext and the known start:

```
F6448B019B0A9108D20A9601D14FC503D84E8040DE59C5578413D44E
```

## Steps

Write the code in place of the `TODO` lines in `cheap.py`:

1. Find the 4 numbers.
2. Decrypt the whole ciphertext and print it.

Hint: `i % 4` is the remainder after dividing `i` by 4 (mod), so it goes around 0, 1, 2, 3:

| `i`     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |
|---------|---|---|---|---|---|---|---|---|-----|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | ... |

## Run

```
python3 cheap.py
```

About 5 minutes. Python 3, no extra libraries.
