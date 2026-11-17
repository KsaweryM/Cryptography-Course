# Task 1: follow the chain

## The situation

When Bob's browser opens https://www.coventry.ac.uk, the server sends two certificates: its own (the leaf) and the intermediate certificate WE1 of Google Trust Services. The third certificate, the root GTS Root R4, is already on Bob's computer, in its trust store. The three files in this folder were saved on 15 November 2026 (`openssl s_client -connect www.coventry.ac.uk:443 -showcerts`; the root comes from the trust store of Ubuntu 24.04). Check that they really form a chain.

![Three certificate cards: leaf.pem (www.coventry.ac.uk, issued by WE1, valid 2026-10-13 to 2027-01-11, EC P-256), intermediate.pem (WE1, Google Trust Services, issued by GTS Root R4, valid 2023-12-13 to 2029-02-20, EC P-256) and root.pem (GTS Root R4, issued by itself, valid 2016-06-22 to 2036-06-22, EC P-384). Arrows with question marks: did the next certificate sign the previous one?](figure.svg)

## Goal

Check, link by link, that the names and the signatures of the chain of www.coventry.ac.uk fit together.

## Ready for you

- `leaf.pem`, `intermediate.pem`, `root.pem`: the three certificates.
- `cert_ready.py` (a black box):
  - `load_cert(path)` reads a certificate from a PEM file;
  - `subject_of(cert)`, `issuer_of(cert)` give the names as text;
  - `valid_from(cert)`, `valid_until(cert)` give the dates (`.date()` keeps only the day);
  - `signed_by(child, parent)` is `True` when the issuer name of `child` is the subject name of `parent` and the signature on `child` verifies with the public key of `parent`.
- Two certificates `a` and `b` can also be compared directly: `a.issuer == b.subject` compares the names as objects.

## Steps

Write your code in place of the `TODO` comments in `follow_chain.py`:

1. Load the three certificates into a list, the leaf first: `chain = [load_cert("leaf.pem"), ...]`.
2. For each certificate (a loop over `range(len(chain))`) print its subject, its issuer and its dates.
3. For each link `i` (from 0 to 1) print whether `chain[i].issuer == chain[i + 1].subject`.
4. For each link `i` print whether `signed_by(chain[i], chain[i + 1])`.
5. Print whether the root signed itself (`signed_by(chain[2], chain[2])`) and whether the leaf signed the intermediate (`signed_by(chain[1], chain[0])`).

## Expected output

Predict first: which of the checks in step 5 gives `False`?

<details>
<summary>Check your answer</summary>

```
0 subject: CN=www.coventry.ac.uk
  issuer:  CN=WE1,O=Google Trust Services,C=US
  valid:   2026-10-13 to 2027-01-11
1 subject: CN=WE1,O=Google Trust Services,C=US
  issuer:  CN=GTS Root R4,O=Google Trust Services LLC,C=US
  valid:   2023-12-13 to 2029-02-20
2 subject: CN=GTS Root R4,O=Google Trust Services LLC,C=US
  issuer:  CN=GTS Root R4,O=Google Trust Services LLC,C=US
  valid:   2016-06-22 to 2036-06-22

issuer of 0 == subject of 1 : True
issuer of 1 == subject of 2 : True
1 signed 0 : True
2 signed 1 : True
the root signed itself: True
the leaf signed the intermediate: False
```

Both links hold: the names match and each certificate is signed by the next one. The root signs itself; that proves nothing, the trust in it comes from the trust store. The leaf did not sign the intermediate: a chain only works in one direction.

</details>

## Run

```
python3 follow_chain.py
```

About 8 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
