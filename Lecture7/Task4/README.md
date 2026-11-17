# Task 4: two real collisions

## The situation

In 2004 Xiaoyun Wang, Dengguo Feng, Xuejia Lai and Hongbo Yu published two different 128-byte messages with the same MD5 digest. In 2017 researchers from CWI Amsterdam and Google (SHAttered) published two different PDF files with the same SHA-1 digest. You have both pairs: `md5_a.bin` and `md5_b.bin` (Wang's messages) and `sha1_a.bin` and `sha1_b.bin` (the first 320 bytes of the two SHAttered PDFs, downloaded from shattered.io on 2026-11-17; after these 320 bytes the inner state of SHA-1 is already the same, so the rest of the PDF is not needed).

![Two pairs of files: md5_a.bin and md5_b.bin, 128 bytes, Wang, Feng, Lai, Yu (2004); sha1_a.bin and sha1_b.bin, 320 bytes, the start of the SHAttered PDFs (2017). For each file the MD5, SHA-1 and SHA-256 digests are question marks, with "same?" under each pair. Then: add the same text to the end of both files of each pair: are the digests still the same?](figure.svg)

## Goal

Check which hash function each pair breaks, and whether the collision survives when the same text is added to the end of both files.

## Ready for you

- `real_collisions.py`: `load_file(path)`, the list of the two pairs, `SUFFIX` (the text to add), and the loop over the pairs.
- `hashlib.md5(data).hexdigest()`, `hashlib.sha1(data).hexdigest()`, `hashlib.sha256(data).hexdigest()` return a digest as hex text. `a + SUFFIX` joins two byte strings, like `memcpy` of both into one buffer in C.

Before you run it, predict: does the MD5 pair also collide in SHA-1? Does it still collide after you add text?

## Steps

Write your code in `real_collisions.py`, in place of the `TODO` comments:

1. In `count_different`, count the positions `i` where `a[i] != b[i]`: an index loop over `range(len(a))`, as in C. Return the count.
2. Print the MD5, the SHA-1 and the SHA-256 of `a` and of `b`, one line each.
3. Add `SUFFIX` to the end of both (`a + SUFFIX`, `b + SUFFIX`) and print their MD5 and SHA-1 again.

## Expected output

<details>
<summary>Check your answer</summary>

```
md5_a.bin and md5_b.bin: 128 bytes each, 6 bytes differ
  MD5     a: 79054025255fb1a26e4bc422aef54eb4
  MD5     b: 79054025255fb1a26e4bc422aef54eb4
  SHA-1   a: a34473cf767c6108a5751a20971f1fdfba97690a
  SHA-1   b: 4283dd2d70af1ad3c2d5fdc917330bf502035658
  SHA-256 a: 8d12236e5c4ed9f4e790db4d868fd5c399df267e18ff65c1107c328228cffc98
  SHA-256 b: b9fef2a8fc93b05e7701e97196fda6c4fbeea25ff8e64fdfee7015eca8fa617d
  with the suffix: MD5   a: 2eb33e858c3caeed58bda9dc975f5d21
  with the suffix: MD5   b: 2eb33e858c3caeed58bda9dc975f5d21
  ...
sha1_a.bin and sha1_b.bin: 320 bytes each, 62 bytes differ
  MD5     a: 736acaed4ec96ab7120fb5fd750f1f07
  MD5     b: 80e808e7abdbe9109903c71f049a30f7
  SHA-1   a: f92d74e3874587aaf443d1db961d4e26dde13e9c
  SHA-1   b: f92d74e3874587aaf443d1db961d4e26dde13e9c
  ...
  with the suffix: SHA-1 a: 61d5e3914c69b226129d601cebadb818fafc8edd
  with the suffix: SHA-1 b: 61d5e3914c69b226129d601cebadb818fafc8edd
```

Each pair breaks only the function it was computed for; SHA-256 tells all four files apart. A common suffix keeps the collision, because after the colliding blocks both files have the same inner state, and the rest of the input is processed the same way.

</details>

## Run

```
python3 real_collisions.py
```

About 8 minutes. Python 3.8 or newer, no extra libraries.
