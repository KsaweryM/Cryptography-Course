# Task 1: ECDH as a black box

## The situation

In Lecture 4, Alice and Bob agreed on a secret with Diffie-Hellman: each picked a random secret, sent one public number and computed the same shared number, 256 bytes long. Now they do the same with points of a curve, using X25519: ECDH on the curve Curve25519, as in HTTPS and Signal. You do not need to know yet what happens inside: `public_key` and `x25519` are the black box. Eve reads everything on the network, so she sees both public keys.

![Alice and Bob, each with a private key "32 random bytes = ?" in amber, made by secrets.token_bytes(32). public_key turns each into a public key, "public A = ?" and "public B = ?", in violet; A goes to Bob and B to Alice, and Eve listens and sees A and B. x25519(private, B) on Alice's side and x25519(private, A) on Bob's side each give "secret = ?", with "= ?" between them. Below, a bar of 256 bytes labelled "the shared secret of Diffie-Hellman, Lecture 4" and a short bar labelled "the shared secret of X25519: ? bytes".](figure.svg)

## Goal

Make a key pair for Alice and one for Bob, compute the shared secret on both sides, check that both are the same, and compare its size with the 256 bytes of Lecture 4.

**Predict first:** run the file twice. Will the shared secret be the same both times?

## Ready for you

- `x25519_ready.py` (RFC 7748, in plain Python; you do not need to read it):
  - `public_key(private)`: the public key, a point of Curve25519 made from the private key. 32 bytes in, 32 bytes out.
  - `x25519(my_private, other_public)`: the shared secret, 32 bytes.
- `ecdh.py`: the printing at the end. Each line says `not done yet: TODO n` until its TODO is done. It prints the values with `.hex()` (the bytes as a hex string) and compares the two secrets with `==`, which compares two `bytes` objects byte by byte, like `memcmp(a, b, 32) == 0` in C. `len(x)` is the number of bytes, like `sizeof` of an array in C.

## Steps

Write your code in place of the `TODO` comments in `ecdh.py`:

1. The private keys: `alice_private = secrets.token_bytes(32)` and the same for `bob_private`. `token_bytes(32)` gives 32 random bytes, like reading 32 bytes from `/dev/urandom` into a `uint8_t[32]` in C.
2. The public keys: `alice_public = public_key(alice_private)` and `bob_public = public_key(bob_private)`. Alice sends hers to Bob, Bob sends his to Alice.
3. The shared secret on both sides: Alice computes `alice_secret = x25519(alice_private, bob_public)` (her private key, Bob's public key), Bob computes `bob_secret = x25519(bob_private, alice_public)`.

Then run the program twice.

## Expected output

The two private keys, the two public keys, the two secrets, then `equal: True` and the size of the secret. The keys are random, so all the hex values are new on every run; `equal: True` and the size are always the same.

<details>
<summary>Check your answer</summary>

```
Alice's private key: e238b846cba5bd8d33283b1fbb359f85c0fdcc2a53359552ca8be580f86965f6
Bob's private key:   47ed642534e8188780f91f1c7242c22191780d8f226d39d1b07ec9779a283715
Alice's public key:  8e4ee193e7e2c4db4b496c7caa57c854f4801f62dffca7b7392b4e5b78bd9017
Bob's public key:    c8b2a21974bc3b23d6591db26461af235a2fe86437359abaebef58493b3cf276
secret (Alice):      4dba73139a4111d89d66989e803c9f486ad21614094c10e2bee05d660f006472
secret (Bob):        4dba73139a4111d89d66989e803c9f486ad21614094c10e2bee05d660f006472
equal: True
size of the secret: 32 bytes (Diffie-Hellman in Lecture 4: 256 bytes)
```

Your hex values differ (the keys are random), but both secrets are always the same, and the secret is 32 bytes: 8 times shorter than the Diffie-Hellman secret of Lecture 4 (and for the same security as X25519, Diffie-Hellman would even need 3072 bits, 384 bytes). Each public key is 32 bytes too.

</details>

## Run

```
python3 ecdh.py
```

About 5 minutes. Python 3, no extra libraries.

Want to see it move? The [elliptic-curves simulator, step 1](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#1) runs the same exchange on a small curve: change the secrets and watch both sides get the same point.
