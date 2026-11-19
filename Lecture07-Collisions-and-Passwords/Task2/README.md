# Task 2: collisions of a short digest

## The situation

A full SHA-256 digest has 256 bits, and nobody has ever found two inputs with the same one. Here we keep only the first 24, 32 or 40 bits of SHA-256: a **short digest**. The birthday paradox says that among N possible values a repeat comes after about 1.18 √N random tries, so with n bits after about 1.18 · 2^(n/2). Is that true for a real hash?

![Messages "note 0", "note 1", "note 2", ..., "note j" go into SHA-256, of which only the first bits are kept; each gives a short digest shown as question marks. A table "seen" maps short digest to note number, like a hash table in C. The digest of note j is "seen before!". Sizes 24, 32, 40 bits; prediction about 1.18 · 2^(n/2) notes; your answer i = ?, j = ?](figure.svg)

## Goal

For 24, 32 and 40 bits, find two messages "note i" and "note j" with the same short digest, and compare the number of messages you needed with the prediction.

## Ready for you

- `find_collision.py`: `short_hash(data, bits)` returns the first `bits` bits of SHA-256(data) as a whole number.
- The loop at the end runs `find_collision(bits)` for 24, 32 and 40 bits and measures the time.
- `seen = {}` is a Python dictionary: a hash table, as you would write in C, with the short digest as the key and the message number as the value. `h in seen` asks "is this key in the table?" in one step; `seen[h] = i` stores a value; `seen[h]` reads it back.

Before you run it, predict: about how many messages for 40 bits?

## Steps

Write your code in `find_collision.py`, in place of the `TODO` comments:

1. In `find_collision`, compute the short digest of the message: `h = short_hash(message, bits)`.
2. If `h` is already in `seen`, you have a collision: return `(seen[h], i)`, the number of the earlier message and of this one.
3. Otherwise remember it: `seen[h] = i`. Then delete the line `return None   # remove this line ...`.
4. In the loop at the end, replace the `not done yet: TODO 4` line with the `print` given in the comment above it.

## Expected output

One line per size. The messages are fixed, so everybody gets the same notes; only the times differ between computers.

<details>
<summary>Check your answer</summary>

```
24 bits: note 1076 and note 4202 -> 5a34b2, after 4203 messages (predicted about 4833), 0.02 s
32 bits: note 53529 and note 75183 -> 42f58c3e, after 75184 messages (predicted about 77332), 0.19 s
40 bits: note 803992 and note 915856 -> d8ff4c408b, after 915857 messages (predicted about 1237320), 2.25 s
```

The prediction is where the chance reaches 50%, so a real search ends a bit earlier or later. Every 8 more bits make the search about 2^4 = 16 times longer; to hit one **given** 40-bit digest you would need about 2^40, a trillion tries.

</details>

## Run

```
python3 find_collision.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries; the program runs a few seconds.
