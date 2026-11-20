# Task 7: double the transfer

## The situation

Alice tells her bank to transfer 100 to Bob. She encrypts the amount with the bank's **public key**, with **textbook RSA**: C = amount<sup>e</sup> mod n. **Mallory** sits on the network between Alice and the bank. She cannot read C and has no private key, but she can **change** C before it reaches the bank. Can she change the amount the bank reads?

![Alice's order "transfer 100 to Bob" is encrypted with textbook RSA, C = amount to the power e mod n, with the bank's public key (e = 65537, n starting 18811042465118, 2048 bits). The ciphertext C, starting 18726317804580, goes over the network to the bank. On the way Mallory, who has no private key, only the public key, turns it into C2 = C times ? mod n. The bank decrypts C2 with its secret private key d: bank_decrypt(C2) = ?](figure.svg)

## Goal

Without the private key, make the bank read 2 times, then 100 times Alice's amount.

**Predict first:** C is a number with 617 digits. If Mallory multiplies it by something, will the bank read nonsense?

## Ready for you

- `double.py`: the bank's public key `e`, `n` (2048 bits) and Alice's ciphertext `C`. It already prints what the bank reads from `C`: 100.
- `bank.py`: the bank, with `bank_decrypt(C)`, which decrypts with the private key and returns the amount. You do not need to read it; Mallory cannot see inside the bank, so do not use `D` from it.

## Steps

Write your code in place of the `None` after each `TODO` in `double.py`. The `print` lines are ready: each one says `not done yet` until its TODO is done.

1. TODO 1: `C2`, a ciphertext the bank reads as 2 times the amount. Encrypt the number 2 with the public key, `pow(2, e, n)`, and multiply it into C: `(C * ...) % n`.
2. TODO 2: `C100`, a ciphertext the bank reads as 100 times the amount. The same with 100.

<details>
<summary>Hint: why does it work?</summary>

(2<sup>e</sup>) × (P<sup>e</sup>) = (2 × P)<sup>e</sup>, also modulo n. So C × 2<sup>e</sup> mod n is the ciphertext of 2 × P, and the bank's private key opens it like any other ciphertext.

</details>

## Expected output

Three lines: what the bank reads from Alice's C, from C2 and from C100.

<details>
<summary>Check your answer</summary>

```
the bank reads Alice's C: 100
the bank reads C2:      200
the bank reads C100:    10000
```

Mallory never saw the amount and never had d, yet she chose what the bank reads: multiplying the ciphertexts multiplies the messages. Textbook RSA does not protect a message against change. The random padding of real RSA (OAEP) breaks this: a multiplied ciphertext no longer has a valid padding, and the bank rejects it.

After you finish: in [Textbook RSA is not enough, part 6](https://ksawerym.github.io/Cryptography-simulators/rsa/#5.6), the same trick on another key, with your own multiplier.

</details>

## Run

```
python3 double.py
```

About 5 minutes. Python 3, no extra libraries.
