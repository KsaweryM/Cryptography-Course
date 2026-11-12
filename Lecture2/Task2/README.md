# Task 2: jump to the middle

`film.bin` is an encrypted "film" of 1000 blocks, 64 bytes each. It was encrypted with
`chacha.py` starting with counter 0, so block n used counter n.

The program already decrypts the whole film and prints block 700. Fill in the `TODO`s in `jump.py`:

1. Cut block 700 out of the film: bytes 700*64 to 701*64, a slice `film[start:end]`.
2. Decrypt only that block, without the blocks before it. Which counter do you need?

Then compare the times.

## Run

```
python3 jump.py
```

Python 3, no extra libraries.
