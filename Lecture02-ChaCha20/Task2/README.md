# Task 2: jump to the middle

## The situation

Alice sent Bob an encrypted film, `film.bin`: 64 000 bytes of ciphertext, cut into 1000 blocks of 64 bytes. It was encrypted with ChaCha20 starting with counter 0, so **block n used counter n**. Bob wants to watch only frame 700. With RC4 he would have to make the keystream from the very start. With ChaCha20 he can set the counter to 700 and decrypt that one block.

![The film as a strip of 1000 blocks: block 0 at byte 0, block 1 at byte 64, block 699 at byte 44 736, block 700 at byte 44 800, block 701 at byte 44 864, up to block 999 at byte 63 936. Under each block is its counter, 0 to 999. Slow: decrypt all 701 blocks, counter 0 to 700. Fast: jump straight to block 700: the same key and nonce, counter 700, only 64 bytes go into ChaCha20, and out comes Frame 0700 followed by unknown text.](figure.svg)

## Goal

Decrypt **only** block 700 of the film, using the counter, and measure how much time that saves.

## Ready for you

- `chacha.py`: `chacha20(key, nonce, counter, data)` encrypts and decrypts. It uses `counter` for the first 64 bytes of `data`, `counter + 1` for the next 64, and so on.
- `jump.py`: the `key` and the `nonce` of the film, and `data`: all 64 000 bytes of `film.bin`.

## Steps

Write your code in place of the `TODO` comments in `jump.py`. Each line of the output says `not done yet` until its TODO is done.

1. Cut out block 700 into `block`: bytes `700*64` to `701*64`. Use a slice: `data[start : end]` gives the bytes from `start` up to `end - 1` (like the `end - start` bytes at `data + start` in C).
2. Decrypt that block with `counter = 700` into `frame`. The printing is ready: `frame.decode()` turns the bytes into text.
3. Time it into `one` and `all701`: one block versus all 701 blocks (blocks 0 to 700, so `data[0 : 701*64]` with counter 0).
   - `start = time.perf_counter()` before, `time.perf_counter() - start` after: the time in seconds.
   - The printing is ready: `print(f"one block: {one:.5f} s")` works like `printf("one block: %.5f s\n", one)` in C.

## Expected output

Frame 700 of the film, then two times. The block ends with a newline, so an empty line follows the text. Your times will be different, but one block should be hundreds of times faster than all 701.

<details>
<summary>Check your answer</summary>

```
Frame 0700: the hero finally opens the red door.

one block: 0.00014 s
all 701:   0.10195 s
```

</details>

## Run

```
python3 jump.py
```

About 5 minutes. Python 3, no extra libraries.

Want to see it move? In the [ChaCha20 black box](https://ksawerym.github.io/Cryptography-simulators/chacha20/#1), change the counter and watch your message move along the keystream.
