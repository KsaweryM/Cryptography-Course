# Task 3: change one byte

`aead.py` is ready: treat it as a black box. It gives ChaCha20-Poly1305 as two functions:

- `seal(key, nonce, plaintext)` encrypts and returns the packet: the ciphertext and a 16-byte tag.
- `open_(key, nonce, packet)` checks the tag and returns the plaintext,
  or raises `ValueError` if the packet was changed.

Fill in the `TODO`s in `tamper.py`:

1. `packet = seal(key, nonce, b"Pay Bob 100")`
2. Flip one byte of the packet (for example XOR byte 5 with 1).
3. Try `open_(key, nonce, packet)` and print what happens
   (`try: ... except ValueError as e: print(e)`).

## Run

```
python3 tamper.py
```

Python 3, no extra libraries.
