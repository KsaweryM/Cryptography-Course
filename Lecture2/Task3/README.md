# Task 3: change one byte

## The situation

Alice sends Bob the message `Pay Bob 100`, sealed with ChaCha20-Poly1305. The packet is the ciphertext (11 bytes) followed by a 16-byte **tag**. Mallory sits between them. She has no key, but she can change bytes on the way: she flips one bit of byte 5. Without the tag, Bob would decrypt a changed message and never know. With the tag, Bob recomputes it from what arrived and compares.

![Alice sends a packet, Mallory changes it, Bob receives it. Alice's packet: the ciphertext 4C EA 76 9D 37 9F 55 B9 D7 A3 5A of "Pay Bob 100" and the tag 0E E9 C8 47 ... 30 71. Mallory changes byte 5: 9F XOR 01 = 9E, and leaves the tag as it is. Bob recomputes the tag from the ciphertext that arrived and gets A7 90 CE 91 ... 79 28, which is not equal to the tag. What does open_ do with this packet?](figure.svg)

## Goal

Seal a message, change one byte of the packet, then try to open it.

## Ready for you

- `aead.py`: ChaCha20-Poly1305 as two functions. Treat it as a black box.
  - `seal(key, nonce, plaintext)` encrypts and returns the packet: the ciphertext and the 16-byte tag.
  - `open_(key, nonce, packet)` checks the tag and returns the plaintext, or raises `ValueError` if the packet was changed. `open_` has an underscore because `open` is already a Python function.
- `tamper.py`: the `key` and the `nonce`.

## Steps

Write your code in place of the `TODO` comments in `tamper.py`:

1. Seal the message: `packet = seal(key, nonce, b"Pay Bob 100")`.
2. Play Mallory: flip one byte of the packet, for example XOR byte 5 with 1.
3. Try `open_(key, nonce, packet)` and print what happens.

Hints:

- `bytes` cannot be changed, like a `const` array in C. Make a copy you can change, then change one byte:
  `packet = bytearray(packet)`, then `packet[5] ^= 1`.
- A Python function reports an error by raising an exception, not by returning an error code. Catch it like this:

```python
try:
    open_(key, nonce, packet)
except ValueError as e:
    print("open_ raises:", e)
```

## Expected output

One line: `open_` rejects the packet and decrypts nothing.

<details>
<summary>Check your answer</summary>

```
open_ raises: bad tag: message rejected
```

Without the tag, the same change would pass unseen: Bob would read `Pay Bnb 100`.

</details>

## Run

```
python3 tamper.py
```

About 5 minutes. Python 3, no extra libraries.
