# Task 1: decrypt a message

You received a ciphertext and you know the keystream. Decrypt the message.

Fill in the `TODO` in `decrypt.py`. XOR each ciphertext byte with its keystream byte (`c ^ z`). Each result is an ASCII code: `chr(72)` gives `H`.

## Run

```
python3 decrypt.py
```

Python 3, no extra libraries.
