# Task 4: which certificate fits?

## The situation

Trusty CA has issued four certificates: `cert_A.pem` to `cert_D.pem`. Their subjects alone do not say what each one may be used for: the extensions do. Read the Subject Alternative Name, Basic Constraints, Key Usage, Extended Key Usage and the critical flags, and decide.

![Four certificate cards: cert_A.pem (www.alice-shop.example), cert_B.pem (Trusty CA Issuing 1), cert_C.pem (Carol Software Ltd) and cert_D.pem (*.dave.example), each with the questions SAN? CA? EKU? critical? Below: which one is a CA, which one may sign programs, and which one fits www.alice-shop.example, shop.dave.example and dave.example?](figure.svg)

## Goal

Print the main extensions of the four certificates, then answer: which one is a CA? Which one may sign programs? Which one fits `www.alice-shop.example`, `shop.dave.example` and `dave.example`?

## Ready for you

- `cert_tools.py`:
  - `load_cert(path)` reads a certificate,
  - `find_extension(cert, kind)` returns the value of one extension, or `None` when the certificate does not have it. `kind` is a class, for example `x509.SubjectAlternativeName`,
  - `ext_name(ext)` and `oid_name(oid)` give short names such as `keyUsage` or `serverAuth`.
- In `which_cert.py`: the loop over the four files, which prints each subject.

## Steps

Write your code in place of the `TODO` comments in `which_cert.py`, inside the loop:

1. The names: `san = find_extension(cert, x509.SubjectAlternativeName)`. If it is `None`, print `none`; otherwise print `san.get_values_for_type(x509.DNSName)`, a list of the DNS names.
2. A CA? `bc = find_extension(cert, x509.BasicConstraints)`, then print `bc.ca`.
3. What may the key do? `ku = find_extension(cert, x509.KeyUsage)`: print `ku.digital_signature` and `ku.key_cert_sign`. Then `eku = find_extension(cert, x509.ExtendedKeyUsage)`: if it is not `None`, it is a list of purposes; print `oid_name(eku[k])` for every `k`.
4. Which extensions are critical? Loop over `cert.extensions` and print `ext_name(ext)` for every `ext` with `ext.critical` equal to `True`.

Then answer the questions from the Goal. Remember: a `*` matches exactly one label (the part between two dots), the left-most one.

## Expected output

For each certificate: its subject, the SAN names, `CA: True` or `False`, the key usage, the extended key usage and the list of critical extensions.

<details>
<summary>Check your answer</summary>

```
== cert_A.pem  subject: CN=www.alice-shop.example,O=Alice Shop Ltd,C=GB
   SAN:          ['alice-shop.example', 'www.alice-shop.example']
   CA:           False
   key usage:    digital_signature True  key_cert_sign False
   ext. usage:   ['serverAuth']
   critical:     ['keyUsage']
== cert_B.pem  subject: CN=Trusty CA Issuing 1,O=Trusty CA Ltd,C=GB
   SAN:          none
   CA:           True
   key usage:    digital_signature True  key_cert_sign True
   ext. usage:   none
   critical:     ['basicConstraints', 'keyUsage']
== cert_C.pem  subject: CN=Carol Software Ltd,O=Carol Software Ltd,C=GB
   SAN:          none
   CA:           False
   key usage:    digital_signature True  key_cert_sign False
   ext. usage:   ['codeSigning']
   critical:     ['basicConstraints', 'keyUsage', 'extendedKeyUsage']
== cert_D.pem  subject: CN=*.dave.example,O=Dave Games Ltd,C=GB
   SAN:          ['*.dave.example']
   CA:           False
   key usage:    digital_signature True  key_cert_sign False
   ext. usage:   ['serverAuth', 'clientAuth']
   critical:     ['basicConstraints', 'keyUsage']
```

- A CA: **B** (`CA: True` and `key_cert_sign`).
- May sign programs: **C** (`codeSigning`).
- `www.alice-shop.example`: **A**. `shop.dave.example`: **D** (`*` = `shop`).
- `dave.example`: **none of them**. `*.dave.example` needs one label in place of `*`.

</details>

## Run

```
python3 which_cert.py
```

About 10 minutes. Python 3 and the library `cryptography` (version 41 or newer).
