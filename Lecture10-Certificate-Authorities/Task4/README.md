# Task 4: who may sign?

## The situation

Mallory bought an honest certificate for her own website `mallory.example`, so she has a private key and a certificate signed by Trusty Issuing CA 1. She uses that key to sign a certificate for `bank.example`. The signature is mathematically correct. Will a TLS client accept it?

A second case: the company Acme gets its own intermediate CA, "Acme Corp CA", limited by Name Constraints to names under `acme.example`. What happens when it issues a certificate for `bank.example`? And Acme's CA has `path_len=0`: what if Acme makes one more CA below it?

![Top: Trusty Issuing CA 1 (CA:TRUE) signs mallory.example (CA:FALSE, Mallory's key), which signs a dashed pink certificate bank.example: accepted? Bottom: Acme Corp CA (permitted: acme.example) issues www.acme.example and bank.example: accepted? Below Acme Corp CA (path_len 0) one more CA, Acme Sub CA, issues www.acme.example: accepted?](figure.svg)

## Goal

See a TLS client reject a correct signature made by a leaf, a name outside a CA's limits, and a CA too deep in the tree.

## Ready for you

- In `who_may_sign.py`: Trusty Root CA (no path length limit), Trusty Issuing CA 1 and Mallory's honest certificate are already made, and the first line of output checks Mallory's own site.
- `cert_ready.py` (a black box): `new_key`, `make_cert`, `signed_by`, `tls_check` as in Task 3. `make_cert(..., permitted=["acme.example"])` adds Name Constraints to a CA certificate.

## Steps

Write your code in place of the `TODO` comments in `who_may_sign.py`. Under each `TODO` there is a line `print("not done yet: TODO n")`: replace it with your code.

1. Mallory signs a certificate for `bank.example` with her leaf: a new key `fake_key`, then `make_cert("bank.example", fake_key, mallory, mallory_key, ca=False, days=90, dns_names=["bank.example"])`.
2. Print `signed_by(fake, mallory)`, then let the TLS client connect: `tls_check(fake_key, [fake, mallory, inter], root, "bank.example")`.
3. Make "Acme Corp CA", signed by the root, `ca=True`, `path_len=0`, with `permitted=["acme.example"]`.
4. Let the Acme CA issue `www.acme.example` and `bank.example` (one key is enough for both) and call `tls_check` for each, with the chain `[leaf, acme]`.
5. Make "Acme Sub CA", signed by the Acme CA (`ca=True`), let it issue `www.acme.example` and call `tls_check` with the chain `[leaf, sub, acme]`.

## Expected output

Predict first: what does `signed_by` say in step 2? And the TLS client? And in step 5, which line of the chain stops the client?

<details>
<summary>Check your answer</summary>

```
1. mallory.example:           OK
2. her key signed the fake:   True
   bank.example via Mallory:  invalid CA certificate
3. www.acme.example via Acme: OK
4. bank.example via Acme:     permitted subtree violation
5. a CA below Acme Corp CA:   path length constraint exceeded
```

Mallory's signature is correct, but her certificate says `CA:FALSE`, so the client rejects the chain (`invalid CA certificate`). The Acme CA may issue only names under `acme.example` (`permitted subtree violation`). Acme Corp CA has `path_len=0`: only leaves may stand below it, so the Sub CA breaks the rule (`path length constraint exceeded`). With `path_len=1` the same chain is accepted. A client trusts the rules written in the chain, not only the signatures.

</details>

## Run

```
python3 who_may_sign.py
```

About 12 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
