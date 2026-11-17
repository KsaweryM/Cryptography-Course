# Task 4: does it always work?

## The situation

The small key from the slides: p = 17, q = 11, so n = 187, e = 7 and d = 23. On the slides, 88 was encrypted to 11 and came back as 88. But is that luck? Some messages P share a factor with n: the multiples of 17 and of 11, such as 17 and 22. Do they come back too? With only 187 possible messages, you can simply try them all.

![always.py: the public key {e, n} = {7, 187} and the private key {d, n} = {23, 187}. For every P: pow(P, 7, 187) gives C, pow(C, 23, 187) should give P again; if not, add P to wrong. Below, a grid of all 187 values from 0 to 186; the multiples of 17 and 11 (0, 11, 17, 22, 33, 34, and so on) are framed in orange: they share a factor with n = 187. Predict first: do they come back?](figure.svg)

## Goal

Check whether every P from 0 to 186 comes back after encrypting and decrypting.

**Predict first:** does it also work for P = 17, which divides n?

## Ready for you

- `always.py`: the small key `n, e, d = 187, 7, 23` and the `print` lines. `wrong` starts as `None` (nothing yet, like `NULL` in C), so the file prints `not done yet` until you fill it in.

## Steps

Write your code in place of the `TODO` comment in `always.py`:

1. Start with an empty list, `wrong = []`. Then for every P in `range(n)` (0 to n - 1, like `for (P = 0; P < n; P++)` in C): encrypt with `C = pow(P, e, n)`, decrypt with `pow(C, d, n)`, and add P to the list with `wrong.append(P)` if the result is not P. One loop and one comparison.

## Expected output

How many values were checked and the list of the ones that did not come back.

<details>
<summary>Check your answer</summary>

```
checked: 187 values
wrong:   []
```

The list is empty: RSA works for every P from 0 to n - 1, also for P = 17 (17 -> 85 -> 17) and the other multiples of 17 and 11.

</details>

## Run

```
python3 always.py
```

About 4 minutes. Python 3, no extra libraries.

Want to see it move? In [Why decryption works](https://ksawerym.github.io/Cryptography-simulators/rsa/#3), the same 187 values with the reason (Euler's theorem), and why the multiples of 17 and 11 work too.
