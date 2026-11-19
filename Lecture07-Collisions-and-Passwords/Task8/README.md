# Task 8: what the cost costs

## The situation

bcrypt has a **cost**: one bcrypt does 2^cost rounds of its slow key setup, so every +1 should double the time. Part 1: measure it. Part 2: Mallory has stolen Dave's bcrypt text (cost 4, `stolen_bcrypt.txt`) from a shop's database and tries the 20 most common passwords (`top20.txt`). How fast can she guess, compared with plain SHA-256?

![Part 1: four boxes cost 4, cost 5, cost 6, cost 7, each with a stopwatch and "? s". Part 2: Mallory with top20.txt (123456, password, ...) going into check_password together with the stolen text $2b$04$Bm9vfEMu3JI4IV.ybN/ip.o0s/IPx...; found after ? tries, bcrypt: ? guesses/s, SHA-256: ? guesses/s.](figure.svg)

## Goal

See how the time of bcrypt grows with the cost, crack a weak password behind bcrypt, and compare Mallory's speed with SHA-256.

## Ready for you

- `bcrypt_ready.py` (you do not need to read it): `hash_password(password, cost)` and `check_password(password, stored)`; pure Python, about 100 times slower than C, so all numbers are smaller than on a real server, but the proportions are the same.
- `slow_hash.py`: `load_lines(path)` reads a text file without the comment lines; `stored` and `guesses` are loaded for you.
- `time.perf_counter()` returns seconds as a float, like `clock_gettime` in C: take it before and after, and subtract.

Before you run it, predict: how many guesses per second against bcrypt, compared with SHA-256?

## Steps

Write your code in `slow_hash.py`, in place of the `TODO` comments:

1. For `cost` in 4, 5, 6, 7 (`range(4, 8)`): measure one `hash_password("test password", cost)` and print `f"cost {cost}: {seconds:.2f} s"`.
2. Try the guesses in order with `check_password(guess, stored)`, counting the tries. When one matches, print `f"found after {tries} tries: {guess}"` and `break`. Measure the whole loop and print the guesses per second as in the comment.
3. Measure SHA-256 on the same 20 guesses, 10 000 times over (200 000 hashes), and print the guesses per second as in the comment.

## Expected output

Your times will differ (they depend on the computer), but the doubling and the gap between bcrypt and SHA-256 will be similar. The whole program runs 10 to 30 seconds, depending on the computer.

<details>
<summary>Check your answer</summary>

```
cost 4: 0.22 s
cost 5: 0.42 s
cost 6: 0.82 s
cost 7: 1.69 s
stolen: $2b$04$Bm9vfEMu3JI4IV.ybN/ip.o0s/IPxPkzhcVSMvbHjN0qqn0.Cm3Lu
found after 20 tries: sunshine
bcrypt cost 4: 4.4 guesses per second
SHA-256: 690705 guesses per second
```

(Intel i5-8265U, Python 3.12.) A weak password falls even behind bcrypt, but every guess costs as much as about 150 000 SHA-256 guesses, and real servers use cost 10 to 12, which is 64 to 256 times slower again.

</details>

## Run

```
python3 slow_hash.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries.
