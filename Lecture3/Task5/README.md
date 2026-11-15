# Task 5: does it always work?

Goal: with the key n = 187, e = 7, d = 23, check whether every P from 0 to 186 comes back.

`always.py` holds the small key (p = 17, q = 11) and prints the result.

Predict first: does it also work for P = 17, which divides n?

Fill in the `TODO` in `always.py`:

1. For every P in `range(n)`: encrypt with `pow(P, e, n)`, decrypt with `pow(C, d, n)`,
   and add P to the list `wrong` if the result is not P. One loop and one comparison.

## Run

```
python3 always.py
```

Python 3, no extra libraries.

## Expected output

```
checked: 187 values
wrong:   []
P = 17 -> 85 -> 17
```

RSA works for every P from 0 to n - 1, also for P = 17.
