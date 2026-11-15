# Ready examples (no TODO)

Run them and read the result. Each takes about 20 seconds.
`rc4.py` and `chacha.py` are the same black boxes as in the tasks.

| File | What it measures |
|---|---|
| `remember.py` | RC4: how often S[0] == key[0]; ChaCha20: how often the first keystream byte == key[0] |
| `second_byte.py` | how often the second keystream byte is 0, for RC4 and for ChaCha20 |

If a cipher's output looks random, each of these happens by chance: 1 in 256 = 0.39%.

## Run

```
python3 remember.py
python3 second_byte.py
```

Python 3, no extra libraries. The random seed is fixed, so every run prints the same numbers.

## Expected output

```
$ python3 remember.py
100000 random keys: first output byte == key[0] ?
  RC4      S[0] == key[0]          36.75%
  ChaCha20 first byte == key[0]     0.40%
  chance                            0.39%

$ python3 second_byte.py
100000 random keys: how often is the second keystream byte 0 ?
  RC4       0.78%   (779 keys)
  ChaCha20  0.36%   (362 keys)
  chance    0.39%
```

RC4 remembers the first key byte and makes the second byte 0 twice too often.
ChaCha20 looks like chance in both.
