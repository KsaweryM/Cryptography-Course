# Task 5: check four CSRs

## The situation

You play the CA. Three certificate signing requests (CSRs) arrived, and a new customer, Carol, is about to send a fourth:

- `bob.csr`: Bob's request for `bob.example`;
- `bob-changed.csr`: the same request after Mallory changed a few bytes on the way (the name `bob.example` became `mal.example`);
- `mallory.csr`: Mallory's own request for `bob.example`, made with her own key.

A CSR carries a name, a public key and a signature made with the matching private key. Which requests should you accept?

![Bob sends bob.csr (bob.example, Bob's key, signed by Bob's key). On the way it becomes bob-changed.csr (mal.example, Bob's key, Bob's old signature). Mallory sends mallory.csr (bob.example, Mallory's key, signed by Mallory's key). You, the CA: is the signature valid?](figure.svg)

## Goal

Check the signatures of four CSRs and see what a valid one proves.

## Ready for you

- `bob.csr`, `bob-changed.csr`, `mallory.csr`.
- `cert_ready.py` (a black box): `new_key()`; `make_csr(key, cn, dns_names)` builds a CSR and signs it with `key`; `save_csr`, `load_csr`; `subject_of(csr)`, `dns_names_of(csr)`; `key_id(public_key)` gives a short fingerprint of a public key (16 hex digits).
- `csr.is_signature_valid` is `True` when the signature on the CSR verifies with the public key inside the same CSR. `csr.public_key()` gives that key.

## Steps

Write your code in place of the `TODO` comments in `check_csrs.py`. Under each `TODO` there is a line `print("not done yet: TODO n")`: replace it with your code.

1. Make Carol's key and a CSR for `"carol.example"` (with the same name in `dns_names`) and save it as `carol.csr`.
2. Load the four CSRs (Carol's first) into a list and print, for each, the file name, the subject and the DNS names.
3. Print, for each CSR, whether its signature is valid.
4. Print the `key_id` of the public key in `bob.csr` and in `mallory.csr`.

`openssl req -in carol.csr -noout -text -verify` shows Carol's CSR.

## Expected output

Predict first: which CSRs have a valid signature?

<details>
<summary>Check your answer</summary>

```
carol.csr : CN=carol.example ['carol.example']
bob.csr : CN=bob.example ['bob.example']
bob-changed.csr : CN=mal.example ['mal.example']
mallory.csr : CN=bob.example ['bob.example']

carol.csr signature valid: True
bob.csr signature valid: True
bob-changed.csr signature valid: False
mallory.csr signature valid: True

key in bob.csr:     1e21088d56d9a109
key in mallory.csr: 5dec17479913c708
```

The changed request fails: any change breaks the signature. But Mallory's own request for Bob's name is perfectly valid, only with a different key. A CSR proves that the sender holds the private key, not that the name is theirs: that is why the CA must check the name (DV, OV or EV) before it issues anything.

</details>

## Run

```
python3 check_csrs.py
```

About 10 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
