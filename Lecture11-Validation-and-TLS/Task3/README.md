# Task 3: check six chains yourself

## The situation

Alice typed `bob.example`. Six servers sent her six chains (the leaf first, then the certificates above it), and her trust store holds one root, the **Trusty Root CA**. Each chain breaks at most one rule. In Task 1 a library did all the checks for you; now you write them yourself, one by one, and find which rule each chain breaks.

![Six chains, leaf first. case1: bob.example signed by Trusty Issuing CA 1. case2: bob.example signed by Trusty Issuing CA 0, valid until 30 Jun 2026. case3: *.bob.example signed by Trusty Issuing CA 1. case4: bob.example signed by mallory.example, signed by Trusty Issuing CA 1. case5: bob.example signed by Trusty Issuing CA 1. case6: bob.example for clientAuth only, signed by Trusty Issuing CA 1. The trust store holds Trusty Root CA. Your checks in check(): 1 signatures up to a trusted root, 2 dates of every certificate, 3 the name with the wildcard rule, 4 every issuer is a CA, 5 the leaf is for a server.](figure.svg)

## Goal

Write the checks 1 to 5 in `check()` and find the one rule that each chain breaks.

## Ready for you

- `certs_ready.py` (do not change it), black boxes on top of the `cryptography` library:
  - `load_chain(filename)` gives the list of certificates from `chains/`, `load_store()` the trust store (a list with one root).
  - `signed_by(cert, issuer)`: `True` if `cert` was signed with the private key of `issuer` (and names `issuer` as its issuer).
  - `valid_from(cert)`, `valid_until(cert)`: Not Before and Not After; `NOW` is the time now. They can be compared with `<=`.
  - `dns_names(cert)`: the DNS names in the SAN, for example `['bob.example']`.
  - `is_ca(cert)`: `True` if Basic Constraints says `CA:TRUE`.
  - `key_purposes(cert)`: the Extended Key Usage, for example `['serverAuth']`.
  - `name_of(cert)`: the Common Name, only for printing.
- `check_chain.py`: the six cases and the loop that prints the result of `check()`.

## Steps

Write your code in place of the `TODO` comments in `check_chain.py`. `check()` returns `"OK"` or the first check that fails, with the exact text given in the `TODO`. Do the checks in this order:

1. **Signatures.** For every `i` from 0 to `n - 2`, `chain[i]` must be `signed_by` `chain[i + 1]`. The last certificate must be signed by a root in `store` (loop over `store`).
2. **Dates.** For every certificate: `valid_from(c) <= NOW <= valid_until(c)`.
3. **The name.** First write `name_matches(pattern, host)`: equal names (ignore case with `.lower()`), or a wildcard `*.bob.example` that covers exactly one more label (`www.bob.example` yes, `bob.example` no, `a.b.bob.example` no). Then `host` must match at least one of `dns_names(chain[0])`.
4. **Basic Constraints.** Every certificate except the leaf must be a CA: `is_ca(chain[i])`.
5. **Extended Key Usage.** `"serverAuth"` must be in `key_purposes(chain[0])`.
6. **All passed.** At the end of `check()`, return `"OK"` in place of the line `return "not done yet: TODO 1"`.

Hints:

- `for i in range(n - 1):` runs `i = 0, 1, ..., n - 2`, like `for (i = 0; i < n - 1; i++)` in C.
- Useful string functions: `s.startswith("*.")`, `s.endswith(rest)`, `s[1:]` (everything after the first character), `"." in s`.

Until you write the checks, every line says `not done yet: TODO 1`.

## Expected output

One line per case: one good chain and five different failures.

<details>
<summary>Check your answer</summary>

```
case1.pem  2 certificates  OK
case2.pem  2 certificates  check 2: certificate 1 is not valid now (until 2026-06-30)
case3.pem  2 certificates  check 3: bob.example is not in ['*.bob.example']
case4.pem  3 certificates  check 4: certificate 1 (mallory.example) is not a CA
case5.pem  2 certificates  check 1: certificate 1 is not signed by a trusted root
case6.pem  2 certificates  check 5: the leaf is for ['clientAuth'], not for a server
```

OpenSSL agrees (`openssl verify -purpose sslserver -verify_hostname bob.example`): errors 10 (expired), 62 (hostname mismatch), 79 (invalid CA certificate), 7 (signature failure) and 26 (unsuitable purpose). In case 4 every signature, date and name is fine: Mallory used her real leaf as a CA, and only Basic Constraints stops her. In case 5 she made her own "Trusty Issuing CA 1" with the right name, but she cannot make the root's signature.

</details>

The Trusty CA is a private test CA, so its certificates may live two years; a public certificate issued today may live at most 200 days (Lecture 10).

## Run

```
python3 check_chain.py
```

About 15 minutes. Python 3 and the `cryptography` library (`pip install cryptography`, version 41 or newer); works offline.
