# Task 2: use RC4

`rc4.py` gives you RC4 as a ready function: `keystream(key, n)` returns `n` bytes of keystream. For now, treat it as a black box.

Fill in the `TODO`s in `use_rc4.py`:

1. Decrypt the ciphertext with the key `Kangaroo`.
2. Change the last letter of the key to get `Kangarop`. Print the first 8 keystream bytes for both keys. How many bytes are the same?

Hint: `data.hex(" ")` prints bytes as hex with spaces.

## Run

```
python3 use_rc4.py
```

Python 3, no extra libraries.
