# Task 4: your own RSA

Goal: make your own RSA key from two primes, then encrypt and decrypt the number 2026.

`my_rsa.py` gives two primes p and q (about 20 digits each, so that the result fits on the screen)
and the public exponent e = 65537. Fill in the `TODO`s:

1. n = p · q
2. phi = (p - 1)(q - 1)
3. d, the inverse of e mod phi: in Python `pow(e, -1, phi)`
4. C = message^e mod n: in Python `pow(message, e, n)`
5. P = C^d mod n

Print n, d, C and P. P must be the original message, 2026.

## Run

```
python3 my_rsa.py
```

Python 3.8 or newer (for `pow(e, -1, phi)`), no extra libraries.

## Expected output

```
n = 2221701454780507748530735154427775990789
d = 1367151349159148221410861819858768950381
C = 736246060401132335090489988934276767570
P = 2026
```
