# Task 6: hunt in a CT log

## The situation

Bob owns the domain `bob.example`. Every publicly trusted certificate is written into public **Certificate Transparency** logs, so he can read what any CA issued for his domain, even behind his back. He keeps the SHA-256 fingerprints of the certificates he ordered, and his DNS has a **CAA** record that allows only Trusty CA to issue for his domain.

`ct_log.pem` is a piece of a log: nine certificates from October and November 2026.

![A list of nine CT log entries, oldest first, each with a question mark: 2026-10-02 Green CA bakery.example, www.bakery.example; 2026-10-05 Trusty CA bob.example, www.bob.example; 2026-10-09 Green CA carol.example; 2026-10-14 Trusty CA api.bob.example; 2026-10-21 Green CA bob.example.mallory.example; 2026-10-25 Trusty CA dave.example, mail.dave.example; 2026-11-02 Shady CA bob.example, www.bob.example; 2026-11-06 Trusty CA login.bob.example; 2026-11-09 Shady CA mallory.example. Bob owns bob.example. His my_orders.txt has the SHA-256 fingerprints 5f1d8b540c1665af... and b2acc6775a289bc0...; his caa.txt is the DNS record CAA 0 issue "trusty-ca.example". Which entries are for Bob's domain? Which of those did he not order? Which CA broke his CAA record?](figure.svg)

Bob's CAA record has been in his DNS since September 2026, before all the certificates in this piece of the log. A CA checks CAA only at the moment it issues, so this matters: a certificate issued before the record existed broke nothing.

## Goal

Find the certificates for Bob's domain that he did not order, and say for each one whether the CA broke his CAA record.

## Ready for you

- `ctlog.py`: `load_log(path)` (a list of certificates), `load_orders(path)` (his fingerprints as hex text), `dns_names(cert)` (a list of names), `issuer_cn(cert)`, `issued_on(cert)`, `CAA_ID` (a `dict`: the CAA name of each CA, `CAA_ID["Trusty CA"]` is `"trusty-ca.example"`) and `ALLOWED` (the CAA names in `caa.txt`).
- From the `cryptography` library: `cert.fingerprint(hashes.SHA256())` returns the SHA-256 of the whole certificate; `.hex()` turns it into hex text.

## Steps

Write your code in place of the `TODO` comments in `ct_watch.py`, inside the loop over the log:

1. Is the certificate for Bob's domain? Yes if one of its names is `DOMAIN` or ends with `"." + DOMAIN` (`name.endswith(...)`). Careful: `bob.example.mallory.example` is Mallory's domain, not Bob's. If not, `continue`.
2. `fp = cert.fingerprint(hashes.SHA256()).hex()`. If `fp in orders`, print `mine:` with the names and the date, then `continue`.
3. Otherwise print `UNKNOWN:` with the names, the CA and the date. If `CAA_ID[issuer_cn(cert)] in ALLOWED`, the CA was allowed: ask it who ordered the certificate. If not, the CA broke CAA: report it.

The starter prints `not done yet: TODO 1 to 3` for every certificate; delete that line when the three steps are done.

## Expected output

Two certificates are Bob's, two are not. One CA broke CAA, the other did not.

<details>
<summary>Check your answer</summary>

```
9 certificates in the log, 2 ordered by Bob, CAA allows ['trusty-ca.example']
mine:    ['bob.example', 'www.bob.example'] issued 2026-10-05
mine:    ['api.bob.example'] issued 2026-10-14
UNKNOWN: ['bob.example', 'www.bob.example'] from Shady CA issued 2026-11-02
  this CA broke CAA: report it and ask the browsers to look at it
UNKNOWN: ['login.bob.example'] from Trusty CA issued 2026-11-06
  CAA allowed this CA: ask it who ordered the certificate
```

CAA cannot stop a CA that ignores it, and it cannot stop the allowed CA from being fooled. The log makes both cases visible within days, instead of seven weeks as with DigiNotar in 2011. Real logs are read by monitors such as crt.sh, which can e-mail you when a new certificate for your domain appears. One trap in real logs: a CA first logs a **precertificate** (the same fields with a poison extension), whose fingerprint differs from the final certificate. On crt.sh you see both, so compare names, serial numbers and keys before you raise an alarm about a fingerprint you do not know.

</details>

## Run

```
python3 ct_watch.py
```

About 10 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
