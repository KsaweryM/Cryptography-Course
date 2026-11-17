# Task 4: one key, many messages

## The situation

You and a friend share one secret key, `our secret`, and want to send many messages with it. But RC4 has only one input, the key, so the same key always gives the same keystream: exactly the mistake of Task 3. The fix: before each message, make a new public value `n` and use `n + key` as the RC4 key. One secret, a new keystream every time.

![Step 1: the key our secret gives the same keystream B5 D0 D4 DF for both messages. Step 2: a new 3-byte value n, for example 3B 91 E4 or C7 05 6A, is glued in front of the key. Each n gives a different keystream, and the packet that is sent is n followed by the ciphertext c.](figure.svg)

## Goal

Write `encrypt` and `decrypt` that use one secret key but a different keystream for every message.

## Ready for you

- `rc4.py`: `rc4(key, data)` encrypts and decrypts (the same operation: XOR with the keystream).
- `one_key.py`: `xor(a, b)` XORs two byte strings, byte by byte.
- `one_key.py`: `attacker_learns_xor(p1, p2, m1, m2)`, a ready test for check d). It plays the attacker, who sees only the two packets.
- `one_key.py`: `key = b"our secret"`, `m1 = b"Meet at noon."`, `m2 = b"Bring the map"`.

## Steps

Write your code in place of the `TODO` comments in `one_key.py`.

**Step 1: the same key twice**

1. Encrypt both messages with the same key, `c1 = rc4(key, m1)` and `c2 = rc4(key, m2)`. Print:
   - `xor(c1, c2) == xor(m1, m2)`
   - `rc4(key, m1) == rc4(key, m1)` (the same message, sent twice)

   When is this dangerous?

**Step 2: a public value, new for every message**

2. Write `encrypt(key, m)`:
   - a) Make a new 3-byte value: `n = random.randbytes(3)`. It is not secret: it travels in the open.
   - b) The RC4 key for this message is `n + key` (`n` glued in front of the key): `c = rc4(n + key, m)`.
   - c) Return the packet that is sent: `n + c`.
3. Write `decrypt(key, packet)`:
   - a) `n` is the first 3 bytes of the packet, `c` is the rest.
   - b) The RC4 key is again `n + key`: return `rc4(n + key, c)`.
4. Check: make `p1 = encrypt(key, m1)` and `p2 = encrypt(key, m2)`, then print four lines:
   - a) `xor(p1[3:], p2[3:]) == xor(m1, m2)`: should be `False` (no shared keystream).
   - b) `encrypt(key, m1) != encrypt(key, m1)`: should be `True` (the same message looks different).
   - c) `decrypt(key, p1)`: should be `b'Meet at noon.'` (your friend can still read it).
   - d) `attacker_learns_xor(p1, p2, m1, m2)`: should be `False`.

Hints: `b"ab" + b"cd" == b"abcd"`. `packet[0:3]` is the first 3 bytes, `packet[3:]` the rest (like `packet + 3` in C).

## Expected output

Six lines: two from step 1, four from step 2. They are the same on every run, even though `n` is random.

```
True
True
False
True
b'Meet at noon.'
False
```

## Run

```
python3 one_key.py
```

About 6 minutes. Python 3.9 or newer (for `random.randbytes`), no extra libraries.
