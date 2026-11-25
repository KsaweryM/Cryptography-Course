# Task 1: use ChaCha20

## The situation

ChaCha20 is a stream cipher, like RC4, but it has three inputs instead of one: a secret **key**, a public **nonce** and a **counter**. RFC 8439, the standard that defines ChaCha20, gives an example in section 2.4.2: a key, a nonce and a 114-byte ciphertext. Play Bob: you know the key, so you can read the message. For now ChaCha20 is a black box: you call it, you do not look inside.

![Four inputs go into the ChaCha20 black box: the key 00 01 02 to 1F (32 bytes, secret), the nonce 00 00 00 00 00 00 00 4A 00 00 00 00 (12 bytes, public), the counter 1 and the ciphertext 6E 2E 35 9A 25 68 F9 80 and so on (114 bytes). Out comes the message, 114 bytes, still unknown. The same call encrypts and decrypts.](figure.svg)

## Goal

Decrypt the message from RFC 8439 with one call to ChaCha20.

## Ready for you

- `chacha.py`: `chacha20(key, nonce, counter, data)` XORs `data` with the keystream of `key`, `nonce` and `counter`. So the same call encrypts and decrypts. The counter is the number of the first 64-byte block of keystream.
- `use_chacha.py`: the `key` (32 bytes: 00, 01, 02, ..., 1F), the `nonce` (12 bytes) and the `ciphertext` (114 bytes), copied from the RFC.

## Steps

Write your code in place of the `TODO` comments in `use_chacha.py`. Until TODO 1 is done, the file prints `not done yet: TODO 1`.

1. Decrypt the ciphertext with counter 1: `plaintext = chacha20(key, nonce, 1, ciphertext)`.
2. Print the message. `plaintext.decode()` turns the bytes into text.

## Expected output

One line: the message, 114 characters, in English.

<details>
<summary>Check your answer</summary>

```
Ladies and Gentlemen of the class of '99: If I could offer you only one tip for the future, sunscreen would be it.
```

</details>

## Run

```
python3 use_chacha.py
```

About 4 minutes. Python 3, no extra libraries.

Want to see it move? Type your own key, nonce and counter into the [ChaCha20 black box](https://ksawerym.github.io/Cryptography-simulators/chacha20/#1).
