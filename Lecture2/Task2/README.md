# Task 2: jump to the middle

`film.bin` is an encrypted "film": a ciphertext of 1000 blocks, 64 bytes each (64 000 bytes).
It was encrypted with `chacha.py` starting with counter 0, so block n used counter n.

Goal: decrypt ONLY block 700 of the film, using the counter. `chacha.py` is ready:
`chacha20(key, nonce, counter, data)`.

Fill in the `TODO`s in `jump.py`:

1. Cut out block 700: bytes 700*64 to 701*64, a slice `data[start : end]`.
2. Decrypt that block with counter = 700 and print it.
3. Time it: one block vs all 701 blocks (blocks 0 to 700, counter 0).
   `start = time.perf_counter()` before, `time.perf_counter() - start` after.

## Run

```
python3 jump.py
```

Python 3, no extra libraries.
