# Task 5: which mirror is honest?

## The situation

Alice wrote a text editor. She publishes the file `editor-2.4.1-installer.bin` (200 000 bytes) on three download mirrors, servers of other people that copy her file so that it downloads fast everywhere. On her own website she publishes only one line: the SHA-256 digest of the file, in a file called `SHA256SUMS`. Bob downloaded the file from all three mirrors. Every mirror also offers its own `SHA256SUMS` next to the file. Mallory controls one or more of the mirrors.

![On top, Alice in indigo and her website with a brown SHA256SUMS: 347ec73c...690e89d1. Below, three mirrors, mirror-a, mirror-b, mirror-c, each with a violet file editor-2.4.1-installer.bin of 200 000 bytes and its own brown SHA256SUMS. Mallory in pink stands next to the mirrors with a question mark. Bob in teal downloads from all three and asks "the same as on Alice's website?".](figure.svg)

## Goal

Compute the SHA-256 of each downloaded file, reading it in pieces, and find out which copies are Alice's file: first against Alice's website, then against each mirror's own `SHA256SUMS`.

## Ready for you

- `check_mirrors.py`:
  - `read_sums(path)`: the digest from a `SHA256SUMS` file (64 hex digits, two spaces, the file name).
  - `published`: the digest from Alice's website, `website/SHA256SUMS`.
- `website/SHA256SUMS`, and `mirror-a/`, `mirror-b/`, `mirror-c/`, each with the file and its own `SHA256SUMS`.

## Steps

1. In `sha256_of_file(path)`: open the file with `open(path, "rb") as f`, and in a loop read `piece = f.read(4096)`; stop when `piece == b""` (the end of the file, like `fread` returning 0 in C), otherwise `h.update(piece)`. At the end `return h.hexdigest()`. `update` adds the next piece to the hash, so even a 5 GB file needs only 4096 bytes of memory.
2. For each mirror, compare the digest of its file with `published` and print `OK` or `CHANGED`.
3. Now compare each mirror's file with the `SHA256SUMS` **on that mirror**, `read_sums(m + "/SHA256SUMS")`, and print the result in the same way.

Before step 3, think: if a mirror's file and its own `SHA256SUMS` agree, does that prove the file is Alice's?

## Expected output

Step 2 finds the honest mirror. Step 3 gives a different answer for one mirror: think about why.

<details>
<summary>Check your answer</summary>

```
Alice's website says: 347ec73c3723bd33801f50ea0b3fd0e010a989c4c05a5c1d2365a17e690e89d1
mirror-a: OK
mirror-b: CHANGED
mirror-c: CHANGED
mirror-a against its own SHA256SUMS: OK
mirror-b against its own SHA256SUMS: CHANGED
mirror-c against its own SHA256SUMS: OK
```

Only mirror-a has Alice's file. In mirror-b one bit of byte 123 456 is different (a broken copy, or a clumsy attacker), and the digest catches it. Mirror-c is Mallory's: she changed the file **and** wrote a new `SHA256SUMS` for it, so the mirror agrees with itself. A digest proves only that the file matches **that digest**; the digest must come from a place Mallory cannot change, here Alice's own website.

</details>

## Run

```
python3 check_mirrors.py
```

About 8 minutes. Python 3.8 or newer, no extra libraries. On Linux and macOS you can compare with the command `sha256sum mirror-*/editor-2.4.1-installer.bin`.

The files were made by `Lecture06-Hash-Functions/checks/make_task5.py`; running it again gives the same files.
