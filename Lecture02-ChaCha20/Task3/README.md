# Task 3: which one mixes faster?

## The situation

Salsa20 (2005) and ChaCha20 (2008) are two ciphers by the same author, Daniel J. Bernstein. Both fill a 4 by 4 table of 32-bit words with constants, the key, a nonce and a counter, and both mix it with add, rotate and xor. Both quarter rounds have 12 small steps. Bernstein made ChaCha20 because its quarter round should spread a change further. Is that true? Flip one input bit and count how many output bits change. A good mix changes about half of them.

![Two 4 by 4 tables. Salsa20: the constants on the diagonal, the key in eight cells around them, the nonce and the counter in the middle rows. ChaCha20: the constants in the first row, the key in rows 2 and 3, the counter and the nonce in row 4. Under each table, its quarter round as code. Salsa20: b ^= (a + d) <<< 7, c ^= (b + a) <<< 9, d ^= (c + b) <<< 13, a ^= (d + c) <<< 18. ChaCha20: a += b, d ^= a, d <<<= 16, then c += d, b ^= c, b <<<= 12, then the same with 8 and 7. The question: flip one input bit; how many of the 128 output bits change in Salsa20 and in ChaCha20, and after 1, 2, 3, 4 rounds of the whole table (512 bits)?](figure.svg)

## Goal

Measure how far one flipped bit spreads in Salsa20 and in ChaCha20: in one quarter round, and in the whole table after 1 to 4 rounds.

## Ready for you

- `salsa.py` and `chacha.py`: the two ciphers, with the same functions. Treat them as black boxes.
  - `quarter_round(s, a, b, c, d)` changes the words `s[a]`, `s[b]`, `s[c]`, `s[d]` of the list `s` in place, like a C function that gets a `uint32_t *`.
  - `rounds(s, n)` runs `n` rounds on a 16-word table `s` in place.
  - `initial_state(key, counter, nonce)` returns the start table. The nonce has 8 bytes in Salsa20 and 12 bytes in ChaCha20.
- `mix.py`: four input words `words` (the example of RFC 8439, section 2.1.1), the `key` 00 01 ... 1F, the function `changed_bits(x, y)` and the printing of the results.

## Steps

Predict first: which cipher spreads the change further? Then write your code in place of the `TODO` comments in `mix.py`. Each line of the output says `not done yet` until its TODO is done.

1. One quarter round: make two copies of the words, `x = list(words)` and `y = list(words)` (like `memcpy` into two arrays), and flip bit 0 of `a` in one of them: `y[0] ^= 1`. Run `salsa.quarter_round(x, 0, 1, 2, 3)` and the same on `y`. Add up `changed_bits(x[k], y[k])` for `k` from 0 to 3. Do the same with `chacha.quarter_round`.
2. One bit is only one sample. Repeat step 1 for each of the 128 input bits: bit `i % 32` of word `i // 32`, so `y[i // 32] ^= 1 << (i % 32)`. Print the average for each cipher.
3. The whole table: two keys that differ in one bit, `key2 = bytearray(key)`, then `key2[0] ^= 1`. For `n` from 1 to 4, build both start tables (`salsa.initial_state(key, 0, bytes(8))` and with `key2`), run `salsa.rounds(s, n)` on both and count the changed bits over all 16 words. The same with `chacha.initial_state(key, 0, bytes(12))`. Store `table[n] = [salsa_bits, chacha_bits]`; `table = {}` is a dictionary, which here works like an array indexed by `n`.

## Expected output

The bits changed by one quarter round for bit 0, the averages over 128 bits, and a small table of 4 rows. Random would be about half: 64 of 128, 256 of 512.

<details>
<summary>Check your answer</summary>

```
one quarter round, bit 0 of a flipped (of 128 bits):
  Salsa20:  31
  ChaCha20: 36
average over all 128 input bits: Salsa20 15.8, ChaCha20 25.1
whole table, one key bit flipped (of 512 bits; random would be about 256):
  rounds  Salsa20  ChaCha20
       1       15        37
       2      124       245
       3      234       238
       4      265       256
```

On average, the ChaCha20 quarter round changes about 25 bits where Salsa20 changes about 16: in ChaCha20 every word is changed twice, in Salsa20 once. In the whole table, ChaCha20 is at about half (random) after 2 rounds, Salsa20 only after 3 to 4. Both run 20 rounds, so both have a big margin.

</details>

## Run

```
python3 mix.py
```

About 8 minutes. Python 3, no extra libraries. It runs in well under a second.

Want to see it move? The [Salsa20 vs ChaCha20 step of the ChaCha20 explorer](https://ksawerym.github.io/Cryptography-simulators/chacha20/#6) shows the two quarter rounds side by side and colours the changed bits.
