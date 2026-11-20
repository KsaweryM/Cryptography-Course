# Task 4: check a CRL

## The situation

Carol's private key leaked, so on 10 November 2026 her CA, **Trusty Issuing CA 1**, revoked her certificate. Bob's certificate is fine. Alice has three Certificate Revocation Lists that claim to come from this CA: the current one, an old one from October, and one that Mallory made with her own key. A list is worth something only if the CA signed it and it is still fresh.

![Trusty Issuing CA 1 issued bob.pem (bob.example, serial 0x1001) and carol.pem (carol.example, serial 0x1002). Three lists: crl.pem, valid 15 Nov 2026 to 31 Dec 2027, revokes 0FFE (superseded) and 1002 (keyCompromise), signed with Trusty Issuing CA 1; old_crl.pem, valid 1 Oct to 8 Oct 2026, revokes 0FFE, signed with Trusty Issuing CA 1; fake_crl.pem, valid 15 Nov 2026 to 31 Dec 2027, revokes 0FFE, signed with a key, but whose? For each list: 1 is the signature the CA's, 2 is it still fresh, then 3 look up Bob's and Carol's serial numbers.](figure.svg)

## Goal

Decide whether Bob's and Carol's certificates are revoked, using only lists that are signed by the CA and still fresh.

## Ready for you

- `crl_ready.py` (do not change it): `load_cert(filename)`, `load_crl(filename)`, `NOW`, `name_of(cert)`, `next_update(crl)` (Next Update), `revoked_on(entry)` (the date of one entry) and `reason_of(entry)` (for example `keyCompromise`).
- `files/`: the CA certificate `issuing_ca.pem`, `bob.pem`, `carol.pem` and the three lists.
- `check_crl.py`: loads everything and loops over the lists and the certificates.
- Two methods of the `cryptography` library that you will call directly:
  - `crl.is_signature_valid(public_key)` is `True` only if the list was signed with the matching private key.
  - `crl.get_revoked_certificate_by_serial_number(serial)` returns the entry for that serial number, or `None`.

## Steps

Write your code in place of the `TODO` comments in `check_crl.py`:

1. In `list_is_good`: check the list's signature with `crl.is_signature_valid` and the CA's public key. If the CA did not sign it, return `"bad signature"`.
2. In `list_is_good`: if `next_update(crl)` is before `NOW`, return `"too old (next update was %s)" % next_update(crl).date()`. When both checks pass, return `"OK"` in place of the line `return "not done yet: TODO 1"`.
3. In the loop: look the certificate's serial number up with `crl.get_revoked_certificate_by_serial_number`. If there is no entry, print `not revoked`; otherwise print `REVOKED on`, `revoked_on(entry)` and `reason:` `reason_of(entry)`.

Until you write the code, every list is rejected with `not done yet: TODO 1`.

<details>
<summary>Hint: the calls of steps 1 and 3</summary>

```python
if crl.is_signature_valid(ca.public_key()) is not True:
    return "bad signature"
...
entry = crl.get_revoked_certificate_by_serial_number(cert.serial_number)
if entry is None:
    ...
```

`is None` is how Python compares with `None`, like comparing a pointer with `NULL` in C.

</details>

## Expected output

The good list says Bob is fine and Carol is revoked. The other two lists are rejected before you read them.

<details>
<summary>Check your answer</summary>

```
crl.pem       list OK (next update 2027-12-31)
    bob.example    serial 0x1001  not revoked
    carol.example  serial 0x1002  REVOKED on 2026-11-10 09:30:00, reason: keyCompromise
old_crl.pem   REJECT the list: too old (next update was 2026-10-08)
fake_crl.pem  REJECT the list: bad signature
```

Without steps 1 and 2, the old list and the fake list would both say that Carol is fine: neither lists her serial number. Real lists live a few days (the list of Google's CA WE1: about 10 days); `crl.pem` lasts until the end of 2027 only so that this task works during the whole course. For the same reason the certificates of this private test CA live two years; a public certificate issued today may live at most 200 days (Lecture 10).

</details>

## Run

```
python3 check_crl.py
```

About 10 minutes. Python 3 and the `cryptography` library (version 41 or newer); works offline.
