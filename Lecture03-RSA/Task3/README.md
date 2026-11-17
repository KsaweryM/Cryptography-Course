# Task 3: factor it

## The situation

An RSA public key contains a number n = p × q, where p and q are two secret primes. Whoever finds p and q can compute the private key. `factor.py` holds four such numbers, from 32 to 55 bits: each one is 8 bits longer than the one before. How long does it take to break them apart?

![factor.py: four numbers, each one a prime times a prime, as an RSA n: 3215484683 (32 bits), 731738952551 (40 bits), 175092413211607 (48 bits) and 32013612409104631 (55 bits). Both factors and the time are question marks; each number is 8 bits longer than the one before, how many times slower? Below, trial division: try f = 2, 3, 5, 7, 9, 11 and so on until n % f == 0, and stop at the square root of n (f * f <= n). Why is that enough?](figure.svg)

## Goal

Factor the four numbers and time each one.

**Predict first:** each number is 8 bits longer than the one before. How many times longer will it take?

## Ready for you

- `factor.py`: the four numbers in `NUMBERS`, and the loop that calls `smallest_factor(n)`, measures the time and prints the result.

## Steps

Write your code in place of the `TODO` comment in `factor.py`:

1. Write `smallest_factor(n)` by **trial division**: try the divisors 2, 3, 5, 7, 9, ... (2, then the odd numbers) until one divides n (`n % f == 0`), and return it.
   - You only need to try f while `f * f <= n`. Why?
   - In C you would write `for (f = 3; f * f <= n; f += 2)`; in Python use a `while` loop with `f += 2`.

## Expected output

Four lines: each number, its two factors and the time. The last number takes several seconds. Your times will be different, but each line should take roughly 16 times longer than the one before.

<details>
<summary>Check your answer</summary>

```
32 bits: 3215484683 = 50119 x 64157   0.003 s
40 bits: 731738952551 = 737039 x 992809   0.047 s
48 bits: 175092413211607 = 12100201 x 14470207   0.775 s
55 bits: 32013612409104631 = 162019679 x 197590889   10.113 s
```

8 more bits in n make each factor about 4 bits longer, so there are about 2⁴ = 16 times more divisors to try. A 2048-bit n has factors of 1024 bits: trial division would never finish.

</details>

## Run

```
python3 factor.py
```

About 7 minutes. Python 3, no extra libraries.

Want to see it move? In [How long for a bigger n?](https://ksawerym.github.io/Cryptography-simulators/rsa/#4.2), your browser makes a random n = p × q of the size you pick and factors it by trial division: make n bigger and watch the time grow.
