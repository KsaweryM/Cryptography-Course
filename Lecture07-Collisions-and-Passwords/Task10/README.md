# Task 10: a hash that needs memory

## The situation

bcrypt makes every guess cost **time**. scrypt also makes it cost **memory**: it first fills a large table, then reads it in an order that depends on the password. Bob's server can spare 32 MiB for one login; Mallory, who wants thousands of guesses at once on a graphics card, has to give every guess its own 32 MiB.

![Part 1: the password "violet kettle 1987" and a salt go into scrypt; four boxes n = 2^12 to 2^15, each with "? s, ? MiB". Part 2: a device with 16 MiB: n = 2^15, done or refused? Part 3: one graphics card with 24 GiB and 16 384 cores: how many bcrypt guesses (4 KiB each) and how many scrypt guesses (32 MiB each) fit at once?](figure.svg)

## Goal

Measure how the time and the memory of scrypt grow with its parameter n, see that scrypt refuses to run without its memory, and count what this means for a graphics card.

## Ready for you

- `hashlib.scrypt(password, salt=salt, n=n, r=8, p=1, maxmem=limit, dklen=32)` is in the Python standard library (it calls OpenSSL, C code). It uses 128 · r · n bytes of memory; `maxmem` is the most it may take, and if it needs more it raises `ValueError`.
- `memory_hard.py`: the password, the salt and `MIB = 1024 * 1024`.
- `try: ... except ValueError: ...` works like checking an error code in C: the code after `except` runs only if the call failed.

Before you run it, predict: when n doubles, what happens to the time and to the memory?

## Steps

Write your code in `memory_hard.py`, in place of the `TODO` comments:

1. For `k` in 12 to 15: `n = 2 ** k`. Call scrypt three times, keep the shortest time, compute the memory `128 * 8 * n` and print it as in the comment.
2. Call scrypt with `n = 2 ** 15` and `maxmem = 16 * MIB` inside `try`; print whether it was done or refused.
3. A graphics card with 24 GiB and 16 384 cores: divide its memory by 4 KiB (bcrypt) and by 32 MiB (scrypt, n = 2^15). Print both counts.

## Expected output

Your times will differ; the doubling will be similar.

<details>
<summary>Check your answer</summary>

```
n = 2^12: 0.012 s, 4 MiB
n = 2^13: 0.021 s, 8 MiB
n = 2^14: 0.041 s, 16 MiB
n = 2^15: 0.088 s, 32 MiB
n = 2^15 with at most 16 MiB: refused
bcrypt: 6291456 guesses fit at once
scrypt n = 2^15: 768 guesses fit at once, for 16384 cores
```

(Intel i5-8265U, Python 3.12.) Doubling n doubles the time **and** the memory. With bcrypt, memory never limits a graphics card: millions of guesses fit. With scrypt at n = 2^15 only 768 guesses fit at once, so about 95% of the 16 384 cores have nothing to do. Recomputing the table instead of storing it costs far more time: memory cannot be traded away cheaply.

</details>

## Run

```
python3 memory_hard.py
```

About 8 minutes. Python 3.8 or newer with OpenSSL (the usual builds), no extra libraries; the program runs under a second.
