# Task 8: crack a short key

## The situation

You have two messages encrypted with RC4 and very short keys: the first with a key of 1 byte, the second with a key of 2 bytes. You know that every message starts with `Hello`. The simplest attack is **brute force**: try every key until one turns the start of the ciphertext into `Hello`. Here it works. You also measure how fast the work grows with the key length.

![The start of c1, F3 CA 21 A4 C0, and the known start Hello, 48 65 6C 6C 6F. Each of the 256 keys of 1 byte is tried: key 00 gives 2D D2 A8 E5 63, key 01 gives F5 C2 2F AA D8, and so on, all wrong. One unknown key gives 48 65 6C 6C 6F, which matches. On the right: 256 keys for 1 byte, 65 536 for 2 bytes, about 1.1 times 10 to the 12 for 5 bytes, about 3.4 times 10 to the 38 for 16 bytes.](figure.svg)

## Goal

Find both keys, read both messages, and estimate how long longer keys would take.

## Ready for you

- `rc4.py`: `keystream(key, n)` returns `n` bytes of keystream for the key `key` (bytes).
- `crack.py`: the two ciphertexts `c1` (key of 1 byte) and `c2` (key of 2 bytes), `known = b"Hello"`, and a ready loop that runs `crack(c1, 1)` and `crack(c2, 2)` and prints the keys found and the time of each search.

## Steps

Write your code in place of the `TODO` comments in `crack.py`:

1. Write `crack(ciphertext, n)`: try every key of `n` bytes. For each key, XOR the first 5 bytes of the ciphertext with `keystream(key, 5)`. If all 5 results equal the bytes of `known`, add the key to the list `keys`.
2. In the ready loop, decrypt the whole ciphertext with `keys[0]` and print the message, in place of `print("not done yet: TODO 2")`.
3. The program prints the time of each search. From these two times, estimate (do not run it!) how long a key of 5 bytes, and of 16 bytes, would take. Print your two estimates in place of `print("not done yet: TODO 3")`.

Until a step is done, the program prints `not done yet: TODO n` for it.

Hint: there are 256<sup>n</sup> keys of `n` bytes (`256 ** n` in Python). This loop visits all of them, as bytes:

```python
for k in range(256 ** n):
    key = k.to_bytes(n, "big")    # the number k written into n bytes
```

## Expected output

Five lines: for each key length, the key found with the time, then the message; then your estimate. The keys and messages are always the same. The times depend on your computer.

<details>
<summary>Check your answer</summary>

```
1 byte(s): keys a7 , 0.01 s
Hello Bob, the meeting is moved to Friday.
2 byte(s): keys c35e , 3.12 s
Hello Alice, the spare key is under the blue pot.
```

Each extra byte multiplies the work by 256.

</details>

## Run

```
python3 crack.py
```

The 2-byte search takes a few seconds. About 8 minutes. Python 3, no extra libraries.
