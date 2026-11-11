# Task 5: your own RSA

`my_rsa.py` gives two primes p and q and the public exponent e = 65537. Fill in the `TODO`s:

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
