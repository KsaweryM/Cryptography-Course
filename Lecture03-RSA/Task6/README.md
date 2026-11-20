# Task 6: guess the PIN

## The situation

A bank encrypts the customers' 4-digit PINs with **textbook RSA**, C = PIN<sup>e</sup> mod n, and a strong 2048-bit key. Eve intercepted one encrypted PIN. She does not have the bank's private key, and nobody can factor a 2048-bit n. But she has the bank's **public key**, like everybody else.

![A customer's PIN, four question marks, a 4-digit PIN, is encrypted with textbook RSA, C = PIN to the power e mod n, with the bank's public key (e = 65537, n starting 18728411951178, 2048 bits). The ciphertext C, starting 73320723855296, goes to the bank, which keeps the private key d secret. Eve listens. Eve has the public key and the encrypted PIN C, but not the private key d.](figure.svg)

## Goal

Find the PIN without the private key.

## Ready for you

- `pin.py`: the bank's public key `e`, `n` (2048 bits), the encrypted PIN `C`, and the time measurement around your code.

## Steps

Write your code in place of the `TODO` comment in `pin.py`:

1. Find the PIN without the private key and store it in `pin`. Until then the file prints `not found yet`.

<details>
<summary>Hint</summary>

The public key is public, so you can encrypt any number yourself with `pow(number, e, n)`.

</details>

## Expected output

The PIN and the time it took. Your time will be different, but it is under a second.

<details>
<summary>Check your answer</summary>

```
PIN: 4821    found in 0.40 s
```

Textbook RSA always gives the same ciphertext for the same message, and there are only 10 000 PINs: Eve encrypts every one of them and compares with C. A bigger key does not help.

After you finish: in [Textbook RSA is not enough, part 3](https://ksawerym.github.io/Cryptography-simulators/rsa/#5.3), Eve guesses and checks on a small key and on the 2048-bit key of this task.

</details>

## Run

```
python3 pin.py
```

About 7 minutes. Python 3, no extra libraries.
