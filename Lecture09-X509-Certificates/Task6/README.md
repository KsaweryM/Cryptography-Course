# Task 6: a self-signed certificate

## The situation

Alice runs a test server, `www.alice.example`, and has no CA. She makes a self-signed certificate: the issuer and the subject are the same name, and she signs it with her own private key. Its signature can be checked with the public key inside the same certificate. Mallory tries two tricks: she puts her own key into Alice's certificate, and she makes her own self-signed certificate with Alice's name.

![Three certificate cards, all with issuer = subject = CN=www.alice.example. Alice's certificate: Alice's key, signed with Alice's private key, verify? (steps 1 to 3). Mallory swaps the key: Mallory's key, still signed with Alice's private key, verify? (step 4). Mallory's own: Mallory's key, signed with Mallory's private key, verify? (step 5).](figure.svg)

## Goal

Make Alice's self-signed certificate and check its signature with its own key. Then try both tricks of Mallory. What does a good signature on a self-signed certificate prove?

## Ready for you

- `cert_tools.py`: `load_private_key(path)` and `make_cert(subject, issuer, public_key, signing_key)`, which builds and signs a certificate as in Task 3 (serial number and dates are fixed).
- `signing.py`: `verify(public_key, data, signature)` returns `True` or `False`.
- `alice_private.pem` and `mallory_private.pem`, loaded as `alice_private` and `mallory_private`; the name `name` (`CN=www.alice.example`); the raw 32-byte public keys `alice_raw` and `mallory_raw`.

## Steps

Write your code in place of the `TODO` comments in `self_signed.py`:

1. Make Alice's certificate: the subject and the issuer are both `name`, the public key is `alice_private.public_key()`, and `alice_private` signs it.
2. Print the subject and the issuer (`.rfc4514_string()`) and whether they are equal (`==`).
3. Write `check(cert)`: verify the signature of `cert` with the public key inside the same `cert`. The signed bytes are `cert.tbs_certificate_bytes`, the signature is `cert.signature`, the key is `cert.public_key()`.
4. Mallory puts her key into Alice's certificate: `der = bytearray(cert.public_bytes(serialization.Encoding.DER))`, `pos = der.find(alice_raw)`, then copy the 32 bytes of `mallory_raw` over `der[pos]` to `der[pos + 31]` in a loop. Load the result with `x509.load_der_x509_certificate(bytes(der))` and print `check()` of it.
5. Mallory makes her own self-signed certificate with the same `name`, her public key and her private key. Print `check()` of it.

## Expected output

The subject and issuer (equal), then three results: Alice's certificate, the one with the swapped key, and Mallory's own.

<details>
<summary>Check your answer</summary>

```
subject: CN=www.alice.example
issuer:  CN=www.alice.example
issuer == subject: True
Alice's certificate, signature OK: True
Mallory's key in Alice's certificate (at byte 132 ), signature OK: False
Mallory's own certificate for www.alice.example, signature OK: True
```

Swapping the key changes the signed bytes, so the check fails. But Mallory's own certificate passes: it has the same name, and its signature is correct for the key inside it. A good signature on a self-signed certificate only proves that whoever made it has the matching private key. It says nothing about who owns the name; that trust must come from outside (a CA, or a fingerprint you checked).

</details>

## Run

```
python3 self_signed.py
```

About 10 minutes. Python 3 and the library `cryptography` (version 41 or newer).
