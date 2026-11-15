# Task 3: one key, two messages

**Goal:** somebody carelessly encrypted two messages with the same key, so both use the same keystream. From a reliable source you learned that the first message is `MEET ME AT 9 PM`. Decrypt the second message.

**Ready:** `reuse.py` holds the two ciphertexts and the known first message:

```
C1  A6DA32D597798F52E64D6A1147E60F
C2  BFD732A1E77D8452EE4A6A1C568170
P1  MEET ME AT 9 PM
```

## Steps

Write the code in place of the `TODO` lines in `reuse.py`:

1. Write `xor_bytes(a, b)`: XOR byte `i` of `a` with byte `i` of `b`. `bytes(numbers)` turns a list of numbers into bytes.
2. Get the keystream from `c1` and `p1`.
3. Decrypt `c2` and print it.

## Run

```
python3 reuse.py
```

About 10 minutes. Python 3, no extra libraries.
