# Task 2: a signed name card

## The situation

Alice wants Bob's public key, but Mallory sits on the network and can swap it for her own. A party that everybody trusts, the certificate authority Trusty CA, checks that the key is really Bob's and signs the card `name=bob.example;key=<Bob's key>`. Alice already has the public key of Trusty CA, so she can check the card. Can Mallory change it?

![Trusty CA (brown, with its private key) signs Bob's card: name=bob.example;key=2fa8b9a6...702e3c40, with the signature still unknown (steps 1 and 2). Below, Alice with the public key of Trusty CA checks the card (step 3). Mallory, with her key 456918eb...539d5bcb, tries two tricks: her key in the card with the CA signature (step 4), and her key with her own signature (step 5).](figure.svg)

## Goal

Play Trusty CA and sign Bob's card; play Alice and check it; then try both tricks of Mallory and see what Alice gets.

## Ready for you

- `signing.py`: digital signatures as a black box (Ed25519, from the library `cryptography`):
  - `sign(private_key, data)` returns the signature (64 bytes),
  - `verify(public_key, data, signature)` returns `True` or `False`,
  - `key_hex(public_key)` returns the 32 bytes of a public key as hex text.
- The keys, already loaded at the top of `name_card.py`: `ca_private`, `ca_public`, `bob_public`, `mallory_private`, `mallory_public`.

## Steps

Write your code in place of the `TODO` comments in `name_card.py`:

1. Make Bob's card: the bytes `b"name=bob.example;key="` followed by `key_hex(bob_public)`. `key_hex` gives text; `.encode()` turns text into bytes, and `+` joins two byte strings. Print it.
2. Trusty CA signs the card with its private key: `signature = sign(ca_private, card)`. Print `signature.hex()`.
3. Alice checks the card with the public key of Trusty CA: print `verify(ca_public, card, signature)`.
4. Mallory keeps the signature but puts her own key in the card: `fake = b"name=bob.example;key="` followed by `key_hex(mallory_public)`. Print what Alice gets for `fake` with the same `signature`.
5. Mallory signs `fake` with her own private key. Alice checks it as always, with the public key of Trusty CA. Print the result.

## Expected output

Your two keys, the card and the signature, then three lines: `True` for Bob's card, and a result for each trick of Mallory.

<details>
<summary>Check your answer</summary>

```
Bob's key:     2fa8b9a6b0d5878b924cb42b1188f4e5f12cf7aa0d6faa0f2d715304702e3c40
Mallory's key: 456918eb304833d3885ff5c8f8091b98ca67d882d81deeb5c2590cfb539d5bcb
card:          b'name=bob.example;key=2fa8b9a6b0d5878b924cb42b1188f4e5f12cf7aa0d6faa0f2d715304702e3c40'
signature:     5d034483ee304edd20c5d8652d973ff06104445dd771b3303fc46de25e17176e5acc643a5b7f657abe7e45d6f655791fce16aa808360631a4509d6b3c4043f0a
Bob's card, CA signature:         True
Mallory's key, CA signature:      False
Mallory's key, Mallory signature: False
```

Ed25519 signatures have no randomness, so your signature is exactly this one. Changing the card changes the signed bytes, so the old signature fails. Mallory's own signature fails because Alice always checks with the key of Trusty CA, not with a key from the card.

</details>

## Run

```
pip install cryptography
python3 name_card.py
```

About 12 minutes. Python 3 and the library `cryptography` (version 41 or newer). No internet needed after the install.
