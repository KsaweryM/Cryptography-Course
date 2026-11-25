# Task 7: from a shared secret to keys

## The situation

Alice and Bob have done the X25519 exchange (the same steps as in Task 1) and share a 32-byte secret. Now they want to chat with ChaCha20. They do not use the secret itself as the key: HKDF turns it into keys. First one ChaCha20 key, then two keys, one for each direction, so that Alice and Bob never encrypt with the same key and nonce. Each side derives the keys on its own, and they never send a key over the network. The private keys here are the test values from RFC 7748, section 6.1, so you can compare the shared secret with the standard. At the end, Mallory joins in: she sends Alice 32 zero bytes in place of Bob's public key, and you write the check that stops her.

![Alice and Bob, each with the same shared secret in amber, 4a5d9d5ba4ce2de1... 3376f09b3c1e161742, from x25519 (ready). On Alice's side the secret goes into hkdf with info b"lecture 5 chat key" and out comes "ChaCha20 key = ?". Below, on both sides, the secret goes into hkdf twice, with info b"Alice to Bob" and b"Bob to Alice", and out come "key Alice to Bob = ?" and "key Bob to Alice = ?". Between the two keys on Alice's side: "different?"; between Alice's and Bob's keys: "the same?". Nothing goes over the network.](figure.svg)

## Goal

Derive a ChaCha20 key from the shared secret, then two different keys, one per direction, on Alice's side and on Bob's side, and check that both sides get the same two keys. Then see what a public key of small order does to the secret, and refuse it.

## Ready for you

- `x25519_ready.py` (RFC 7748 and RFC 5869, in plain Python):
  - `public_key(private)` and `x25519(my_private, other_public)`: the exchange of Task 1.
  - `hkdf(secret, info)`: a 32-byte key made from the secret; `info` is a label for what the key is for.
- `derive_keys.py`: the exchange is done. `alice_secret` and `bob_secret` are the shared secret, 32 bytes, computed on each side. A `bytes` object is like a `const uint8_t[32]` in C.
- The printing at the end of `derive_keys.py`: each line says `not done yet: TODO n` until its TODO is done. It compares keys with `==` and `!=`, which compare two `bytes` objects byte by byte, like `memcmp` in C.

## Steps

Write your code in place of the `None` after each `TODO` in `derive_keys.py`:

1. One ChaCha20 key from Alice's secret: `key = hkdf(alice_secret, b"lecture 5 chat key")`. `b"..."` is a `bytes` literal.
2. One secret, two keys: `alice_key_to_bob = hkdf(alice_secret, b"Alice to Bob")` and `alice_key_from_bob = hkdf(alice_secret, b"Bob to Alice")`. Alice encrypts with the first key, Bob with the second. The only difference is the label `info`.
3. Bob does the same on his side, with his own secret: `bob_key_from_alice = hkdf(bob_secret, b"Alice to Bob")` and `bob_key_to_alice = hkdf(bob_secret, b"Bob to Alice")`.
4. Mallory changes Bob's public key on the way: Alice receives `mallory_public`, 32 zero bytes. This is a point of small order: a few additions bring it back to O.
   - a) `mallory_secret = x25519(alice_private, mallory_public)`. Predict first: what does Mallory need to know to compute this secret too?
   - b) Write `is_all_zero(secret)`: a `for i in range(len(secret))` loop that returns `False` at the first byte that is not 0, and `True` after the loop. `secret[i]` is one byte as a number, like `secret[i]` on a `uint8_t *` in C. TLS 1.3 makes this check after every X25519 exchange and stops the connection when it is `True`.

## Expected output

The shared secret, the ChaCha20 key, Alice's two keys and `different: True`, then Bob's two keys and `the same on both sides: True`, then the secret made with Mallory's key and the result of the check. Compare the secret with RFC 7748, section 6.1.

<details>
<summary>Check your answer</summary>

```
shared secret:             4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
ChaCha20 key:              8232af18b2d158a867dead920cb27b5f70409d17ef4712ba664eb4d2ff392f78
key Alice to Bob (Alice):  ebc98d3d10432aec017fa08fc2100ee93ef249f8ca6635e3bd6569aa6fb36a67
key Bob to Alice (Alice):  a187bf5005903e5b1b59498cf8cc53c6ec7f90618b31773f84ca91bd9804edcf
different: True
key Alice to Bob (Bob):    ebc98d3d10432aec017fa08fc2100ee93ef249f8ca6635e3bd6569aa6fb36a67
key Bob to Alice (Bob):    a187bf5005903e5b1b59498cf8cc53c6ec7f90618b31773f84ca91bd9804edcf
the same on both sides: True
secret with Mallory's key:  0000000000000000000000000000000000000000000000000000000000000000
all zero, refused: True | real secret refused: False
```

The secret is exactly the value in RFC 7748, section 6.1. The three keys come from the same secret and differ only in the label: change one letter of a label and the key changes completely. Bob gets the same two keys as Alice, because the same secret with the same label always gives the same key.

With Mallory's key the secret is 32 zero bytes, whatever Alice's private key is: Mallory knows it without any private key, and every key HKDF makes from it. A real secret is never all zero, so the check refuses only the attack.

</details>

## Run

```
python3 derive_keys.py
```

About 8 minutes. Python 3, no extra libraries.

Want to see it move? The [elliptic-curves simulator, step 1](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#1.1) runs the exchange on the small curve mod 17 and, lower on the page, on P-256: change the secrets and watch both sides get the same point.
