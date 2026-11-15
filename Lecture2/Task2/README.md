# Task 2: jump to the middle

Goal: decrypt ONLY block 700 of the film, using the counter.

`film.bin` is an encrypted "film": a ciphertext of 1000 blocks, 64 bytes each (64 000 bytes).
It was encrypted with `chacha.py` starting with counter 0, so block n used counter n.

`chacha.py` is ready: treat it as a black box. It gives one function:
`chacha20(key, nonce, counter, data)`. The key and the nonce are already in `jump.py`.

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

## Expected output

```
Frame 0700: the hero finally opens the red door.

one block: 0.00016 s
all 701:   0.10257 s
```

Your times will be different. One block should be hundreds of times faster than all 701.
