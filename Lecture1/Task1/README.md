# Task 1: decrypt a message

You received a ciphertext. You and the sender share a one-time pad: random bytes, as many as the message has. Decrypt the message.

Fill in the `TODO` in `decrypt.py`. XOR each ciphertext byte with its pad byte (`c ^ p`). Each result is an ASCII code: `chr(72)` gives `H`.

## Run

```
python3 decrypt.py
```

Python 3, no extra libraries.
