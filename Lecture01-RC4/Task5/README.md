# Task 5: raise the price

## The situation

Party A sends party B an encrypted invoice: the price in PLN, as **8 decimal digits in ASCII**, for example `00000010` for 10 PLN. You sit between them. You cannot read the invoice and you do not know the key, but you can change bytes on the way. A stream cipher works byte by byte, so XOR on one ciphertext byte changes exactly the same byte of the plaintext.

![Party A sends a ciphertext, you change it, party B receives it. A's invoice says 00000010. The plaintext bytes are 30 30 30 30 30 30 31 30, the ciphertext is D2 3F BF D0 9C 33 F1 9D. You XOR only byte 0 with an unknown x, and B decrypts 35 30 30 30 30 30 31 30, that is 50000010, and accepts it.](figure.svg)

## Goal

Change the intercepted ciphertext so that party B accepts a price of exactly **50 000 010 PLN**.

## Ready for you

- `tamper.py`: the intercepted ciphertext `D2 3F BF D0 9C 33 F1 9D` in `ciphertext` (a `bytearray`, so you can change one byte: `ciphertext[i] ^= x`). At the end it sends the ciphertext to party B.
- `server.py`: plays party B. It decrypts the invoice and prints the price it accepts. Treat it as a black box: do not look inside.

The price is small, so the first digit is almost surely `0`.

## Steps

Write your code in place of the `TODO` comment in `tamper.py`:

1. Which byte holds the digit you want to change?
2. What must you XOR it with? A digit `d` in ASCII is the byte `0x30 + d`, and you want `0x30` to become `0x35`.
3. Change that one byte, then run the program. Party B prints the price it accepted.

## Expected output

Before your change, the program prints `Invoice accepted: 10 PLN`. When it works:

```
Invoice accepted: 50000010 PLN
```

## Run

```
python3 tamper.py
```

About 6 minutes. Python 3, no extra libraries.
