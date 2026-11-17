# Task 3: find a

## The situation

Eve saw p, g and Alice's public value A = g^a mod p. To get the shared secret she needs Alice's secret a: the **discrete logarithm** of A. She has no better idea than trying a = 1, 2, 3, ... until g^a mod p is A. You are Eve, on four small problems: p has 16, 20, 24 and 28 bits.

![The four problems in dlog.py, all with g = 4: 16 bits, p = 49 223, A = 38 043; 20 bits, p = 939 167, A = 532 807; 24 bits, p = 10 684 799, A = 3 257 080; 28 bits, p = 187 882 979, A = 180 535 483. For each, a and the time are unknown. Below, Eve's search on the 16-bit problem: for a = 1 to 8 the value 4^a mod 49 223 is 4, 16, 64, 256, 1024, 4096, 16384, 16313, each one the previous one times 4 mod p, and none of them is A. She goes on until the value is 38 043, then returns a.](figure.svg)

## Goal

Find the secret a of each problem by trying a = 1, 2, 3, ..., see how the time grows with the size of p, and use your own speed to estimate how long a real 256-bit secret would take.

**Predict first:** each p is 4 bits longer than the one before. How many times longer will the search take?

## Ready for you

- `dlog.py`: `PROBLEMS`, the four problems, each a tuple `(p, g, A)`. Here g = 4; any g with a long cycle works.
- `dlog.py`: the loop that calls your `find_exponent(p, g, A)` for each problem and prints the number of bits, `a` and the time. After the loop, `a` and `seconds` hold the result of the last (28-bit) problem.

## Steps

Write your code in place of the `TODO` comments in `dlog.py`:

1. In `find_exponent(p, g, A)`: try a = 1, 2, 3, ...: keep `value = g^a mod p`. Do not call `pow` again for every a: multiply the previous value by g, mod p (`value = value * g % p`). When `value == A`, return a.
2. After the loop: from 28 bits to 256 bits. For the last problem you tried `a` values in `seconds` seconds, so your speed is `tries_per_second = a / seconds`. A real secret a has 256 bits: trying them all is about 2^256 tries (`2**256` in Python; `**` is the power, there is no such operator in C). How many years is that at your speed? One year is `365 * 24 * 3600` seconds. Print it with `print(f"{tries_per_second:.0f} tries per second, a of 256 bits: about {years:.1e} years")`: `:.0f` prints a number with no digits after the point, `:.1e` like `%.1e` in C's `printf` (`3.5e+62` means 3.5 × 10^62).

## Expected output

Without your code every line says `not done yet`. With it: four lines, then your estimate. The time grows fast: the last search takes several seconds. The times below were measured on a laptop with an Intel Core i5-8265U; your times will differ (they depend on the computer and on its load), but compare them with your prediction.

<details>
<summary>Check your answer</summary>

```
16 bits: a = 17773   0.002 s
20 bits: a = 415826   0.035 s
24 bits: a = 3465539   0.336 s
28 bits: a = 60546499   5.836 s
10374805 tries per second, a of 256 bits: about 3.5e+62 years
```

Every 4 more bits make the search about 16 times longer (2^4 = 16). The jumps are not exactly equal, because a is a different size in each problem.

About 3.5 × 10^62 years: the universe is about 1.4 × 10^10 years old. Even a computer a million times faster would not get anywhere.

</details>

## Run

```
python3 dlog.py
```

About 8 minutes. Python 3, no extra libraries.
