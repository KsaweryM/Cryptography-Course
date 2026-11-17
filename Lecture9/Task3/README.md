# Task 3: Bob's certificate

## The situation

Trusty CA has checked that the Ed25519 key in `bob_public.pem` belongs to Bob Ltd, the owner of `bob.example`. Now it issues a real X.509 certificate: the issuer, the subject, a serial number, the validity dates and Bob's public key, all signed with the private key of Trusty CA.

![The certificate of bob.example as a card. The issuer C=GB, O=Trusty CA Ltd, CN=Trusty CA is ready. Step 1: the subject C=GB, O=Bob Ltd, CN=bob.example. Step 2: serial number 0x4F3A9C2E71D05B88, notBefore 2026-11-01 00:00:00 UTC, notAfter 2027-01-30 00:00:00 UTC and Bob's Ed25519 key. Step 3: the signature, builder.sign(ca_private, None), made with the private key of Trusty CA. Step 4: save to bob.pem and check the fingerprint E8:C5:56:C2:...](figure.svg)

## Goal

Build and sign the X.509 certificate of `bob.example`, save it to `bob.pem`, and check that its fingerprint matches the one below.

## Ready for you

- `cert_tools.py`: `load_private_key`, `load_public_key`, `save_cert(cert, path)` and `show(cert)`, which prints the main fields and the SHA-256 fingerprint.
- `trusty_ca_private.pem` (the key of Trusty CA) and `bob_public.pem` (Bob's public key), already loaded as `ca_private` and `bob_public`.
- The issuer name. A name (a DN) is a list of attributes; each is a type and a value:

```python
issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "GB"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Trusty CA Ltd"),
    x509.NameAttribute(NameOID.COMMON_NAME, "Trusty CA"),
])
```

## Steps

Write your code in place of the `TODO` comments in `make_cert.py`:

1. The subject: `C = GB`, `O = Bob Ltd`, `CN = bob.example`, in this order, written like `issuer`.
2. Fill in the other fields of `builder`, one call per field (each call returns a new builder, so write `builder = builder.xxx(...)`):
   `subject_name(subject)`, `serial_number(0x4F3A9C2E71D05B88)`,
   `not_valid_before(datetime.datetime(2026, 11, 1, tzinfo=UTC))`,
   `not_valid_after(datetime.datetime(2027, 1, 30, tzinfo=UTC))`, `public_key(bob_public)`.
3. Sign it as Trusty CA: `cert = builder.sign(ca_private, None)`. `None` means: no separate hash algorithm, because an Ed25519 key has its own.
4. Save it with `save_cert(cert, "bob.pem")` and print it with `show(cert)`.

## Expected output

The fields you put in (the names are printed CN first, as RFC 4514 writes a DN), and the fingerprint. The keys are fixed and Ed25519 adds no randomness, so everybody gets the same fingerprint.

<details>
<summary>Check your answer</summary>

```
version       v3
serial        0x4f3a9c2e71d05b88
issuer        CN=Trusty CA,O=Trusty CA Ltd,C=GB
subject       CN=bob.example,O=Bob Ltd,C=GB
not before    2026-11-01 00:00:00+00:00
not after     2027-01-30 00:00:00+00:00
public key    Ed25519
extensions    0
SHA-256 fingerprint
    E8:C5:56:C2:D8:3E:72:C3:FB:F0:53:83:64:04:97:A0:A6:72:48:1B:86:79:A6:F4:CB:82:B0:8E:11:71:F8:1C
```

A different fingerprint means one byte is different: usually a typo in a name or the attributes in another order.

</details>

## Run

```
python3 make_cert.py
openssl x509 -in bob.pem -noout -text
```

About 12 minutes. Python 3 and the library `cryptography` (version 41 or newer). The second command is optional: it shows the certificate as OpenSSL reads it.
