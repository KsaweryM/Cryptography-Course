# Task 4: one key, many messages

**Goal:** you and a friend share one secret key, `our secret`, and you want to send many messages. Keep **one** secret key, but get a **different keystream** for every message.

**Ready:** `rc4.py`: `rc4(key, data)` encrypts and decrypts (the same operation). In `one_key.py`: `xor(a, b)` and `attacker_learns_xor(p1, p2, m1, m2)`, a ready test for check d).

## Step 1: the same key twice

1. Encrypt two messages with the same key, `c1 = rc4(key, m1)` and `c2 = rc4(key, m2)`, and print:
   - `xor(c1, c2) == xor(m1, m2)`
   - `rc4(key, m1) == rc4(key, m1)` (the same message, sent twice)

   When is this dangerous?

## Step 2: a public value, new for every message

Step 1 showed: one key gives one keystream. Now every message gets its own RC4 key.

2. Write `encrypt(key, m)`:
   1. Make a new 3-byte value: `n = random.randbytes(3)`. It does not have to be secret: it travels in the open.
   2. The RC4 key for this message is `n + key`: the 3 bytes of `n` glued in front of the secret key. Encrypt with it: `c = rc4(n + key, m)`.
   3. Return the packet that is sent: `n + c` (first the 3 bytes of `n`, then the ciphertext `c`).
3. Write `decrypt(key, packet)`:
   1. Take `n` from the first 3 bytes of the packet and the ciphertext `c` from the rest.
   2. The RC4 key is again `n + key`: return `rc4(n + key, c)`.
4. Check, print four lines:
   - a) `p1 = encrypt(key, m1)` and `p2 = encrypt(key, m2)`: `xor(p1[3:], p2[3:]) == xor(m1, m2)` should be `False` (no shared keystream).
   - b) `encrypt(key, m1)` twice: are the two packets different? Should be `True` (the same message looks different).
   - c) `decrypt(key, p1)` should be `b'Meet at noon.'` (your friend can still read it).
   - d) `attacker_learns_xor(p1, p2, m1, m2)` should be `False`. This function plays the attacker, who sees only the two packets and tries simple tricks to get `m1 XOR m2`.

Hints: `b"ab" + b"cd" == b"abcd"`, so `n + key` is `n` glued in front of `key`. `packet[0:3]` is the first 3 bytes, `packet[3:]` the rest.

## Run

```
python3 one_key.py
```

When everything is done, the program prints six lines:

```
True
True
False
True
b'Meet at noon.'
False
```

About 6 minutes. Python 3.9 or newer (for `random.randbytes`), no extra libraries.
