# Task 9: change one byte

`aead.py` is ready: `seal(key, nonce, plaintext)` encrypts with ChaCha20 and adds a 16-byte Poly1305 tag,
`unseal(key, nonce, sealed)` checks the tag and decrypts, or raises `TagError`.

Fill in the `TODO`s in `tamper.py`: change "100" into "900" in two ciphertexts, one without a tag and one
with a tag, and try to decrypt both.

## Run

```
python3 tamper.py
```

Python 3, no extra libraries.
