# Task 5: X25519

## The situation

Alice and Bob want to chat with ChaCha20, so they need a shared 32-byte key, but they have never met and Eve reads everything on the network. They use X25519: ECDH on Curve25519, as in TLS 1.3 and Signal. Each has a 32-byte private key and sends only the public key. Each then combines their own private key with the other's public key, and both should get the same secret. HKDF turns that secret into the ChaCha20 key. The private keys here are the test values from RFC 7748, section 6.1, so you can compare your result with the standard.

![Alice and Bob, each with a 32-byte private key in amber: Alice's starts 77076d0a7318a57d and ends b177fba51db92c2a, Bob's starts 5dab087e624a8a4b and ends 1c2f8b27ff88e0eb. public_key turns each into a public key, "public A = ?" and "public B = ?", in violet; A goes to Bob and B to Alice, and Eve listens and sees A and B. x25519(private, B) on Alice's side and x25519(private, A) on Bob's side each give "secret = ?", with "= ?" between them. Alice's secret goes into hkdf with info b"lecture 5 chat key" and out comes "ChaCha20 key, 32 bytes = ?".](figure.svg)

## Goal

Agree on a shared secret as Alice and as Bob, check that both are the same, and derive a ChaCha20 key from it.

## Ready for you

- `x25519_ready.py` (RFC 7748 and RFC 5869, in plain Python):
  - `public_key(private)`: the public key, that is d × G on Curve25519. 32 bytes in, 32 bytes out.
  - `x25519(my_private, other_public)`: the shared secret, 32 bytes.
  - `hkdf(secret, info)`: a 32-byte key made from the secret; `info` is a label for what the key is for.
- `ecdh.py`: `alice_private` and `bob_private`, 32 bytes each. A `bytes` object is like a `const uint8_t[32]` in C.
- The printing at the end of `ecdh.py`: each line says `not done yet: TODO n` until its TODO is done. It prints the values with `.hex()` (the bytes as a hex string) and compares the two secrets with `==`, which compares two `bytes` objects byte by byte, like `memcmp(a, b, 32) == 0` in C.

## Steps

Write your code in place of the `None` after each `TODO` in `ecdh.py`:

1. The public keys: `alice_public = public_key(alice_private)` and `bob_public = public_key(bob_private)`.
2. The shared secret on both sides: Alice uses `x25519(alice_private, bob_public)`, Bob uses `x25519(bob_private, alice_public)`.
3. Derive the ChaCha20 key from Alice's secret: `key = hkdf(alice_secret, b"lecture 5 chat key")`. `b"..."` is a `bytes` literal.

## Expected output

The two public keys, the two secrets (the same 64 hex digits twice), `equal: True`, and the 32-byte key. Compare the secret with RFC 7748, section 6.1.

<details>
<summary>Check your answer</summary>

```
Alice's public key:  8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a
Bob's public key:    de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f
secret (Alice):      4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
secret (Bob):        4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
equal: True
ChaCha20 key:        8232af18b2d158a867dead920cb27b5f70409d17ef4712ba664eb4d2ff392f78
```

The public keys and the secret are exactly the values in RFC 7748, section 6.1. Your labels may differ; the hex values must not.

</details>

## Run

```
python3 ecdh.py
```

About 6 minutes. Python 3, no extra libraries.

Want to see it move? The [elliptic-curves simulator, step 1](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#1) runs the same exchange on the small curve mod 17 and, lower on the page, on P-256: change the secrets and watch both sides get the same point.
