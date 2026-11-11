# Task 5: ElGamal in Python

`elgamal.py` holds the 2048-bit group from RFC 3526 and Bartek's keys (private x, public y = G^x mod P).
Fill in the two `TODO`s:

1. `encrypt(M, y)`: a new random k, then C1 = G^k mod P and C2 = M · y^k mod P.
2. `decrypt(C1, C2, x)`: s = C1^x mod P, then M = C2 · s^-1 mod P.

The program encrypts a message twice and decrypts it.

## Run

```
python3 elgamal.py
```

Python 3.8 or newer (for `pow(s, -1, P)`), no extra libraries.
