# Task 2: use RC4

`rc4.py` gives you RC4 as a ready function: `keystream(key, n)` returns `n` bytes of keystream. For now, treat it as a black box.

Fill in the `TODO`s in `use_rc4.py`:

1. Make a keystream as long as the ciphertext, with the key `Kangaroo`. Print its length.
2. Decrypt: XOR each ciphertext byte with its keystream byte, turn each result into a character (`chr`), print the message.
3. Change the last letter of the key to get `Kangarop`. Print the first 8 keystream bytes for both keys. How many bytes are the same?

Hints: `len(ciphertext)` is the number of bytes. `data.hex(" ")` prints bytes as hex with spaces.

## Run

```
python3 use_rc4.py
```

Python 3, no extra libraries.
