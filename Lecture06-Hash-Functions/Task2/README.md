# Task 2: count the changed bits

## The situation

Alice writes to Bob: `Meet Carol at the library at 10:00`. Mallory changes one single bit of the message on the way: the lowest bit of the first byte, so `M` (0x4D) becomes `L` (0x4C). Bob compares the SHA-256 digest of what he got with the digest of what Alice sent. How different are the two digests: one bit, a few bits, or more? Then you repeat the experiment 1000 times with other messages to see whether the first result was luck.

![Two messages in violet, "Meet Carol at the library at 10:00" and "Leet Carol at the library at 10:00", with the changed bit of the first byte marked: 0100 1101 and 0100 1100. Each goes into SHA-256; the two brown digests, 256 bits each, are compared bit by bit with XOR, and a counter asks "changed bits = ? of 256".](figure.svg)

## Goal

Count in how many of the 256 bit positions two digests differ, for one pair and for 1000 pairs, and see what one changed bit of input does to the output.

## Ready for you

- `avalanche.py`:
  - `MESSAGE`: Alice's message.
  - `flip_bit(data, i)`: a copy of `data` with bit number `i` changed (bit 0 is the lowest bit of byte 0).
  - the printing, including a small text histogram. Each line says `not done yet: TODO n` until its TODO is done.

## Steps

1. In `count_diff_bits(a, b)`: for every index `i`, `x = a[i] ^ b[i]` has a 1 exactly where the two bytes differ (XOR, as in C). Count the ones of `x` with a loop as in C: `while x != 0: count = count + (x & 1); x = x >> 1`. Return `count`. The program tests it: 0x0f and 0x01 differ in 3 bits.
2. One pair: `d1` and `d2` are the SHA-256 digests (`.digest()`, 32 bytes) of `MESSAGE` and of `flip_bit(MESSAGE, 0)`; `one_pair = count_diff_bits(d1, d2)`.
3. 1000 trials: for `t` from 0 to 999, `m1 = MESSAGE + t.to_bytes(4, "big")` (the message with the trial number appended as 4 bytes, so every trial has a different message), `m2 = flip_bit(m1, t % (8 * len(m1)))` (one bit changed, at a different place every time), and count the differing bits of their digests. Keep the smallest, the largest and the sum, and add 1 to `histogram[diff]`.

Predict first: one bit of the input changed. How many of the 256 output bits change?

## Expected output

The test line, the two digests and the number of changed bits, then the smallest, largest and average of 1000 trials and a histogram.

<details>
<summary>Check your answer</summary>

```
test: 0x0f and 0x01 differ in 3 bits (should be 3)
digest 1: 732060cea8098b9544f35ac67fd4eb6f92cf7d28d07620fe0b090978a02f231d
digest 2: 46da9bbfaac6536ff0615de35d84bbd3a2babdf8983d87d8470a92e72964dd8f
one bit changed in the message, 121 of 256 bits changed in the digest
1000 trials: smallest 104  largest 152  average 127.723
how many trials gave each number of changed bits (one # per 5 trials):
  100 to 103:  0
  104 to 107:  2
  108 to 111: ### 19
  112 to 115: ######### 48
  116 to 119: ################# 89
  120 to 123: ############################## 154
  124 to 127: ###################################### 191
  128 to 131: ################################## 172
  132 to 135: ############################### 155
  136 to 139: ################### 95
  140 to 143: ######## 42
  144 to 147: #### 23
  148 to 151: # 9
  152 to 155:  1
  156 to 159:  0
```

About half of the 256 bits change, never just a few: the digests of two almost equal messages look like two unrelated random numbers. This is the avalanche effect.

</details>

## Run

```
python3 avalanche.py
```

About 8 minutes. Python 3.8 or newer, no extra libraries. The 1000 trials take well under a second.
