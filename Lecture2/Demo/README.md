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
