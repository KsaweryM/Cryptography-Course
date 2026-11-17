# Task 4: audit Carol's certificates

## The situation

Carol looks after the servers of Carol Corp. Last month a web server went down for a day: its certificate had expired and nobody was watching it. Carol collected every certificate she could find into the folder `certs/`. Now she wants a script that checks them all on the audit day, 2026-12-01, against three rules: renew when fewer than 30 days are left, no MD5 or SHA-1 in the CA's signature, and RSA keys of at least 2048 bits.

![Carol, audit day 2026-12-01, and her folder certs/ with eight certificate cards, each with a question mark. api.pem: key EC 384, CA hash sha256, expires 2026-12-24. build.pem: Ed25519, sha256, 2027-07-01. camera.pem: RSA 2048, md5, 2028-10-15. intranet.pem: RSA 1024, sha1, 2030-02-27. mail.pem: RSA 2048, sha256, 2026-12-12. printer.pem: RSA 2048, sha256, 2026-10-03. vpn.pem: RSA 3072, sha256, 2027-02-20. www.pem: EC 256, sha256, 2027-04-30. Which certificates break a rule?](figure.svg)

## Goal

Print, for every certificate, how many days are left and which rules it breaks; count the problems.

## Ready for you

- `certinfo.py`: `load_folder(folder)` returns a list of `(file name, certificate)`; `expires(cert)` the end of the validity period; `key_info(cert)` a pair such as `("RSA", 2048)`; `hash_name(cert)` the hash in the CA's signature, such as `"sha256"`; `subject_cn(cert)` and `issuer_cn(cert)` the names.
- In `audit.py`: `TODAY`, `RENEW_DAYS = 30`, `WEAK_HASHES = ["md5", "sha1"]`, `MIN_RSA_BITS = 2048`, and the loop that prints one line per certificate.

## Steps

Write your code in place of the `TODO` comments in `audit.py`, inside the loop:

1. `days_left = (expires(cert) - TODAY).days`: subtracting two dates gives a time difference, and `.days` is its number of whole days. Print it.
2. If `days_left < 0`: print `EXPIRED`; else if `days_left < RENEW_DAYS`: print `RENEW NOW`. (`elif` is C's `else if`.)
3. If `hash_name(cert) in WEAK_HASHES`: print `WEAK HASH`. (`x in list` is a loop that looks for `x`.)
4. If the key is `"RSA"` and has fewer than `MIN_RSA_BITS` bits: print `WEAK KEY`. Add 1 to `problems` for every rule broken.

## Expected output

Eight certificates; five of them break at least one rule.

<details>
<summary>Check your answer</summary>

```
api.pem        api.carol-corp.example       EC        384 sha256  from Trusty CA
  days left: 23
  RENEW NOW
build.pem      build.carol-corp.example     Ed25519   256 sha256  from Carol Corp Internal CA
  days left: 212
camera.pem     camera.carol-corp.example    RSA      2048 md5     from camera.carol-corp.example
  days left: 684
  WEAK HASH
intranet.pem   intranet.carol-corp.example  RSA      1024 sha1    from intranet.carol-corp.example
  days left: 1184
  WEAK HASH
  WEAK KEY
mail.pem       mail.carol-corp.example      RSA      2048 sha256  from Trusty CA
  days left: 11
  RENEW NOW
printer.pem    printer.carol-corp.example   RSA      2048 sha256  from Carol Corp Internal CA
  days left: -59
  EXPIRED
vpn.pem        vpn.carol-corp.example       RSA      3072 sha256  from Carol Corp Internal CA
  days left: 81
www.pem        www.carol-corp.example       EC        256 sha256  from Trusty CA
  days left: 150
6 problems in 8 certificates
```

Six problems in five certificates. The camera and the intranet are self-signed (issuer = subject) and valid for years: long life and weak algorithms often come together on old devices. The key size rule is only for RSA: an EC key of 256 bits is as strong as RSA with about 3072 bits.

</details>

## Run

```
python3 audit.py
```

About 12 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
