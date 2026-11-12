# Task 9: change one byte

`aead.py` is ready: `seal(key, nonce, plaintext)` encrypts with ChaCha20 and adds a 16-byte Poly1305 tag,
`unseal(key, nonce, sealed)` checks the tag and decrypts, or raises `TagError`.

The attacker changes "100" into "900": XOR byte 4 with `0x08`. Fill in the `TODO`s in `tamper.py`:

1. Make `changed_plain`: a copy of `plain` (only ChaCha20, no tag) with byte 4 XORed with `0x08`.
2. Make `changed_sealed` in the same way from `sealed` (with a tag).
3. Decrypt `changed_plain` with `chacha20(key, nonce, 1, ...)` and print it.
4. Decrypt `changed_sealed` with `unseal(key, nonce, ...)` inside `try: ... except TagError`.

## Run

```
python3 tamper.py
```

Python 3, no extra libraries.
