# Task 4: invert a short hash

## The situation

Alice's door lock shows a short check code next to her note `Alice: the door code is 0886`: only the first few bits of the SHA-256 digest of the note. Mallory sees the short code but not the note. To fool the lock she needs **any** input whose short code is the same: that is a preimage. Her only method is the generic one: try inputs `0`, `1`, `2`, ... and compare. You play Mallory for codes of 12, 16 and 20 bits, count the tries, and then work out how long the same attack would take on all 256 bits.

![A violet note "Alice: the door code is 0886" goes into SHA-256; only the first k bits of the brown digest are kept, for k = 12, 16, 20. Mallory, in pink, feeds the inputs "0", "1", "2" and so on into the same SHA-256 and compares the first k bits with the target. A counter "tries = ?" and a clock "seconds = ?".](figure.svg)

## Goal

Measure how many tries the generic attack needs for a k-bit digest, compare with 2^k, and extrapolate to 256 bits.

## Ready for you

- `invert_short.py`:
  - `NOTE`: Alice's note.
  - `short_hash(data, k)`: the first k bits of SHA-256(data), as a number.
  - the printing of TODO 3. Each part says `not done yet: TODO n` until its TODO is done.

## Steps

1. In `invert(target, k)`: a loop over `i = 0, 1, 2, ...`. The input is `str(i).encode()`: the decimal digits of `i` as bytes, like `sprintf(buf, "%d", i)` in C. Add 1 to `tries`; when `short_hash(input, k) == target`, return `(tries, input)` (two values at once, like a small struct).
2. For `k` in 12, 16, 20: `target = short_hash(NOTE, k)`, then `(tries, found) = invert(target, k)`. Measure the time: `t0 = time.perf_counter()` before, `time.perf_counter() - t0` after (seconds, like `clock_gettime` in C). Print one line per `k` in the format given in the TODO, and keep the tries and seconds of the last `k`.
3. Your speed: `rate = last_tries / last_seconds` hashes per second. All 256 bits need about 2^256 tries: `years = 2**256 / rate / (365 * 24 * 3600)`. (`**` is the power in Python; Python integers have no size limit.)

Predict first: 12 bits need about 2^12 = 4096 tries. How many for 16 bits? For 20 bits?

## Expected output

Three lines with the tries close to 2^k, each 4 more bits about 16 times more tries and time, then your speed and the number of years for 256 bits. Your times will differ, the proportions will not.

<details>
<summary>Check your answer</summary>

```
k = 12:      3715 tries (2^k =      4096),   0.01 s, found b'3714'
k = 16:     64050 tries (2^k =     65536),   0.16 s, found b'64049'
k = 20:   1017612 tries (2^k =   1048576),   2.12 s, found b'1017611'
your speed: 480081 hashes per second
all 256 bits: about 7.6e+63 years
```

(Intel Core i5-8265U laptop, Python 3.12.) The number of tries for one target is random; on average over many targets it is 2^k. Every 4 bits more multiply the work by 16. For 256 bits the answer has 64 digits of years; the universe is about 1.4e+10 years old.

</details>

## Run

```
python3 invert_short.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries. The program runs for a few seconds.
