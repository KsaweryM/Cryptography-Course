# Task 6: one full block

`quarter_round` is ready. Fill in the four `TODO`s in `block.py`:

1. Build the initial state: 4 constants, 8 key words, the counter, 3 nonce words.
2. Run 10 double rounds (a column round, then a diagonal round) on a copy of the state.
3. Add the initial state, word by word.
4. Return the 16 words as 64 little-endian bytes.

The program compares your block with the test vector from RFC 8439, section 2.3.2.

## Run

```
python3 block.py
```

Python 3, no extra libraries.
