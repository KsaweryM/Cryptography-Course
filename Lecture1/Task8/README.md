# Task 8: crack a short key

**Goal:** two messages were encrypted with RC4 and very short keys: the first with a key of 1 byte, the second with a key of 2 bytes. You know that every message starts with `Hello`. Find both keys by brute force, and estimate how long longer keys would take.

**Ready:** `rc4.py`: `keystream(key, n)` returns `n` bytes of keystream. `crack.py` holds both ciphertexts and a ready loop that runs `crack(c1, 1)` and `crack(c2, 2)` and prints the time of each.

## Steps

Write the code in place of the `TODO` lines in `crack.py`:

1. Write `crack(ciphertext, n)`: try every key of `n` bytes. Return a list of all keys whose keystream turns the start of the ciphertext into `known`.
2. Decrypt both messages with the keys you found and print them.
3. The program prints the time for each key length. From these, estimate (do not run it!) how long the same search would take for a key of 5 bytes, and of 16 bytes.

Hint: all keys of `n` bytes ($256^n$ of them; in Python `256 ** n`):

```python
for k in range(256 ** n):
    key = k.to_bytes(n, "big")
```

## Run

```
python3 crack.py
```

The 2-byte search takes a few seconds. About 8 minutes. Python 3, no extra libraries.
