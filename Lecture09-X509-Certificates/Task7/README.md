# Task 7: two real certificates

## The situation

`coventry.pem` and `bbc.pem` are the real certificates of www.coventry.ac.uk and www.bbc.co.uk, saved on 15 November 2026 with

```
openssl s_client -connect www.coventry.ac.uk:443 -servername www.coventry.ac.uk < /dev/null > out.txt
```

(and the same for www.bbc.co.uk), keeping the first certificate. `cert_D.pem` is Dave's certificate from Task 4, with the name `*.dave.example`. No internet is needed for the task. The university's certificate is valid for 90 days and is renewed before it ends, so what the sites send today is probably newer.

A browser does one check with every certificate: is the name in the address bar covered by the SAN? Here you write that check yourself, with the wildcard rule.

![Three certificate cards. coventry.pem: subject CN=www.coventry.ac.uk, issuer WE1 (Google Trust Services), key EC P-256. bbc.pem: subject CN=www.bbc.com, O=BRITISH ..., C=GB, issuer GlobalSign GCC R46 OV TLS CA 2025, key RSA 2048. cert_D.pem: SAN *.dave.example, issuer Trusty CA. On each: days valid? SAN: ? names. Below, eight names with a question mark each: www.coventry.ac.uk, coventry.ac.uk, www.bbc.co.uk, news.bbc.co.uk, sport.bbc.co.uk, play.dave.example, dave.example, x.play.dave.example. Steps 3 and 4: matches(pattern, host) with the * rule, and covers(cert, host).](figure.svg)

## Goal

Read the two real certificates: who they belong to, who issued them, for how many days. Then write the name check of a browser, `covers(cert, host)`, with the wildcard rule, and decide which names each certificate covers.

Predict first: does the university's certificate cover `coventry.ac.uk`, without `www.`?

## Ready for you

- `coventry.pem`, `bbc.pem`, `cert_D.pem`.
- `cert_tools.py`: `load_cert`, `valid_from(cert)` and `valid_until(cert)` (dates in UTC), `find_extension(cert, kind)`, `key_name(public_key)` (for example `EC P-256`), `oid_name(oid)`.
- In `read_real.py`: the loop over the three files, which already prints the key and the signature algorithm, the list `hosts`, and a test line for `matches()`.

## Steps

Write your code in place of the `TODO` comments in `read_real.py`:

1. Print the subject and the issuer (`.rfc4514_string()`).
2. Print how many days the certificate is valid: `(valid_until(cert) - valid_from(cert)).days`.
3. Write `matches(pattern, host)` for one SAN name `pattern`:
   - equal names match: `pattern == host`;
   - a pattern that starts with `"*."` is a wildcard. The `*` stands for exactly one label (the part between two dots), the left-most one. Take `rest = pattern[1:]` (for `*.dave.example` that is `.dave.example`) and `dot = host.find(".")`, the index of the first dot in `host` (`-1` if there is none, like `strchr` in C). The host matches if `dot > 0` and `host[dot:] == rest`;
   - anything else does not match.
4. Write `covers(cert, host)`: `san = find_extension(cert, x509.SubjectAlternativeName)`, `names = san.get_values_for_type(x509.DNSName)`, then loop over `names` with an index and return `True` if `matches(names[k], host)` for one of them, otherwise `False`.
5. In the loop over the files: print how many DNS names the SAN has, and the first three of them.
6. After the loop: for every host in `hosts` print one line with the result of `covers()` for each of the three certificates.

## Expected output

For each certificate: subject, issuer, days, key, signature algorithm, the SAN count; the test line; then a table of `True` and `False`.

<details>
<summary>Check your answer</summary>

```
== coventry.pem
   subject:   CN=www.coventry.ac.uk
   issuer:    CN=WE1,O=Google Trust Services,C=US
   days:      90
   key:       EC P-256
   signature: ecdsa-with-SHA256
   SAN names: 1 ['www.coventry.ac.uk']
== bbc.pem
   subject:   CN=www.bbc.com,O=BRITISH BROADCASTING CORPORATION,L=London,ST=London,C=GB
   issuer:    CN=GlobalSign GCC R46 OV TLS CA 2025,O=GlobalSign nv-sa,C=BE
   days:      155
   key:       RSA 2048
   signature: sha256WithRSAEncryption
   SAN names: 22 ['www.bbc.com', 'account.bbc.com', 'session.bbc.com']
== cert_D.pem
   subject:   CN=*.dave.example,O=Dave Games Ltd,C=GB
   issuer:    CN=Trusty CA,O=Trusty CA Ltd,C=GB
   days:      90
   key:       Ed25519
   signature: Ed25519
   SAN names: 1 ['*.dave.example']
test: *.carol.example fits www.carol.example: True (should be True)
www.coventry.ac.uk    coventry.pem: True   bbc.pem: False  cert_D.pem: False
coventry.ac.uk        coventry.pem: False  bbc.pem: False  cert_D.pem: False
www.bbc.co.uk         coventry.pem: False  bbc.pem: True   cert_D.pem: False
news.bbc.co.uk        coventry.pem: False  bbc.pem: True   cert_D.pem: False
sport.bbc.co.uk       coventry.pem: False  bbc.pem: False  cert_D.pem: False
play.dave.example     coventry.pem: False  bbc.pem: False  cert_D.pem: True 
dave.example          coventry.pem: False  bbc.pem: False  cert_D.pem: False
x.play.dave.example   coventry.pem: False  bbc.pem: False  cert_D.pem: False
```

- The university's certificate has one name only, `www.coventry.ac.uk`: it does **not** cover `coventry.ac.uk`.
- The BBC certificate says `CN=www.bbc.com`, but covers `www.bbc.co.uk` and `news.bbc.co.uk` because they are in its SAN. `sport.bbc.co.uk` is not, so that site needs another certificate.
- `*.dave.example` covers `play.dave.example`, but not `dave.example` (nothing for the `*`) and not `x.play.dave.example` (two labels for one `*`).
- The SAN decides, not the CN, and a name that looks similar is not enough.

</details>

## Run

```
python3 read_real.py
```

About 15 minutes. Python 3 and the library `cryptography` (version 41 or newer). No internet needed.
