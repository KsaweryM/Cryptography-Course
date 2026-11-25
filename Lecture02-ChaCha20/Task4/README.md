# Task 4: change one byte

## The situation

Alice sends Bob the message `Pay Bob 100`, sealed with ChaCha20-Poly1305. The packet is the ciphertext (11 bytes) followed by a 16-byte **tag**. Mallory sits between them. She has no key, but she can change bytes on the way: she flips one bit of byte 5. Bob recomputes the tag from what arrived and compares it with the tag in the packet. Predict first: what does Bob read without the tag check, and what does `open_` do with it?

![Alice sends a packet, Mallory changes it, Bob receives it. Alice's packet: the ciphertext 4C EA 76 9D 37 9F 55 B9 D7 A3 5A of "Pay Bob 100" and the tag 0E E9 C8 47 ... 30 71. Mallory changes byte 5: 9F XOR 01 = 9E, and leaves the tag as it is. Bob recomputes the tag from the ciphertext that arrived, with the secret key: the result is unknown. Is it equal to the tag in the packet? What does open_ do with this packet?](figure.svg)

## Goal

Seal a message, change one byte of the packet, and see what Bob reads without the tag and with it. Then change only the header (the associated data) and try again.

## Ready for you

- `aead.py`: ChaCha20-Poly1305 as two functions, and plain ChaCha20. Treat it as a black box.
  - `seal(key, nonce, plaintext, aad=b"")` encrypts and returns the packet: the ciphertext and the 16-byte tag.
  - `open_(key, nonce, packet, aad=b"")` checks the tag and returns the plaintext, or raises `ValueError` if the packet was changed. `open_` has an underscore because `open` is already a Python function.
  - `aad` is the **associated data**: a header that is sent in the clear (for example who the message is for) but is protected by the tag. Bob must pass the same `aad` to `open_`.
  - `chacha20(key, nonce, counter, data)`: the cipher alone, without the tag. `seal` encrypts from counter 1.
- `tamper.py`: the `key` and the `nonce`, and the printing of the results.

## Steps

Write your code in place of the `TODO` comments in `tamper.py`. Each line of the output says `not done yet` until its TODO is done.

1. Seal the message: `packet = seal(key, nonce, b"Pay Bob 100")`.
2. Play Mallory: make a copy and flip one bit of byte 5. `bytes` cannot be changed, like a `const` array in C, so copy it first: `changed = bytearray(packet)`, then `changed[5] ^= 1`.
3. Without the tag: decrypt only the ciphertext part with `chacha20(key, nonce, 1, ...)`. `changed[:-16]` is everything except the last 16 bytes (the tag), like the first `len - 16` bytes in C.
4. With the tag: try `open_(key, nonce, changed)`. A Python function reports an error by raising an exception, not by returning an error code. Catch it like this:

   ```python
   try:
       plaintext = open_(key, nonce, changed)
       result = "opened: " + str(plaintext)
   except ValueError as e:
       result = "open_ raises: " + str(e)
   ```

5. Associated data: seal `b"Pay Bob 100"` again with `aad=b"to: Bob"`. Mallory leaves the ciphertext and the tag alone and only changes the header: open the same packet with `aad=b"to: Eve"`. Store the outcome in `result_aad`, as in step 4.

## Expected output

Five lines: the packet, the changed packet, what Bob would read without the tag, and what `open_` says twice.

<details>
<summary>Check your answer</summary>

```
packet:    4cea769d379f55b9d7a35a | tag 0ee9c847aa0230779088410523333071
changed:   4cea769d379e55b9d7a35a | tag 0ee9c847aa0230779088410523333071
without the tag Bob reads: b'Pay Bnb 100'
with the tag: open_ raises: bad tag: message rejected
header changed: open_ raises: bad tag: message rejected
```

Without the tag, the change passes unseen: Bob reads `Pay Bnb 100`. With the tag, nothing is decrypted. The header is not encrypted, but a changed header is caught in the same way.

</details>

## Run

```
python3 tamper.py
```

About 7 minutes. Python 3, no extra libraries.

Want to see it move? The [Poly1305 step of the ChaCha20 explorer](https://ksawerym.github.io/Cryptography-simulators/chacha20/#7) builds a tag chunk by chunk and shows what one changed byte does to it.
