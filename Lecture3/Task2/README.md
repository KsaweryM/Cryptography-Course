# Task 2: use RSA

## The situation

You are Bob. Alice wants to meet you, so she took your **public key**, encrypted her message with it and sent you the result: one big number with 617 digits. Only your **private key** can open it. You want to answer her, and for that you need **her** public key. RSA is the best known public-key cipher; here you use it as a black box.

![Alice sends Bob a ciphertext over the internet, a number with 617 digits starting 10536221293020, locked with Bob's public key. Bob's reply "Yes, at 5 pm." goes back to Alice, to be locked with Alice's public key. Bob's file use_rsa.py holds his private key (d, n), secret, with d starting 23536257730787 (616 digits) and n starting 14228352761761 (617 digits), and Alice's public key (e, n), public, with e = 65537 and n starting 17535949526233. rsa_ready.py is a black box with encrypt(text, key) and decrypt(number, key).](figure.svg)

## Goal

Decrypt Alice's message, then encrypt a reply for her.

## Ready for you

- `rsa_ready.py`: a black box, you do not need to read it. Two functions:
  - `encrypt(text, public_key)` gives a number,
  - `decrypt(number, private_key)` gives the text.
- `use_rsa.py`: `my_private_key` (yours), `alice_public_key` and `ciphertext` from Alice. The keys have 2048 bits (numbers with about 617 digits): just pass them to the functions.

## Steps

Write your code in place of the `TODO` comments in `use_rsa.py`:

1. Decrypt `ciphertext` with your private key and print it.
2. Encrypt the reply `"Yes, at 5 pm."` with Alice's public key and print the first 30 digits of the result: `str(reply)[:30]` (`str` turns the number into text, `[:30]` keeps its first 30 characters).
3. Try to decrypt your own reply with **your** private key. What do you get, and why?

## Expected output

Alice's question, then the start of your reply as a number, then whatever your private key makes of your own reply.

<details>
<summary>Check your answer</summary>

```
Alice says: Can we meet on Friday at the library?
reply:     148116905244108187548815493601 ...
my key on my reply: '\x06��Z���1Ű��d>(�\\lE��8\x1c�W�...
```

The last line is nonsense (the exact characters depend on your terminal and on how much of it you print): what is locked with Alice's public key, only Alice's private key opens. Even Bob cannot read his own reply any more.

</details>

## Run

```
python3 use_rsa.py
```

About 6 minutes. Python 3, no extra libraries.

Want to see it move? In the [RSA black box](https://ksawerym.github.io/Cryptography-simulators/rsa/#1), Alice encrypts, Bob decrypts and Eve listens, step by step with small numbers.
