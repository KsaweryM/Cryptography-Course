# Task 2: a real exchange

`dh.py` holds the public 2048-bit prime P and G = 2 from RFC 3526 (group 14). Fill in the `TODO`s:

1. Pick Ania's secret a and Bartek's secret b (random 256-bit numbers).
2. Compute A = G^a mod P and B = G^b mod P.
3. Compute the shared secret on both sides: B^a mod P and A^b mod P.
4. Print whether they are equal, and the first 20 digits of the secret: `str(secret)[:20]`.

## Run

```
python3 dh.py
```

Python 3, no extra libraries.
