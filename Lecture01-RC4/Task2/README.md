# Task 2: use RC4

## The situation

A one-time pad needs a key as long as the message. RC4 fixes that: from a short key it makes as many keystream bytes as you ask for. You received a 28-byte ciphertext, encrypted with RC4 and the key `Kangaroo`. For now RC4 is a black box: you call it, you do not look inside.

![The key Kangaroo goes into the RC4 black box, which gives the keystream 69 9D DA 7E FE 61 73 62 and so on. XOR with the ciphertext 24 F8 BF 0A DE 0C 16 42 gives the message, still unknown. Below, the key Kangarop, with the last letter changed, gives 8 unknown keystream bytes: how many stay the same?](figure.svg)

## Goal

Read the message, and see what one changed letter of the key does to the keystream.

## Ready for you

- `rc4.py`: `keystream(key, n)` returns `n` bytes of keystream for the key `key` (bytes). Example: `keystream(b"Kangaroo", 8)`.
- `use_rc4.py`: the key `key = b"Kangaroo"` and the `ciphertext` (28 bytes).

## Steps

Write your code in place of the `TODO` comments in `use_rc4.py`:

1. Make a keystream as long as the ciphertext: `ks = keystream(key, len(ciphertext))`. The program prints its length.
2. Decrypt: inside the ready loop, XOR ciphertext byte `i` with keystream byte `i`, turn the result into a character with `chr` and add it to `message`. The program prints the message.
3. Print `keystream(key, 8)` and `keystream(b"Kangarop", 8)` in hex, one line each, in place of `print("not done yet: TODO 3")`. How many bytes are the same?

Until a step is done, the program prints `not done yet: TODO n` for it.

Hint: `data.hex(" ")` prints bytes in hex with spaces, for example `69 9d da`.

## Expected output

Four lines: the length, the message, then the two keystreams.

<details>
<summary>Check your answer</summary>

```
28
Meet me at the library at 5.
69 9d da 7e fe 61 73 62
97 c5 8c ab f1 d1 2e 8d
```

</details>

## Run

```
python3 use_rc4.py
```

About 5 minutes. Python 3, no extra libraries.

Want to see it move? After the task, type your own key and text into the [RC4 black box](https://ksawerym.github.io/Cryptography-simulators/rc4/#1).
