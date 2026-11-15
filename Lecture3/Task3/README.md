# Task 3: factor it

Goal: factor four numbers (32, 40, 48 and 55 bits) and time each one.

Each number in `factor.py` is a product of two primes, as in RSA.
The numbers and the time measurement are ready in the file.

Predict first: each number is 8 bits longer than the one before. How many times longer will it take?

Fill in the `TODO` in `factor.py`:

1. Write `smallest_factor(n)` by trial division: try the divisors 2, 3, 5, 7, 9, ... (2, then odd numbers)
   until one divides n (`n % f == 0`), and return it.
   You only need to try f while `f * f <= n`. Why?

The program prints the factors and the time for each number. The last number takes several seconds.

## Run

```
python3 factor.py
```

Python 3, no extra libraries.

## Expected output

```
32 bits: 3215484683 = 50119 x 64157   0.003 s
40 bits: 731738952551 = 737039 x 992809   0.047 s
48 bits: 175092413211607 = 12100201 x 14470207   0.775 s
55 bits: 32013612409104631 = 162019679 x 197590889   10.113 s
```

Your times will be different. Every 8 more bits make factoring about 16 times slower.
