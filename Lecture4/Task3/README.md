# Task 3: find a

## The situation

Eve saw p, g and Alice's public value A = g^a mod p. To get the shared secret she needs Alice's secret a: the **discrete logarithm** of A. She has no better idea than trying a = 1, 2, 3, ... until g^a mod p is A. You are Eve, on four small problems: p has 16, 20, 24 and 28 bits.

![The four problems in dlog.py, all with g = 4: 16 bits, p = 49 223, A = 38 043; 20 bits, p = 939 167, A = 532 807; 24 bits, p = 10 684 799, A = 3 257 080; 28 bits, p = 187 882 979, A = 180 535 483. For each, a and the time are unknown. Below, Eve's search on the 16-bit problem: for a = 1 to 8 the value 4^a mod 49 223 is 4, 16, 64, 256, 1024, 4096, 16384, 16313, each one the previous one times 4 mod p, and none of them is A. She goes on until the value is 38 043, then returns a.](figure.svg)

## Goal

Find the secret a of each problem by trying a = 1, 2, 3, ..., and see how the time grows with the size of p.

**Predict first:** each p is 4 bits longer than the one before. How many times longer will the search take?

## Ready for you

- `dlog.py`: `PROBLEMS`, the four problems, each a tuple `(p, g, A)`.
- `dlog.py`: the loop that calls your `find_exponent(p, g, A)` for each problem and prints the number of bits, `a` and the time.

## Steps

Write your code in place of the `TODO` comment in `dlog.py`, in `find_exponent(p, g, A)`:

1. Try a = 1, 2, 3, ...: keep `value = g^a mod p`. Do not call `pow` again for every a: multiply the previous value by g, mod p (`value = value * g % p`). When `value == A`, return a.

## Expected output

Four lines. The time grows fast: the last one takes several seconds. Your times will be different (they depend on the computer and on its load), but compare them with your prediction.

<details>
<summary>Check your answer</summary>

```
16 bits: a = 17773   0.003 s
20 bits: a = 415826   0.056 s
24 bits: a = 3465539   0.487 s
28 bits: a = 60546499   8.548 s
```

Every 4 more bits make the search about 16 times longer (2^4 = 16). The jumps are not exactly equal, because a is a different size in each problem.

</details>

## Run

```
python3 dlog.py
```

About 6 minutes. Python 3, no extra libraries.
