# Task 6: hash, then sign

## The situation

Alice signs a whole update file, 100 000 bytes, far more than the 256 bytes of `n`. So she uses hash-and-sign: she signs the SHA-256 of the file, read as a number. Bob checks the file he downloaded. Mallory flips one bit of it. Then Mallory tries the trick of Task 5 again: Alice hash-signed two orders, "Pay Mallory 20 pounds. Alice" and "Pay Mallory 50 pounds. Alice", and Mallory multiplies the two signatures.

![update.bin, 100 000 bytes, goes through SHA-256 to "hash as a number = ?", and with Alice's d, n to s = ?. Bob checks the file: ? and the file with one bit of byte 50 000 flipped: ?. Mallory offers sig_20 x sig_50 mod n for "Pay Mallory 1000 pounds. Alice": bank = ?](figure.svg)

## Goal

Sign a large file with one RSA signature, see that one changed bit fails, and see that multiplying signatures no longer forges anything.

## Ready for you

- `alice_key.py`: `n`, `e`, `d` and `short(x)`, as in Task 4.
- `hash_and_sign.py`: `read_file(path)`, the file `update` (bytes), the three orders, and `sig_20`, `sig_50` read from `signed_orders.txt`.
- `hashlib.sha256(data).digest()`: the 32-byte SHA-256 of `data`.

## Steps

Write your code in place of the `None` after each `TODO` in `hash_and_sign.py`:

1. Finish `hash_number(data)`: the SHA-256 of `data` read as a big-endian number.
2. `s`: Alice signs the hash of `update`: `pow(hash_number(update), d, n)`.
3. `check`: Bob hashes the file himself and compares: `pow(s, e, n) == hash_number(update)`.
4. `check_changed`: copy the file into a `bytearray` (a writable buffer, like `uint8_t buf[]` in C), flip the lowest bit of byte 50000 with `^= 1`, and check `s` on `bytes(changed)`.
5. `check_forged`: `forged = sig_20 * sig_50 % n`, checked on `order_1000` as in step 3.

Before step 5, predict: will the bank accept 1000 pounds this time?

## Expected output

<details>
<summary>Check your answer</summary>

```
file: 100000 bytes, its hash as a number: 710fcd1df5b9...3416108c9faf (64 hex digits)
s = bf0aa615a40e...f8609c05042f (512 hex digits)
Bob checks the file:         True
Bob checks the changed file: False
the bank checks the forged 1000: False
```

One signature covers the whole file, and one changed bit gives a completely different hash. The product of two signatures signs the number H(order_20) x H(order_50) mod n, which is not the hash of any message Mallory can find.

</details>

## Run

```
python3 hash_and_sign.py
```

About 9 minutes. Python 3 and the library `cryptography` (only `alice_key.py` uses it).
