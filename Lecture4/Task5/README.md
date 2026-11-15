# Task 5: ElGamal in Python

## The situation

Bob has published his ElGamal public key y = g^x mod p, in the real 2048-bit group. Alice wants to send him a message. For every message she picks a new random secret k and sends a pair: C1 = g^k mod p (her half of a Diffie-Hellman exchange) and C2 = M · y^k mod p (the message, hidden by the shared value). Bob computes the same shared value from C1 with his private key x and divides it out.

![Bob's keys, both ready in elgamal.py, 617 digits each: the public key y = g^x mod p = 19681741201639... and the private key x = 30211086908663...; p and g = 2 come from RFC 3526. Alice's message "Meet me at the old bridge at noon." becomes a 271-bit number M with text_to_number. M, Bob's public key y and a new random k go into encrypt(M, y) (TODO), which gives the pair (C1, C2). The pair and Bob's private key x go into decrypt(C1, C2, x) (TODO): do we get M again? Below, the same M is encrypted again into (C1', C2'): is C1 equal to C1'?](figure.svg)

## Goal

Write `encrypt` and `decrypt` of ElGamal, then check that the message comes back and that the same message encrypted twice gives two different ciphertexts.

## Ready for you

- `elgamal.py`: `P` (2048 bits) and `G = 2`, Bob's private key `x` and public key `y`.
- `elgamal.py`: `text_to_number(text)` and `number_to_text(number)` turn text into a number and back.
- `elgamal.py`: the code at the end, which encrypts the message, decrypts it, encrypts it once more and compares the two C1.

## Steps

Write your code in place of the `TODO` comments in `elgamal.py`:

1. `encrypt(M, y)`: pick a random k, `secrets.randbelow(P - 2) + 1`, and return the pair `(C1, C2)` with `C1 = G^k mod P` and `C2 = M * y^k mod P`. `return a, b` returns two values at once (a tuple), like a small struct in C.
2. `decrypt(C1, C2, x)`: `s = C1^x mod P`, then return `M = C2 * (inverse of s) mod P`. `pow(s, -1, P)` gives the inverse.

## Expected output

The first digits of C1 and C2 (new on every run, because k is random), then the message, then whether the same message gives the same C1 twice.

<details>
<summary>Check your answer</summary>

```
C1 = 705046884062151247803948219803 ...
C2 = 154515346338198761448162095481 ...
decrypted: Meet me at the old bridge at noon.
the same message again gives the same C1: False
```

Your C1 and C2 will be different. The last line is `False` on every run: a new k gives a new ciphertext.

</details>

## Run

```
python3 elgamal.py
```

About 8 minutes. Python 3.8 or newer (for `pow(s, -1, P)`), no extra libraries.

Want to see it with small numbers? The [ElGamal step](https://ksawerym.github.io/Cryptography-simulators/diffie-hellman/#4) encrypts and decrypts the example of the slides.
