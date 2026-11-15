# Task 1: decrypt a message

**Goal:** you received a ciphertext. You and the sender share a one-time pad: random bytes, as many as the message has. Decrypt the message.

**Ready:** `decrypt.py` holds the 11 ciphertext bytes and the 11 pad bytes:

```
ciphertext  A3 FA 1B ED D8 14 BE 1A C2 6B 2F
pad         EB 9F 77 81 B7 34 CA 72 A7 19 4A
```

## Steps

Write the code in place of the `TODO` lines in `decrypt.py`:

1. XOR each ciphertext byte with its pad byte. In Python: `c ^ p`.
2. Each result is an ASCII code. Turn it into a letter. In Python: `chr(72)` gives `H`.
3. Print the whole message.

## Run

```
python3 decrypt.py
```

About 5 minutes. Python 3, no extra libraries.
