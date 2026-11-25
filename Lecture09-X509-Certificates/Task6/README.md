# Task 6: a self-signed certificate

## The situation

Alice runs a test server, `www.alice.example`, and has no CA. She makes a self-signed certificate: the issuer and the subject are the same name, and she signs it with her own private key. Its signature can be checked with the public key inside the same certificate. Mallory makes her own self-signed certificate with Alice's name. Bob wants to connect to Alice's server: which certificate is Alice's? Alice has read out to Bob on the phone the SHA-256 fingerprint of her certificate (idea 3 of Task 1).

![Two certificate cards, both with issuer = subject = CN=www.alice.example. Alice's certificate: Alice's key, signed with Alice's private key, verify? (steps 1 to 3). Mallory's own: Mallory's key, signed with Mallory's private key, verify? (step 4). Under each: fingerprint = ALICE_FP? Below: Alice phones Bob and reads out ALICE_FP = 6F:4B:D6:04:C8:F5:0B:73:... (step 5).](figure.svg)

## Goal

Make Alice's self-signed certificate and check its signature with its own key. Do the same for Mallory's certificate. What does a good signature on a self-signed certificate prove, and what does the fingerprint add?

## Ready for you

- `cert_tools.py`: `load_private_key(path)`, `make_cert(subject, issuer, public_key, signing_key)`, which builds and signs a certificate as in Task 3 (serial number and dates are fixed), and `colon_hex(data)`, which prints bytes as hex with `:` between them.
- `signing.py`: `verify(public_key, data, signature)` returns `True` or `False`.
- In `self_signed.py`: `alice_private` and `mallory_private` (from `alice_private.pem` and `mallory_private.pem`), the name `name` (`CN=www.alice.example`), the fingerprint `ALICE_FP` that Bob got on the phone, and the printing of the results.

## Steps

Write your code in place of the `TODO` comments in `self_signed.py`:

1. Make Alice's certificate: the subject and the issuer are both `name`, the public key is `alice_private.public_key()`, and `alice_private` signs it.
2. Print the subject and the issuer (`.rfc4514_string()`) and whether they are equal (`==`).
3. Write `check(cert)`: verify the signature of `cert` with the public key inside the same `cert`. The signed bytes are `cert.tbs_certificate_bytes`, the signature is `cert.signature`, the key is `cert.public_key()`.
4. Mallory makes her own self-signed certificate: the same `name`, her public key, signed with her private key.
5. Bob compares fingerprints: for each of the two certificates compute `colon_hex(cert.fingerprint(hashes.SHA256()))` and compare it with `ALICE_FP` (`==`).

Predict first: will Mallory's certificate pass `check()`?

## Expected output

The subject and issuer (equal), then `check()` of both certificates, then the two fingerprint comparisons.

<details>
<summary>Check your answer</summary>

```
subject: CN=www.alice.example
issuer:  CN=www.alice.example
issuer == subject: True
Alice's certificate, signature OK:   True
Mallory's certificate, signature OK: True
Alice's certificate, fingerprint = ALICE_FP:   True
Mallory's certificate, fingerprint = ALICE_FP: False
```

Mallory's certificate passes the signature check: it has the same name, and its signature is correct for the key inside it. A good signature on a self-signed certificate only proves that whoever made it has the matching private key. It says nothing about who owns the name. Trust must come from outside: here the fingerprint that Bob got on the phone, which Mallory does not control, tells the two certificates apart. A CA (Lecture 10) does the same for millions of certificates.

</details>

## Run

```
python3 self_signed.py
```

About 10 minutes. Python 3 and the library `cryptography` (version 41 or newer).
