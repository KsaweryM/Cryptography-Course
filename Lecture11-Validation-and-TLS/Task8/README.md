# Task 8: pins and renewals

## The situation

Bob's phone app talks only to `api.bob.example`. In 2026 he shipped the app with **pins**: a pin of the whole 2026 certificate, and two pins of public keys (SPKI pins): the key of the 2026 certificate and a backup key that he keeps offline and has never used. In December 2026 the certificate must be renewed. Bob has three options: a new certificate with the same key, one with a brand new key, or one with the backup key. Which of them will the app still accept?

![Bob's app from 2026 has pinned: a certificate pin, cert_pin(api_2026.pem), and two key pins, spki_pin(api_2026.pem) and 80E24poONJAEyvB/...u+I4=, a backup key kept in Bob's safe. Four certificates: api_2026.pem (January 2026, key 1), api_2027_same_key.pem (December 2026, key 1 again), api_2027_new_key.pem (December 2026, key 2), api_2027_backup_key.pem (December 2026, the backup key). For each: does the certificate pin match? Does a key pin match?](figure.svg)

## Goal

Compute certificate pins and key pins, and find which of the renewed certificates the app still accepts.

## Ready for you

- `pins_ready.py` (do not change it): `FILES`, the four certificate files, and `load_cert(filename)`.
- `certs/`: the four certificates of `api.bob.example`.
- `pins.py`: the pins of the app and the loop over the certificates.

## Steps

Write your code in place of the `TODO` comments in `pins.py`:

1. `cert_pin(cert)`: take the DER bytes of the whole certificate, `cert.public_bytes(serialization.Encoding.DER)`, hash them with SHA-256 and encode the 32 bytes in base64: `base64.b64encode(hashlib.sha256(der).digest()).decode()`.
2. `spki_pin(cert)`: the same, but only for the public key (the SubjectPublicKeyInfo):
   `cert.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)`.
3. In the loop: compare `cert_pin(cert)` with `APP_CERT_PIN`, and `spki_pin(cert)` with each pin in `APP_SPKI_PINS` (use an index loop). Print the file name and `match` or `NO` for each kind of pin.

**Predict first:** which of the three renewals pass the certificate pin? Which pass a key pin?

## Expected output

The app's pins on the first two lines, then one line per certificate.

<details>
<summary>Check your answer</summary>

```
app cert pin: YG8DPNekiK+QyyAVTSAYvpVlTXSPIcO51TvSbnO5GVE=
app key pins: ['/Bbx1A2gOvArfgXexc8HhPf+aZ1GbF9+OPlh0/gtaFQ=', '80E24poONJAEyvB/qmN1uvdylRrWLUT6ExA0k7hu+I4=']
api_2026.pem               cert pin: match  key pin: match
api_2027_same_key.pem      cert pin: NO     key pin: match
api_2027_new_key.pem       cert pin: NO     key pin: NO
api_2027_backup_key.pem    cert pin: NO     key pin: match
```

Every renewal breaks the certificate pin. A key pin survives a renewal with the same key, and the backup pin saves Bob when he must change the key (for example after a leak). With a new key that was never pinned, the app stops working until every user installs an update.

You can check a key pin with the same command as on the slides:

```
openssl x509 -in certs/api_2026.pem -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64
```

It prints `/Bbx1A2gOvArfgXexc8HhPf+aZ1GbF9+OPlh0/gtaFQ=`.

</details>

## Run

```
python3 pins.py
```

About 10 minutes. Python 3 and the `cryptography` library (version 41 or newer); works offline.
