# Task 5: ElGamal on a curve

`ec_elgamal.py` uses the small curve from the slides. `add`, `mul` and `neg` are ready, and so are Bartek's keys
(d = 7, Q = 7G) and the message point M = (13, 10). Fill in the `TODO`s:

1. `encrypt`: C1 = kG and C2 = M + kQ.
2. `decrypt`: S = d C1, then M = C2 - S.

## Run

```
python3 ec_elgamal.py
```

Python 3.8 or newer, no extra libraries.
