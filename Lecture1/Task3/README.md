# Task 3: one key, two messages

Somebody carelessly encrypted two messages with the same key, so both use the same keystream. From a reliable source you learned the first message.

Fill in the `TODO`s in `reuse.py` and print the second message:

1. Write `xor_bytes(a, b)`: XOR byte `i` of `a` with byte `i` of `b`. `bytes(numbers)` turns a list of numbers into bytes.
2. Get the keystream from `c1` and `p1`.
3. Decrypt `c2` and print it.

## Run

```
python3 reuse.py
```

Python 3, no extra libraries.
