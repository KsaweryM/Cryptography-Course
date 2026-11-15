# Task 1: use ChaCha20

Goal: decrypt a message from RFC 8439 with one call to ChaCha20.

`chacha.py` is ready: treat it as a black box. It gives one function:
`chacha20(key, nonce, counter, data)`. The same call encrypts and decrypts.

The key, the nonce and the ciphertext are the example from RFC 8439, section 2.4.2.
They are already in `use_chacha.py`.

Fill in the `TODO`s in `use_chacha.py`:

1. Decrypt the ciphertext with counter 1.
2. Print the message (`plaintext.decode()` turns the bytes into text).

## Run

```
python3 use_chacha.py
```

Python 3, no extra libraries.

## Expected output

```
Ladies and Gentlemen of the class of '99: If I could offer you only one tip for the future, sunscreen would be it.
```
