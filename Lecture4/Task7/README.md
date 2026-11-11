# Task 7: sign and verify

`sign.py` uses the small numbers from the slides: p = 23, g = 5, Bartek's private key x = 6, public y = 8.
Fill in the two `TODO`s:

1. `sign(m, k)`: r = g^k mod p and s = (m - x·r) · k^-1 mod (p - 1).
2. `verify(m, r, s)`: check g^m mod p == y^r · r^s mod p.

The program signs m = 10 with k = 3, then checks the signature for m = 10 and for m = 11.

## Run

```
python3 sign.py
```

Python 3.8 or newer, no extra libraries.
