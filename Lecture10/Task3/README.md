# Task 3: build your own PKI

## The situation

Alice runs the shop `alice-shop.example`. Instead of buying a certificate, she wants to see how a CA works from the inside, so she builds a tiny PKI of her own: a root CA "Trusty Root CA", an intermediate CA "Trusty CA 1", and a leaf certificate for her shop. Then a TLS client that trusts only her root connects to a server that uses the leaf.

![Three certificates to make: 1 Trusty Root CA (self-signed, CA:TRUE, path_len 1, 20 years), 2 Trusty CA 1 (signed by the root, CA:TRUE, path_len 0, 5 years), 3 alice-shop.example (signed by Trusty CA 1, CA:FALSE, 90 days). A TLS client that trusts only Trusty Root CA receives the leaf and the intermediate: OK, or why not?](figure.svg)

## Goal

Make a root, an intermediate and a leaf for alice-shop.example, and let a TLS client accept them.

## Ready for you

`cert_ready.py` (a black box):

- `new_key()` makes a new private key (elliptic curve P-256);
- `make_cert(cn, key, issuer, issuer_key, ca=..., path_len=..., days=..., dns_names=[...])` builds and signs a certificate for the name `cn` and the public half of `key`. `issuer` is the certificate of the CA that signs and `issuer_key` its private key; `issuer=None, issuer_key=None` makes a self-signed certificate. `ca=True` makes a CA certificate, `path_len` says how many CA certificates may stand below it;
- `save_cert(cert, path)`, `subject_of`, `issuer_of`, `signed_by` as before; `ca_flag(cert)` gives `(True or False, path length)`;
- `tls_check(leaf_key, chain, root, hostname)`: a TLS server sends `chain` (the leaf first) and a TLS client that trusts only `root` checks it, as a browser would, for the name `hostname`. It returns `"OK"` or the reason why the client said no. It runs in memory, with no network. What the client checks inside: Lecture 11.

## Steps

Write your code in place of the `TODO` comments in `build_pki.py`:

1. The root: `root_key = new_key()`, then `root = make_cert("Trusty Root CA", root_key, None, None, ca=True, path_len=1, days=20 * 365)`.
2. The intermediate "Trusty CA 1": a new key, signed by the root (`issuer=root, issuer_key=root_key`), `ca=True`, `path_len=0`, 5 years.
3. The leaf "alice-shop.example": a new key, signed by the intermediate, `ca=False`, 90 days, `dns_names=["alice-shop.example"]`.
4. Save the three certificates as `leaf.pem`, `intermediate.pem`, `root.pem` and print the subject, the issuer and `ca_flag` of each.
5. Check every signature link with `signed_by`, then call `tls_check(leaf_key, [leaf, inter], root, ...)` three times: for `"alice-shop.example"`, for `"bob-shop.example"`, and once with only `[leaf]` as the chain.

`openssl x509 -in leaf.pem -noout -text` shows your leaf the way Lecture 9 did.

## Expected output

<details>
<summary>Check your answer</summary>

```
leaf.pem : CN=alice-shop.example <- CN=Trusty CA 1 (False, None)
intermediate.pem : CN=Trusty CA 1 <- CN=Trusty Root CA (True, 0)
root.pem : CN=Trusty Root CA <- CN=Trusty Root CA (True, 1)
intermediate signed leaf: True
root signed intermediate: True
root signed root:         True
TLS, alice-shop.example:  OK
TLS, bob-shop.example:    Hostname mismatch, certificate is not valid for 'bob-shop.example'.
TLS, no intermediate:     unable to get local issuer certificate
```

The client accepts the chain for the name in the certificate, refuses another name, and cannot find its way to the root without the intermediate: a server must always send its intermediate certificates.

</details>

## Run

```
python3 build_pki.py
```

About 12 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
