# Task 6: guess the PIN

Goal: find a PIN without the private key.

A bank encrypts 4-digit PINs with textbook RSA (C = PIN^e mod n) and a 2048-bit key.
Eve intercepted one encrypted PIN. `pin.py` holds the bank's public key (e, n) and the encrypted PIN C.
The time measurement is ready in the file.

Fill in the `TODO` in `pin.py`:

1. Find the PIN without the private key and store it in `pin`.
   Hint: the public key is public, so you can encrypt any number yourself.

## Run

```
python3 pin.py
```

Python 3, no extra libraries.

## Expected output

```
PIN: 4821    found in 0.40 s
```

Your time will be different. Textbook RSA always gives the same ciphertext for the same message,
and there are only 10 000 PINs.
