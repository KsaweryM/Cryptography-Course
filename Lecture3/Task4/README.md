# Task 4: your own RSA

## The situation

On the slides, Bob made his keys in five steps from p = 17 and q = 11. Now you make your own key the same way, from two primes with about 20 digits each (small enough that the result fits on the screen; real keys have about 309 digits per prime). Then you use it: encrypt the number 2026 with the public key and decrypt it with the private key.

![my_rsa.py gives p = 37908704904578413183 and q = 58606630333925820283 (secret) and e = 65537 (public). Steps 1 to 3: n = p times q (public), phi = (p - 1)(q - 1) (secret), d = the inverse of e mod phi (secret), all question marks. Step 4: the message 2026 goes through C = message to the power e mod n with the public key {e, n}, giving C = ?. Step 5: P = C to the power d mod n with the private key {d, n}, giving P = ?, which must be 2026.](figure.svg)

## Goal

Make your own RSA key from two primes, then encrypt and decrypt the number 2026.

## Ready for you

- `my_rsa.py`: the two primes `p` and `q`, the public exponent `e = 65537` and `message = 2026`.

## Steps

Write your code in place of the `TODO` comments in `my_rsa.py`:

1. `n = p * q`
2. `phi = (p - 1) * (q - 1)`
3. `d`, the inverse of e mod phi: in Python `pow(e, -1, phi)`.
4. C = message<sup>e</sup> mod n: in Python `pow(message, e, n)`.
5. P = C<sup>d</sup> mod n, the same way with `d`.

Then print n, d, C and P: `print("n =", n)` and so on. Python integers have no size limit, so 40-digit numbers need no special type (unlike `long` in C).

## Expected output

Four lines. n has 40 digits; d and C look like random 40-digit numbers; P must be the original message.

<details>
<summary>Check your answer</summary>

```
n = 2221701454780507748530735154427775990789
d = 1367151349159148221410861819858768950381
C = 736246060401132335090489988934276767570
P = 2026
```

</details>

## Run

```
python3 my_rsa.py
```

About 8 minutes. Python 3.8 or newer (for `pow(e, -1, phi)`), no extra libraries.

Want to see it move? In [Making the keys](https://ksawerym.github.io/Cryptography-simulators/rsa/#2), the same five steps with your own primes, and how the extended Euclidean algorithm finds d.
