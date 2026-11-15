# Task 5: raise the price

**Goal:** you intercepted an encrypted invoice for a small amount. Change the ciphertext so that party B accepts a price of exactly **50 000 010 PLN**. You do not know the key.

**Ready:** `tamper.py` holds the ciphertext `D23FBFD09C33F19D` and sends it to party B. `server.py` plays party B: it decrypts the invoice and prints the price it accepted. Treat it as a black box: do not look inside.

The format of the invoice is known: **8 decimal digits, as ASCII text**. For example `00000010` means 10 PLN. The price is small, so the first digit is almost surely `0`.

## Steps

Write the code in place of the `TODO` line in `tamper.py`:

1. Which byte holds the digit you want to change?
2. What must you XOR it with? (A digit `d` in ASCII is the byte `0x30 + d`.)
3. Run it. Party B prints the price it accepted.

## Run

```
python3 tamper.py
```

About 6 minutes. Python 3, no extra libraries.
