# Task 9: build SHA-256 from its parts

## The situation

Bob wants to see that SHA-256 really is the Merkle-Damgård construction from the slides: pad the message, cut it into 64-byte blocks, and feed the blocks one by one into the compression function, which carries a state of 8 words from block to block. The hard part, the compression function with its 64 rounds, is ready in `sha256_ready.py`. You write the rest and compare your digest with `hashlib`.

![A violet message is padded (grey 0x80, zero bytes and the length) and cut into 64-byte blocks, block 1 and block 2. The starting state IV (8 words, 6a09e667 ...) goes into a dark box compress together with block 1; the new state goes into the next compress with block 2; the last state is the brown digest "= ?", compared with hashlib.](figure.svg)

## Goal

Find how many blocks the padding makes, then build SHA-256 from `pad` and `compress` and get exactly the digest of `hashlib`.

## Ready for you

- `sha256_ready.py` (FIPS 180-4, in plain Python; you do not need to read it):
  - `IV`: the starting state, a list of 8 numbers of 32 bits (like `uint32_t iv[8]` in C).
  - `pad(message)`: the message followed by the byte 0x80, zero bytes, and the length of the message in bits as 8 bytes, so that the total is a multiple of 64.
  - `compress(state, block)`: the compression function; a state of 8 words and one 64-byte block in, a new state of 8 words out.
  - `state_to_bytes(state)`: the 8 words as 32 bytes.
- `build_sha256.py`: the test at the end, which compares your function with `hashlib.sha256` for a 3-byte and a 79-byte message.

## Steps

1. Predict first: how many 64-byte blocks for a message of 3 bytes, 55, 56, 64 bytes? Then check: for each `n`, `padded = pad(bytes(n))`, `blocks = len(padded) // 64` (`//` is integer division, as `/` on `int` in C), and print with the format in the TODO.
2. In `my_sha256(message)`: `padded = pad(message)`, `state = IV`, then for `i = 0, 64, 128, ...` below `len(padded)` (`range(0, len(padded), 64)`): `state = compress(state, padded[i:i + 64])`. `padded[i:i + 64]` is the 64 bytes from index `i`, like `&padded[i]` with length 64 in C. Print the first word of the state after each block, then `return state_to_bytes(state)`.

## Expected output

The four lines of step 1, then for each test message the state after each block, your digest, the one of `hashlib`, and `the same: True`.

<details>
<summary>Check your answer</summary>

```
 3 bytes ->  64 bytes after padding, 1 block(s)
55 bytes ->  64 bytes after padding, 1 block(s)
56 bytes -> 128 bytes after padding, 2 block(s)
64 bytes -> 128 bytes after padding, 2 block(s)
3 bytes: b'abc'
  after block 1: ba7816bf ...
  mine:    ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
  hashlib: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
  the same: True
79 bytes: b'The quick brown fox jumps over the lazy dog, then over the lazy cat, then home.'
  after block 1: 26988411 ...
  after block 2: 8c166dba ...
  mine:    8c166dbaa503f9d49ad48c6326a284d5c5c0af17d9757fe2cf841e37d5d21b20
  hashlib: 8c166dbaa503f9d49ad48c6326a284d5c5c0af17d9757fe2cf841e37d5d21b20
  the same: True
```

55 bytes still fit in one block (55 + 1 byte 0x80 + 8 bytes of length = 64), 56 bytes do not, so the padding adds a whole second block. The state after the last block **is** the digest: compare `ba7816bf` with the first 8 hex digits of SHA-256("abc").

</details>

## Run

```
python3 build_sha256.py
```

About 12 minutes. Python 3.8 or newer, no extra libraries.
