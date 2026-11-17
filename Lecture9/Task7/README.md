# Task 7: two real certificates

## The situation

`coventry.pem` and `bbc.pem` are the real certificates of www.coventry.ac.uk and www.bbc.co.uk, saved on 15 November 2026 with

```
openssl s_client -connect www.coventry.ac.uk:443 -servername www.coventry.ac.uk < /dev/null > out.txt
```

(and the same for www.bbc.co.uk), keeping the first certificate. No internet is needed for the task. The sites get new certificates every few weeks, so what they send today is probably newer.

![Two certificate cards. coventry.pem: subject CN=www.coventry.ac.uk, issuer WE1 (Google Trust Services), key EC P-256. bbc.pem: subject CN=www.bbc.com, O=BRITISH ..., C=GB, issuer GlobalSign GCC R46 OV TLS CA 2025, key RSA 2048. On both: days valid? SAN: ? names. Below, five names with a question mark each: www.coventry.ac.uk, coventry.ac.uk, www.bbc.co.uk, news.bbc.co.uk, sport.bbc.co.uk. Step 3: covers(cert, host): is host one of the DNS names in the SAN?](figure.svg)

## Goal

Read the two certificates: who they belong to, who issued them, for how many days, and which names they cover.

Predict first: does the university's certificate cover `coventry.ac.uk`, without `www.`?

## Ready for you

- `coventry.pem`, `bbc.pem`.
- `cert_tools.py`: `load_cert`, `valid_from(cert)` and `valid_until(cert)` (dates in UTC), `find_extension(cert, kind)`, `key_name(public_key)` (for example `EC P-256`), `oid_name(oid)`.
- In `read_real.py`: the loop over the two files, which already prints the key and the signature algorithm.

## Steps

Write your code in place of the `TODO` comments in `read_real.py`:

1. Print the subject and the issuer (`.rfc4514_string()`).
2. Print how many days the certificate is valid: `(valid_until(cert) - valid_from(cert)).days`.
3. Write `covers(cert, host)`: `san = find_extension(cert, x509.SubjectAlternativeName)`, `names = san.get_values_for_type(x509.DNSName)`, then loop over `names` with an index and return `True` if one of them `== host`, otherwise `False`.
4. In the loop over the files: print how many DNS names the SAN has, and the first three of them.
5. After the loop: for every host in `hosts` and every certificate, print the result of `covers()`.

## Expected output

For each certificate: subject, issuer, dates, days, key, signature algorithm, the SAN count; then a table of `True` and `False`.

<details>
<summary>Check your answer</summary>

```
== coventry.pem
   subject:   CN=www.coventry.ac.uk
   issuer:    CN=WE1,O=Google Trust Services,C=US
   valid:     2026-10-13 02:29:16+00:00 to 2027-01-11 03:29:14+00:00
   days:      90
   key:       EC P-256
   signature: ecdsa-with-SHA256
   SAN names: 1 ['www.coventry.ac.uk']
== bbc.pem
   subject:   CN=www.bbc.com,O=BRITISH BROADCASTING CORPORATION,L=London,ST=London,C=GB
   issuer:    CN=GlobalSign GCC R46 OV TLS CA 2025,O=GlobalSign nv-sa,C=BE
   valid:     2026-08-21 11:32:02+00:00 to 2027-01-24 05:46:23+00:00
   days:      155
   key:       RSA 2048
   signature: sha256WithRSAEncryption
   SAN names: 22 ['www.bbc.com', 'account.bbc.com', 'session.bbc.com']
www.coventry.ac.uk    coventry.pem: True  bbc.pem: False
coventry.ac.uk        coventry.pem: False  bbc.pem: False
www.bbc.co.uk         coventry.pem: False  bbc.pem: True
news.bbc.co.uk        coventry.pem: False  bbc.pem: True
sport.bbc.co.uk       coventry.pem: False  bbc.pem: False
```

- The university's certificate has one name only, `www.coventry.ac.uk`: it does **not** cover `coventry.ac.uk`.
- The BBC certificate says `CN=www.bbc.com`, but covers `www.bbc.co.uk` and `news.bbc.co.uk` because they are in its SAN. `sport.bbc.co.uk` is not, so that site needs another certificate.
- The SAN decides, not the CN, and a name that looks similar is not enough.

</details>

## Run

```
python3 read_real.py
```

About 12 minutes. Python 3 and the library `cryptography` (version 41 or newer). No internet needed.
