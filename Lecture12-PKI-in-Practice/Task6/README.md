# Task 6: hunt in a CT log

## The situation

Alice owns the domain `alice-shop.example`. Every publicly trusted certificate is written into public **Certificate Transparency** logs, so she can read what any CA issued for her domain, even behind her back. She keeps the SHA-256 fingerprints of the certificates she ordered, and her DNS has a **CAA** record that allows only Trusty CA to issue for her domain.

`ct_log.pem` is a piece of a log: nine certificates from October and November 2026.

![A list of nine CT log entries, oldest first, each with a question mark: 2026-10-02 Green CA bob-bakery.example, www.bob-bakery.example; 2026-10-05 Trusty CA alice-shop.example, www.alice-shop.example; 2026-10-09 Green CA carol.example; 2026-10-14 Trusty CA api.alice-shop.example; 2026-10-21 Green CA alice-shop.example.mallory.example; 2026-10-25 Trusty CA dave.example, mail.dave.example; 2026-11-02 Shady CA alice-shop.example, www.alice-shop.example; 2026-11-06 Trusty CA login.alice-shop.example; 2026-11-09 Shady CA bob.example. Alice owns alice-shop.example. Her my_orders.txt has the SHA-256 fingerprints 606599e5fee40972... and 4e74d58c752088e8...; her caa.txt is the DNS record CAA 0 issue "trusty-ca.example". Which entries are for Alice's domain? Which of those did she not order? Which CA broke her CAA record?](figure.svg)

Alice's CAA record has been in her DNS since September 2026, before all the certificates in this piece of the log. A CA checks CAA only at the moment it issues, so this matters: a certificate issued before the record existed broke nothing.

## Goal

Find the certificates for Alice's domain that she did not order, and say for each one whether the CA broke her CAA record.

## Ready for you

- `ctlog.py`: `load_log(path)` (a list of certificates), `load_orders(path)` (her fingerprints as hex text), `dns_names(cert)` (a list of names), `issuer_cn(cert)`, `issued_on(cert)`, `CAA_ID` (a `dict`: the CAA name of each CA, `CAA_ID["Trusty CA"]` is `"trusty-ca.example"`) and `ALLOWED` (the CAA names in `caa.txt`).
- From the `cryptography` library: `cert.fingerprint(hashes.SHA256())` returns the SHA-256 of the whole certificate; `.hex()` turns it into hex text.

## Steps

Write your code in place of the `TODO` comments in `ct_watch.py`, inside the loop over the log:

1. Is the certificate for Alice's domain? Yes if one of its names is `DOMAIN` or ends with `"." + DOMAIN` (`name.endswith(...)`). Careful: `alice-shop.example.mallory.example` is Mallory's domain, not Alice's. If not, `continue`.
2. `fp = cert.fingerprint(hashes.SHA256()).hex()`. If `fp in orders`, print `mine:` with the names and the date, then `continue`.
3. Otherwise print `UNKNOWN:` with the names, the CA and the date. If `CAA_ID[issuer_cn(cert)] in ALLOWED`, the CA was allowed: ask it who ordered the certificate. If not, the CA broke CAA: report it.

The starter prints `not done yet: TODO 1 to 3` for every certificate; delete that line when the three steps are done.

## Expected output

Two certificates are Alice's, two are not. One CA broke CAA, the other did not.

<details>
<summary>Check your answer</summary>

```
9 certificates in the log, 2 ordered by Alice, CAA allows ['trusty-ca.example']
mine:    ['alice-shop.example', 'www.alice-shop.example'] issued 2026-10-05
mine:    ['api.alice-shop.example'] issued 2026-10-14
UNKNOWN: ['alice-shop.example', 'www.alice-shop.example'] from Shady CA issued 2026-11-02
  this CA broke CAA: report it and ask the browsers to look at it
UNKNOWN: ['login.alice-shop.example'] from Trusty CA issued 2026-11-06
  CAA allowed this CA: ask it who ordered the certificate
```

CAA cannot stop a CA that ignores it, and it cannot stop the allowed CA from being fooled. The log makes both cases visible within days, instead of months as with DigiNotar in 2011. Real logs are read by monitors such as crt.sh, which can e-mail you when a new certificate for your domain appears. One trap in real logs: a CA first logs a **precertificate** (the same fields with a poison extension), whose fingerprint differs from the final certificate. On crt.sh you see both, so compare names, serial numbers and keys before you raise an alarm about a fingerprint you do not know.

</details>

## Run

```
python3 ct_watch.py
```

About 10 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
