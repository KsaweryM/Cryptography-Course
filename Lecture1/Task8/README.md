# Task 8: crack a short key

Two messages were encrypted with RC4 and very short keys: the first with a key of 1 byte, the second with a key of 2 bytes. You know that every message starts with `Hello`.

`rc4.py` is ready: `keystream(key, n)` returns `n` bytes of keystream. Fill in the `TODO`s in `crack.py`:

1. Find both keys by brute force: try every possible key.
2. Decrypt both messages.
3. The program prints the time for each key length. Estimate how long the same search would take for a key of 5 bytes, and of 16 bytes.

Hint: all keys of `n` bytes:

```python
for k in range(256 ** n):
    key = k.to_bytes(n, "big")
```

## Run

```
python3 crack.py
```

The 2-byte search takes a few seconds. Python 3, no extra libraries.
