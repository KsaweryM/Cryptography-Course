# Task 2: a real exchange

## The situation

On paper, Alice and Bob used p = 23. Real Diffie-Hellman uses a public prime of **2048 bits** (617 digits): group 14 from RFC 3526, with g = 2. Each side picks a random 256-bit secret, sends one public value, and computes the shared secret from the value it got. Nobody sends the secret itself.

![The public values p = 32317006071311... (2048 bits, 617 digits) and g = 2, known to everybody, Eve too. Alice picks a secret a and Bob a secret b, both random 256-bit numbers. Alice computes A = g^a mod p, Bob B = g^b mod p, and they swap A and B over the network. Then Alice computes B^a mod p and Bob A^b mod p. Are they equal? And how many milliseconds does the whole exchange take?](figure.svg)

## Goal

Do one Diffie-Hellman exchange with the real 2048-bit group, check that both sides get the same secret, and see how long it takes.

## Ready for you

- `dh.py`: `P`, the 2048-bit prime, and `G = 2`.
- `dh.py`: the timer around your code: `start = time.perf_counter()` before it, the time in ms printed after it.

## Steps

Write your code in place of the `TODO` comments in `dh.py`:

1. Alice's secret `a` and Bob's secret `b`: random 256-bit numbers, `secrets.randbits(256)`.
2. `A = G^a mod P` (Alice sends it) and `B = G^b mod P` (Bob sends it). In Python `pow(G, a, P)` computes `G^a mod P` quickly, even for huge numbers. Python integers have no size limit: there is no overflow as with `int` in C.
3. Alice computes `B^a mod P`, Bob computes `A^b mod P`.
4. Print whether both results are equal, `print("equal:", ...)`, and the first 20 digits of the secret, `print("secret:", str(x)[:20], "...")`. `str(x)[:20]` gives the first 20 digits of `x` (a slice: the characters 0 to 19).

## Expected output

`True`, then 20 digits, then the time. The digits are new on every run (the secrets are random), and your time will be different, but it should be a few milliseconds.

<details>
<summary>Check your answer</summary>

```
equal: True
secret: 17703899368065106010 ...
took 12.2 ms
```

</details>

## Run

```
python3 dh.py
```

About 6 minutes. Python 3, no extra libraries.

Want to see it with small numbers? In the [Diffie-Hellman black box](https://ksawerym.github.io/Cryptography-simulators/diffie-hellman/#1), change a, b, p or g and watch both secrets change together.
