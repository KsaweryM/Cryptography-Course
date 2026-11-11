# Task 2: jump to the middle

`film.bin` is an encrypted "film" of 1000 blocks, 64 bytes each. It was encrypted with
`chacha20_ready.py` starting with counter 0, so block n used counter n.

The program already decrypts the whole film and prints block 700. Fill in the `TODO` in `jump.py`:
decrypt only block 700, without the blocks before it, and compare the times.

## Run

```
python3 jump.py
```

Python 3, no extra libraries.
