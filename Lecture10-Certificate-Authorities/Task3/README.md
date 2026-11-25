# Task 3: build your own PKI

## The situation

Bob runs the website `bob.example`. Instead of buying a certificate, he wants to see how a CA works from the inside, so he builds a tiny PKI of his own: a root CA "Trusty Root CA", an intermediate CA "Trusty Issuing CA 1", and a leaf certificate for his website. Then a TLS client (Alice's browser) that trusts only his root connects to a server that uses the leaf.

![Three certificates to make: 1 Trusty Root CA (self-signed, CA:TRUE, path_len 1, 20 years), 2 Trusty Issuing CA 1 (signed by the root, CA:TRUE, path_len 0, 5 years), 3 bob.example (signed by Trusty Issuing CA 1, CA:FALSE, 90 days). A TLS client that trusts only Trusty Root CA receives the leaf and the intermediate: OK, or why not?](figure.svg)

## Goal

Make a root, an intermediate and a leaf for bob.example, and let a TLS client accept them.

## Ready for you

`cert_ready.py` (a black box):

- `new_key()` makes a new private key (elliptic curve P-256);
- `make_cert(cn, key, issuer, issuer_key, ca=..., path_len=..., days=..., dns_names=[...])` builds and signs a certificate for the name `cn` and the public half of `key`. `issuer` is the certificate of the CA that signs and `issuer_key` its private key; `issuer=None, issuer_key=None` makes a self-signed certificate. `ca=True` makes a CA certificate (a certificate whose key may sign other certificates), `path_len` says how many CA certificates may stand below it; both come back in the next section, "Limits on a CA";
- `save_cert(cert, path)`, `subject_of`, `issuer_of`, `signed_by` as before; `ca_flag(cert)` gives `(True or False, path length)`;
- `tls_check(leaf_key, chain, root, hostname)`: a TLS server sends `chain` (the leaf first) and a TLS client that trusts only `root` checks it, as a browser would, for the name `hostname`. It returns `"OK"` or the reason why the client said no. It runs in memory, with no network. What the client checks inside: Lecture 11.

## Steps

Write your code in place of the `TODO` comments in `build_pki.py`. Under each `TODO` there is a line `print("not done yet: TODO n")`: replace it with your code.

1. The root: `root_key = new_key()`, then `root = make_cert("Trusty Root CA", root_key, None, None, ca=True, path_len=1, days=20 * 365)`.
2. The intermediate "Trusty Issuing CA 1": a new key, signed by the root (`issuer=root, issuer_key=root_key`), `ca=True`, `path_len=0`, 5 years.
3. The leaf "bob.example": a new key, signed by the intermediate, `ca=False`, 90 days, `dns_names=["bob.example"]`.
4. Save the three certificates as `leaf.pem`, `intermediate.pem`, `root.pem` and print the subject, the issuer and `ca_flag` of each.
5. Check every signature link with `signed_by`, then call `tls_check(leaf_key, [leaf, inter], root, "bob.example")`, and once more with only `[leaf]` as the chain (a server that forgets to send its intermediate).

`openssl x509 -in leaf.pem -noout -text` shows your leaf the way Lecture 9 did.

## Expected output

Predict first: will the client accept the leaf alone, without the intermediate?

<details>
<summary>Check your answer</summary>

```
leaf.pem : CN=bob.example <- CN=Trusty Issuing CA 1 (False, None)
intermediate.pem : CN=Trusty Issuing CA 1 <- CN=Trusty Root CA (True, 0)
root.pem : CN=Trusty Root CA <- CN=Trusty Root CA (True, 1)
intermediate signed leaf: True
root signed intermediate: True
root signed root:         True
TLS, leaf + intermediate: OK
TLS, leaf only:           unable to get local issuer certificate
```

The client accepts the chain, but cannot find its way to the root without the intermediate: a server must always send its intermediate certificates. The other checks of the client (the name, the dates) come in Lecture 11.

</details>

## Run

```
python3 build_pki.py
```

About 10 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
