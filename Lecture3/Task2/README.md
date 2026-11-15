# Task 2: use RSA

Goal: you are Bob. Decrypt Alice's message, then encrypt a reply for her.

RSA is the best known public-key cipher. Here you use it as a black box first.

`rsa_ready.py` is ready: treat it as a black box. It has two functions:

- `encrypt(text, public_key)` gives a number,
- `decrypt(number, private_key)` gives the text.

`use_rsa.py` holds your private key, Alice's public key and a message from Alice.
The keys have 2048 bits (numbers with about 617 digits): just pass them to the functions.

Fill in the `TODO`s in `use_rsa.py`:

1. Decrypt Alice's message with your private key and print it.
2. Encrypt the reply "Yes, at 5 pm." with Alice's public key.
   Print the first 30 digits of the result: `str(reply)[:30]`.
3. Try to decrypt your own reply with YOUR private key. What do you get, and why?

## Run

```
python3 use_rsa.py
```

Python 3, no extra libraries.

## Expected output

```
Alice says: Can we meet on Friday at the library?
reply:     148116905244108187548815493601 ...
my key on my reply: '\x06��Z���1Ű��d>(�\\lE��8\x1c�W�...
```

The last line is nonsense (the exact characters depend on your terminal): what is locked with Alice's public key, only Alice's private key opens.
