# Task 1: first digests

## The situation

Alice sent Bob an invoice, `invoice.txt`. Before they use digests to check files, Bob wants to see the black box at work: what goes in, what comes out, and how long the output is. He also wants to be sure that his Python computes SHA-256 exactly as the standard says, so he first checks the test value printed in the standard FIPS 180-4 by NIST: the digest of the three letters `abc`.

![Four inputs in violet on the left: "abc" (3 bytes), "Hello, Bob!" (11 bytes), the empty input (0 bytes), the file invoice.txt, and one million zero bytes. Each goes into a dark box SHA-256. On the right, a brown box for each digest, "32 bytes = ?". Next to "abc", the value from FIPS 180-4, ba7816bf...f20015ad, and the question "the same?".](figure.svg)

## Goal

Compute SHA-256 of a short text, of empty data, of a file and of one megabyte, and see that the digest always has 32 bytes; check `abc` against the standard.

## Ready for you

- `first_digests.py`: the test value `FIPS_ABC` and the printing. Each line says `not done yet: TODO n` until its TODO is done.
- `invoice.txt`: Alice's invoice, 161 bytes.

`hashlib` is part of Python. `hashlib.sha256(data)` makes a hash object from `data` (a `bytes` object, like a `const uint8_t *` buffer with its length in C). On it, `.digest()` gives the 32 bytes of the digest and `.hexdigest()` the same bytes written as 64 hex digits. `b"abc"` is a `bytes` literal: the three bytes 0x61 0x62 0x63.

## Steps

Write your code in place of the `None` after each `TODO` in `first_digests.py`:

1. `abc_hex = hashlib.sha256(b"abc").hexdigest()`. The program compares it with the standard.
2. The digests of `b"Hello, Bob!"` and of `b""` (no bytes at all), with `.digest()`.
3. Read the file: `file_data = open("invoice.txt", "rb").read()` (`"rb"`: read bytes, like `fopen(name, "rb")` and `fread` of the whole file in C), then its digest.
4. The digest of `bytes(1000000)`: one million zero bytes.

## Expected output

`same as FIPS 180-4: True`, then four lines, each with `32 bytes out`, whatever came in: 11 bytes, 0 bytes, 161 bytes, a million bytes.

<details>
<summary>Check your answer</summary>

```
SHA-256(abc):     ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
same as FIPS 180-4: True
short text: 11 bytes in, 32 bytes out: 2558308eb3f6e132ab8ea8e38267d741ad28d99e5144e5767f4833517caa8d7f
empty data:  0 bytes in, 32 bytes out: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
invoice.txt: 161 bytes in, 32 bytes out: 1bb10a59b102acfc16ec61cc4cadecb33ab99a8488ce180c241025063e46ba94
1000000 zero bytes in, 32 bytes out: d29751f2649b32ff572b5e0a9f541ea660a50f94ff0beedfb0b692b924cc8025
```

Even empty data has a digest of 32 bytes. Everybody who hashes the same bytes gets exactly these hex digits, on any computer.

</details>

## Run

```
python3 first_digests.py
```

About 6 minutes. Python 3.8 or newer, no extra libraries.
