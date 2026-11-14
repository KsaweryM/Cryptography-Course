# Task 4: one key, many messages

You and a friend share one secret key, `our secret`, and you want to send many messages. `rc4.py` is ready: `rc4(key, data)` encrypts and decrypts. `xor(a, b)` and `attacker_learns_xor(p1, p2, m1, m2)` are ready in `one_key.py`.

**Step 1.**

1. Encrypt two messages with the same key and check:
   - `xor(c1, c2) == xor(m1, m2)`
   - `rc4(key, m1) == rc4(key, m1)` (the same message, sent twice)

When is this dangerous?

**Step 2.** Step 1 showed: one key gives one keystream. Goal: keep **one** secret key, but get a different keystream for every message.

2. Write `encrypt(key, m)`: make a new 3-byte value `n = random.randbytes(3)`. It does not have to be secret: it travels in the open. Use `n` with `rc4` so that it changes the keystream. Return the packet `n + c`: first `n`, then the ciphertext `c`.
3. Write `decrypt(key, packet)`: take `n` from the first 3 bytes, the ciphertext from the rest, and give back the message.
4. Check, print four lines:
   - a) `p1 = encrypt(key, m1)`, `p2 = encrypt(key, m2)`: the XOR of the ciphertext parts (`packet[3:]`) equals `xor(m1, m2)`? Should be `False`.
   - b) `encrypt(key, m1)` twice: are the two packets different? Should be `True`.
   - c) `decrypt(key, p1)` gives `b'Meet at noon.'`.
   - d) `attacker_learns_xor(p1, p2, m1, m2)` should be `False`. This function is ready in `one_key.py`: it plays the attacker, who sees only the two packets and tries simple tricks to get `m1 XOR m2`.

Hints: `rc4` takes only two things: `key` and `data`. `packet[0:3]` is the first 3 bytes, `packet[3:]` the rest. `b"ab" + b"cd" == b"abcd"`.

## Run

```
python3 one_key.py
```

Python 3.9 or newer (for `random.randbytes`), no extra libraries.
