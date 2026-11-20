# Task 8: two routers

## The situation

Two routers of the same make each made their own 2048-bit RSA key when they were first switched on. To make a key, a device picks two random primes p and q. But just after switching on, these routers had almost no randomness, so their random generators may have given the **same p** twice. Their public keys are public, as always. **Eve** also caught a message to router 1, encrypted with its public key. Nobody can factor a 2048-bit n. Does Eve need to?

![Two routers, router 1 with the public key e = 65537, n1 starting 17711018021637, and router 2 with e = 65537, n2 starting 16742917297534, 2048 bits each. Above them, a weak random generator, maybe the same p twice? Below, Eve has the ciphertext C to router 1, starting 12999080852746, and asks: gcd(n1, n2) = ?, then q, phi, d and the message = ?](figure.svg)

## Goal

Read the message to router 1 without factoring anything.

**Predict first:** n1 and n2 have 617 digits. How long does it take to find their greatest common divisor?

## Ready for you

- `routers.py`: the two public keys (`e`, `n1`, `n2`), the ciphertext `C` to router 1, the function `to_text(number)` (the number as bytes, then as text, like `rsa_ready.py` in Task 2) and the time measurement.

## Steps

Write your code in place of the `None` after each `TODO` in `routers.py`. The `print` lines are ready: they say `not done yet` until each TODO is done.

1. TODO 1: `p = math.gcd(n1, n2)`, the greatest common divisor (slide "Greatest common divisor"). If it is bigger than 1, it is a prime that both keys share.
2. TODO 2: `q = n1 // p` (`//` is integer division, as `/` on integers in C).
3. TODO 3: router 1's private exponent, as on the slides "Making the keys": `phi = (p - 1) * (q - 1)`, then `d = pow(e, -1, phi)`.
4. TODO 4: `message = to_text(pow(C, d, n1))`.

## Expected output

The start of p and its number of digits, a check that p × q = n1, the message and the time.

<details>
<summary>Check your answer</summary>

```
p = 16870771331706619329 ... 309 digits; p > 1: True
p * q == n1: True
router 1 reads: router 1 admin password: blue-otter-42
all of it took 24.7 ms
```

Your time will be different, but it is a few milliseconds: almost all of it is the one power with d; `math.gcd` alone takes about 14 microseconds. Euclid's algorithm needs only about 1200 divisions even for 617-digit numbers, so the shared p falls out at once, and with it both keys. This really happened: in 2012, two research teams collected millions of public keys from the internet and broke tens of thousands of them this way, mostly keys of routers and firewalls.

</details>

## Run

```
python3 routers.py
```

About 6 minutes. Python 3.8 or newer (for `pow(e, -1, phi)`), no extra libraries.
