# Task 5: forge it

## The situation

Alice's bank takes a payment order as one number, the amount in pounds, signed with textbook RSA: the bank accepts a signature `s` for the amount `m` when `s^e mod n == m`. Alice paid Mallory twice, 20 and 50 pounds, so Mallory has two orders that Alice signed. Mallory does not have Alice's private key `d`. She wants the bank to pay her 1000 pounds.

![Alice signed 20 pounds (signature 80a9b014e367...069ba6863a16) and 50 pounds (signature c95f1a1e8b14...5617ecb95454). Mallory computes sig_1 x sig_2 mod n and offers it for 1000 pounds: bank = ? She also takes any number, 123 456 789, as a signature: amount = ?, bank = ?. The bank accepts s if s^e mod n = amount.](figure.svg)

## Goal

Without the private key, make the bank accept an order for 1000 pounds, and make one more valid signature from a number of your choice.

## Ready for you

- `bank_ready.py`: Alice's public key `n`, `e`; the two orders `amount_1`, `sig_1` and `amount_2`, `sig_2`; `short(x)` for printing.
- `pow(x, e, n)` and the operators `*` and `%` on big integers.

## Steps

Write your code in place of the `None` after each `TODO` in `forge.py`:

1. Check both orders as the bank does: `pow(sig_1, e, n) == amount_1`, and the same for order 2.
2. From `sig_1` and `sig_2` alone, make one signature that the bank accepts on `amount_1 * amount_2`, and check it.
3. Take `any_sig = 123456789`, compute the amount it signs with the **public** key, and check it as the bank does.

<details>
<summary>Hint for step 2</summary>

Multiply the two signatures modulo `n`: `forged = sig_1 * sig_2 % n`. Why it works (slide "Problem 2: signatures multiply"): (m1^d)(m2^d) = (m1 m2)^d mod n.

</details>

## Expected output

<details>
<summary>Check your answer</summary>

```
order 1: 20 pounds, signature 80a9b014e367...069ba6863a16 (512 hex digits)
order 2: 50 pounds, signature c95f1a1e8b14...5617ecb95454 (512 hex digits)
the bank checks order 1: True  order 2: True
forged signature: 13bf50ca7f3a...619b651031c3 (511 hex digits)
the bank checks it on 1000 pounds: True
any signature: 123456789  signs the amount 4383e8aad872...581a62c032b0 (512 hex digits)
the bank checks it: True
```

Two signatures and one multiplication give a valid signature on 1000 pounds. Any number is a valid signature of some amount, only Mallory cannot choose which.

</details>

## Run

```
python3 forge.py
```

About 9 minutes. Python 3 and the library `cryptography` (only `bank_ready.py` uses it, to read the PEM file).
