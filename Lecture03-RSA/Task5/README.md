# Task 5: your own RSA

## The situation

On the slides, Bob made his keys in five steps from p = 17 and q = 11. Now you build a key the same way from two given primes with about 20 digits each (small enough that the result fits on the screen; real keys have about 309 digits per prime). Then you use it: encrypt the number 2026 with the public key and decrypt it with the private key.

![my_rsa.py gives p = 37908704904578413183 and q = 58606630333925820283 (secret) and e = 65537 (public). TODO 1 to 3: n = p times q (public), phi = (p - 1)(q - 1) (secret), d = the inverse of e mod phi (secret), all question marks. TODO 4: the message 2026 goes through C = message to the power e mod n with the public key {e, n}, giving C = ?. TODO 5: P = C to the power d mod n with the private key {d, n}, giving P = ?, which must be 2026.](figure.svg)

## Goal

Build an RSA key from two given primes, then encrypt and decrypt the number 2026.

## Ready for you

- `my_rsa.py`: the two primes `p` and `q`, the public exponent `e = 65537` and `message = 2026`.

## Steps

Write your code in place of the `None` after each `TODO` in `my_rsa.py`. The `print` lines at the end are ready: they say `not done yet` until every TODO is done. The formulas are the ones on the slides "Making the keys" and "Encrypt and decrypt"; the Python functions you need were on the slides "Powers modulo n" and "The modular inverse".

1. TODO 1: n = p × q
2. TODO 2: phi = (p - 1) × (q - 1)
3. TODO 3: d = the inverse of e mod phi
4. TODO 4: C = message<sup>e</sup> mod n (encrypt with the public key {e, n})
5. TODO 5: P = C<sup>d</sup> mod n (decrypt with the private key {d, n})
6. Set `e = 3` at the top of the file and run again. What does Python say, and why? Then set `e = 65537` back.

Python integers have no size limit, so 40-digit numbers need no special type (unlike `long` in C).

## Expected output

Four lines. n has 40 digits; d and C look like random 40-digit numbers; P must be the original message. For step 6, note what Python says.

<details>
<summary>Check your answer</summary>

```
n = 2221701454780507748530735154427775990789
d = 1367151349159148221410861819858768950381
C = 736246060401132335090489988934276767570
P = 2026
```

Step 6, with `e = 3`, TODO 3 stops the program:

```
ValueError: base is not invertible for the given modulus
```

d exists only if gcd(e, phi) = 1 (step 4 on the slides "Making the keys"). For these two primes gcd(3, phi) = 3: both p - 1 and q - 1 are multiples of 3, so 3 × d mod phi is always a multiple of 3 and never 1. That is why step 4 chooses e with gcd(e, phi) = 1; 65537 passes this test for these primes.

</details>

## Run

```
python3 my_rsa.py
```

About 8 minutes. Python 3.8 or newer (for the modular inverse with `pow`), no extra libraries.

Want to see it move? In [Making the keys](https://ksawerym.github.io/Cryptography-simulators/rsa/#2), the same five steps with your own primes, and how the extended Euclidean algorithm finds d.
