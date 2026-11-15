# Task 3: find k

## The situation

Eve has a public point T = kG and wants the secret number k. On a real curve that is the ECDLP, and nobody can do it. Here the curves are small: p has only 16, 20 and 24 bits. So Eve can try the simplest attack there is: start at G and keep adding G until she reaches T. How long does it take, and how does the time grow when p gets longer?

![Top: G, 2G, 3G, 4G, ..., T in violet boxes joined by arrows labelled +G; T is outlined in orange and next to it "k = ?". Below, one row per curve y^2 = x^3 + ax + b mod p. 16 bits: p = 50459, a = 13422, b = 27875, G = (1710, 42410), T = (49665, 28300). 20 bits: p = 896107, a = 808927, b = 241789, G = (119763, 855066), T = (490971, 493613). 24 bits: p = 9788083, a = 4564841, b = 5425030, G = (7065671, 8730247), T = (619167, 4946861). Each row ends with "k = ?" and a stopwatch with "? s". Under it: add(P, Q, a, p) is ready. Each p is 4 bits longer: how many times longer does the search take?](figure.svg)

## Goal

Find k on all three curves and see how the time grows with the size of p.

## Ready for you

- `ecdlp.py`: `add(P, Q, a, p)` adds two points of the curve (`None` is O).
- `PROBLEMS`: the three curves, each with `p`, `a`, `b`, the base point `G` and the public point `T`.
- The loop at the end calls `find_k(p, a, G, T)` for each curve and prints the bits of p, your k and the time.

Before you run it, predict: each p is 4 bits longer. How many times longer will the search take?

## Steps

Write your code in place of the `TODO` in `find_k` in `ecdlp.py`:

1. Start with `R = G` and `k = 1`. Keep adding G, `R = add(R, G, a, p)`, and count with `k`, until `R == T`. Then return `k`.
   - `R == T` compares two tuples element by element: both x and both y must be equal.

## Expected output

Three lines, one per curve: the bits of p, the k you found and the time. Your times will be different; the last curve takes about 15 to 20 seconds.

<details>
<summary>Check your answer</summary>

```
16 bits: k = 37100   0.081 s
20 bits: k = 826876   1.541 s
24 bits: k = 8762309   19.343 s
```

The k values must be exactly these. The time grows with k, the number of additions: here each 4 more bits made the search about 19 and 13 times longer. For 256 bits it would be about 2^255 additions.

</details>

## Run

```
python3 ecdlp.py
```

About 6 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? In the [elliptic-curves simulator, step 1](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#1), Eve runs the same attack on the curve mod 17.
