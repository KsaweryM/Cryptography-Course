# Task 11: continue a digest (length extension)

## The situation

Alice keeps a 38-byte note secret. She published only its SHA-256 digest, `778f6ad4...`, and its length. Mallory does not know a single byte of the note. Yet she wants the SHA-256 of a longer message that **starts with Alice's note** and ends with her own bytes, `" P.S. Give Mallory the key."`. In SHA-256 the digest is the whole state after the last block, so Mallory can load it as a state and keep going.

![Top: the chain of Alice. Her secret note (amber, "????", 38 bytes) and its padding, the glue (grey, 0x80, zeros, the length), form one block; IV and the block go into compress, out comes the brown digest 778f6ad4..., published. Bottom: Mallory starts from that digest as a state, adds one block with her violet bytes " P.S. Give Mallory the key." and new padding, and gets "digest = ?". On the right, the question "= SHA-256(note + glue + extra)?".](figure.svg)

## Goal

Without the note, compute SHA-256(note + glue + extra) from the published digest alone, and check that it is right.

## Ready for you

- `sha256_ready.py` (the same file as in Task 10, you do not need to read it): `pad`, `compress`, `state_to_bytes`.
- `extend.py`: `DIGEST`, `LENGTH`, Mallory's `EXTRA`, the function `pad_continued(extra, done)` (the bytes `extra` followed by the padding of a whole message of `done + len(extra)` bytes) and the check at the end. Only the check knows the note.

## Steps

1. The digest is the whole last state. Turn its 32 bytes back into the 8 words of the state: word `i` is `int.from_bytes(DIGEST[4 * i:4 * i + 4], "big")` for `i` from 0 to 7, like reading 8 big-endian `uint32_t` from a buffer in C. Print the first word.
2. The padding that SHA-256 put after the note depends only on its length. Get these bytes, the **glue**, from `pad` of any 38 bytes: everything after the first 38 bytes. Print its length and hex.
3. Continue the chain: `tail = pad_continued(EXTRA, LENGTH + len(glue))`, then one `compress` per 64-byte block of `tail`, starting from the state of step 1, as in Task 10. Print the result as 32 bytes in hex.

## Expected output

The first word of the state, the glue, Mallory's digest, the real SHA-256 of the long message, and `the same: True`.

<details>
<summary>Check your answer</summary>

```
state from the digest: 778f6ad4 ...
glue: 26 bytes: 8000000000000000000000000000000000000000000000000130
Mallory's digest: 20a7ec53526297ddd2440e28debe82701cc5b98883fd852b50545e52bf9a4682
SHA-256(note + glue + extra): 20a7ec53526297ddd2440e28debe82701cc5b98883fd852b50545e52bf9a4682
the same: True
```

The glue is `80`, 17 zero bytes and the length of the note in bits, 38 × 8 = 304 = 0x130. Mallory never saw the note, but she now knows the digest of a 91-byte message that begins with it. This is no collision and no preimage; it only follows from "the digest is the last state". It becomes an attack when the secret at the start is a key: Lecture 8.

</details>

## Run

```
python3 extend.py
```

About 8 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? The simulator: [ksawerym.github.io/Cryptography-simulators/hash/#8](https://ksawerym.github.io/Cryptography-simulators/hash/#8).
