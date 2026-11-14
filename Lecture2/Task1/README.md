# Task 1: use ChaCha20

`chacha.py` is ready: treat it as a black box. It gives one function:
`chacha20(key, nonce, counter, data)`. The same call encrypts and decrypts.

The key, the nonce and the ciphertext are the example from RFC 8439, section 2.4.2.

Fill in the `TODO`s in `use_chacha.py`:

1. Decrypt the ciphertext with counter 1.
2. Print the message (`plaintext.decode()` turns the bytes into text).

## Run

```
python3 use_chacha.py
```

Python 3, no extra libraries.
