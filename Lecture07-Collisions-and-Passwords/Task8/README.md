# Task 8: what the cost costs

## The situation

bcrypt has a **cost**: one bcrypt does 2^cost rounds of its slow key setup (each round has two key setups), so every +1 should double the time. Part 1: measure it. Part 2: Mallory has stolen Dave's bcrypt text (cost 4, `stolen_bcrypt.txt`) from a shop's database and tries the 20 most common passwords (`top20.txt`). How fast can she guess, compared with plain SHA-256? Part 3: compare fairly, with SHA-256 written in the same plain Python.

![Part 1: four boxes cost 4, cost 5, cost 6, cost 7, each with a stopwatch and "? s". Part 2: Mallory with top20.txt (123456, password, ...) going into check_password together with the stolen text $2b$04$Bm9vfEMu3JI4IV.ybN/ip.o0s/IPx...; found after ? tries, bcrypt: ? guesses/s, SHA-256: ? guesses/s.](figure.svg)

## Goal

See how the time of bcrypt grows with the cost, crack a weak password behind bcrypt, and compare Mallory's speed with SHA-256.

## Ready for you

- `bcrypt_ready.py` (you do not need to read it): `hash_password(password, cost)` and `check_password(password, stored)`; pure Python, about 100 times slower than the C code of a real server.
- `sha256_ready.py` (you do not need to read it): `sha256(data)`, SHA-256 in the same plain Python. Why not `hashlib.sha256`? It is C code, more than 100 times faster than this file, so bcrypt in Python against hashlib would compare two languages, not two hashes.
- `slow_hash.py`: `load_lines(path)` reads a text file without the comment lines; `stored` and `guesses` are loaded for you.
- `time.perf_counter()` returns seconds as a float, like `clock_gettime` in C: take it before and after, and subtract.

Before you run it, predict: how many guesses per second against bcrypt, compared with SHA-256?

## Steps

Write your code in `slow_hash.py`, in place of the `TODO` comments:

1. For `cost` in 4, 5, 6, 7 (`range(4, 8)`): measure one `hash_password("test password", cost)` and print `f"cost {cost}: {seconds:.2f} s"`.
2. Try the guesses in order with `check_password(guess, stored)`, counting the tries. When one matches, print `f"found after {tries} tries: {guess}"` and `break`. Measure the whole loop and print the guesses per second as in the comment.
3. Measure `sha256(guess.encode())` from `sha256_ready.py` on the same 20 guesses, 100 times over (2 000 hashes), and print the guesses per second as in the comment.
4. Divide the two speeds: how many SHA-256 guesses does Mallory make in the time of one bcrypt guess? Print it as in the comment.

## Expected output

Your times will differ (they depend on the computer), but the doubling and the ratio of part 3 will be similar. The whole program runs 5 to 20 seconds, depending on the computer.

<details>
<summary>Check your answer</summary>

```
cost 4: 0.13 s
cost 5: 0.26 s
cost 6: 0.53 s
cost 7: 1.07 s
stolen: $2b$04$Bm9vfEMu3JI4IV.ybN/ip.o0s/IPxPkzhcVSMvbHjN0qqn0.Cm3Lu
found after 20 tries: sunshine
bcrypt cost 4: 7.1 guesses per second
SHA-256, plain Python: 4580 guesses per second
one bcrypt guess = 646 SHA-256 guesses
```

(Intel i5-8265U, Python 3.12; other runs gave 560 to 690.) A weak password falls even behind bcrypt, but every guess at cost 4 costs as much as several hundred SHA-256 guesses, and real servers use cost 10 to 12, which is 64 to 256 times more again. In C on the same laptop the ratio at cost 4 is about 5 200 (bcrypt 1 100 per second, SHA-256 5.7 million per second), and on a graphics card it is bigger still: the lecture shows why.

</details>

## Run

```
python3 slow_hash.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? The simulator puts bcrypt next to SHA-256 in your browser, both in the same JavaScript: [passwords, step 3.2](https://ksawerym.github.io/Cryptography-simulators/passwords/#3.2).
