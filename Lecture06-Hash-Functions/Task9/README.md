# Task 9: a Merkle tree

## The situation

Alice releases version 2.5 of her editor as 8 files. On her website she publishes only **one** digest: the root of the Merkle tree of the 8 files. Bob needs just one file, the English spelling dictionary `spell-en.dat` (leaf 5), and downloads it from a mirror together with a short proof: three digests. Can Bob check his one file against Alice's root, without downloading the other seven? And what happens when Mallory's mirror hands out a changed dictionary with the same proof?

![Eight violet files at the bottom, leaves 0 to 7 (README.txt ... LICENSE.txt); above them brown digests, joined in pairs up to one root at the top, "on Alice's website: 34e794e7...". Leaf 5, spell-en.dat, is Bob's; the three digests of the proof are marked with teal frames: leaf 4, the right node of level 1 and the left node of level 2. Next to it Mallory with her own spell-en.dat and the question "the root again?".](figure.svg)

## Goal

Build the tree of the 8 files and get Alice's root; check Bob's file with a proof of 3 digests; see how short a proof stays for a million files.

## Ready for you

- `release/`: Alice's 8 files.
- `mirror-spell-en.dat`: the dictionary from Mallory's mirror.
- `merkle.py`: the names of the files in leaf order, Alice's `ROOT`, Bob's `PROOF`, `H(data)` (SHA-256 as 32 bytes), `read(name)` and the printing.

A proof is a list of pairs `(side, sibling)`: on every level from the leaves up, the digest of the node next to Bob's node, and whether it stands on its left or on its right. `a + b` on two `bytes` objects joins them, like `memcpy` of `a` and then `b` into one buffer in C.

## Steps

1. Build the tree. The leaves: a list with `H(file)` of every file, in the order of `NAMES`. Then, while the list has more than one digest, make the level above it: the parent of the digests `i` and `i + 1` (for `i = 0, 2, 4, ...`) is `H(left + right)`. The last digest is the root; compare it with `ROOT`.
2. In `verify(data, proof, root_hex)`: start with `h = H(data)`, then go up the proof: if the sibling is on the left, the parent is `H(sibling + h)`, otherwise `H(h + sibling)`. Compare the last `h` with the root.
3. Predict first: how many digests does a proof need for 8 files, 1024 files, one million files? One per level of the tree, `math.ceil(math.log2(n))`. Print the size of the proof (32 bytes per digest) and of a list of all `n` digests.

## Expected output

Your root, `True`, then the two checks of the dictionary, then three lines about proof sizes.

<details>
<summary>Check your answer</summary>

```
my root: 34e794e769407be83f9770594c5ba82db229c669b5f0a18a0f0cc9475cb56d76
the same as on Alice's website: True
Bob's spell-en.dat from an honest mirror: True
Mallory's spell-en.dat, the same proof:   False
        8 files: proof  3 digests =   96 bytes, a list of all digests        256 bytes
     1024 files: proof 10 digests =  320 bytes, a list of all digests      32768 bytes
  1000000 files: proof 20 digests =  640 bytes, a list of all digests   32000000 bytes
```

Mallory's file gives another leaf, so another parent, and so on up to another root. To make her file pass with some proof, she would need a second input that gives one of the digests on the path: a second preimage of SHA-256. The proof grows by one digest each time the number of files doubles: 20 digests (640 bytes) for a million files, instead of a list of 32 MB.

</details>

## Run

```
python3 merkle.py
```

Run it inside the `Task9` folder (it reads `release/`). About 10 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? The simulator: [ksawerym.github.io/Cryptography-simulators/hash/#7](https://ksawerym.github.io/Cryptography-simulators/hash/#7).
