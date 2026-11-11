# Task 4: X25519

`x25519_ready.py` is ready: `public_key(private)`, `x25519(private, public)` (RFC 7748) and `hkdf(secret, info)`
(RFC 5869). Fill in the `TODO`s in `ecdh.py`:

1. Compute Ania's and Bartek's public keys.
2. Compute the shared secret on both sides.
3. Check that both are equal (compare with RFC 7748, section 6.1).
4. Derive a 32-byte key for ChaCha20 with `hkdf`.

## Run

```
python3 ecdh.py
```

Python 3, no extra libraries.
