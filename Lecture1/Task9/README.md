# Task 9: one key, many messages

You and a friend share one secret key, `our secret`, and you want to send many messages. `rc4.py` is ready: `rc4(key, data)` encrypts and decrypts. `xor(a, b)` is ready in `one_key.py`.

**Step 1.** Encrypt two messages with the same key and check:

- `xor(c1, c2) == xor(m1, m2)`
- `rc4(key, m1) == rc4(key, m1)` (the same message, sent twice)

When is this dangerous?

**Step 2.** Fix it, and keep one secret key. For every message, make a new value of 3 bytes (`random.randbytes(3)`). It does not have to be secret: it is sent in the open, together with the ciphertext. It must change the ciphertext. Check:

1. `xor(c1, c2) == xor(m1, m2)` should be `False`.
2. `m1` sent twice, with two new values, should give two different ciphertexts.
3. Your friend, who knows the key and the value, can decrypt `c1`.

Hint: `b"ab" + b"cd" == b"abcd"`

## Run

```
python3 one_key.py
```

Python 3.9 or newer (for `random.randbytes`), no extra libraries.
