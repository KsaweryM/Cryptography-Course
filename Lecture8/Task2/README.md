# Task 2: sign and verify

## The situation

Alice tells Bob that their meeting moves to Friday 10:00 and signs the message with her Ed25519 private key. Bob has Alice's public key. Mallory changes 10:00 to 11:00 on the way, and then tries to sign the changed message herself, with her own private key.

![Alice's private key and the message "Bob, the meeting is moved to Friday 10:00. Alice" go into sign, out comes a signature of 64 bytes = ?. Bob runs verify with Alice's public key on: the message, the message with 11:00, and Mallory's signature on the message with 11:00, made with Mallory's private key. Each result: ?](figure.svg)

## Goal

Sign a message with Ed25519 and check it; see what verify says for a changed message and for a signature from another key; sign the same message twice and compare.

## Ready for you

- `signing.py` (the library `cryptography`, Ed25519; the same module as in Lecture 9):
  - `sign(private_key, data)`: the signature, 64 bytes.
  - `verify(public_key, data, signature)`: `True` or `False`. Inside, the library raises an exception for a wrong signature; `signing.py` turns it into `False`.
  - `load_private_key(path)`, `load_public_key(path)`: read a key from a PEM file (a text file with the key in base64).
- `sign_and_verify.py`: the keys of Alice and Mallory, `message` and `changed` (as `bytes`, like a `const uint8_t[]` in C).

## Steps

Write your code in place of the `None` after each `TODO` in `sign_and_verify.py`:

1. Alice signs `message` with `alice_private`.
2. Bob checks `message` and the signature with `alice_public`.
3. Bob checks `changed` with the same signature.
4. Mallory signs `changed` with `mallory_private`; Bob checks that signature with `alice_public`.
5. Alice signs `message` again. Compare the two signatures with `==` (like `memcmp` in C).

Before step 5, predict: will the second signature be the same?

## Expected output

The signature as 128 hex digits, then four lines with `True` or `False`.

<details>
<summary>Check your answer</summary>

```
signature: 64 bytes
eb232a684f057336cd2780944693c1992e27bda5f6a383416f4a1caa2739a8b54298b02954b5a4d43f647beaf3f1163e3fdea3aa7241cc9a95fcdf85a69d7f06
Bob checks the message:           True
Bob checks the changed message:   False
Bob checks Mallory's signature:   False
the second signature is the same: True
```

Ed25519 is deterministic: the same key and message always give the same signature, so your hex must be exactly this one. One changed character gives `False`; a signature made with Mallory's key does not fit Alice's public key.

</details>

## Run

```
pip install cryptography      # once, if it is not installed
python3 sign_and_verify.py
```

About 10 minutes. Python 3 and the library `cryptography`.
