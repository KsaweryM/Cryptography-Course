# Task 8: get a certificate by ACME

## The situation

Let's Encrypt gives certificates through ACME, with no person involved. To prove that Bob controls `bob.example`, the CA gives him a random token, and Bob puts a file with the "key authorization" on his web server, at `http://bob.example/.well-known/acme-challenge/<token>`. The CA downloads the file; if the text is right, it signs his CSR. This is the http-01 challenge.

Here everything runs on your computer: `acme_toy.py` starts a small web server on 127.0.0.1 that serves the folder `webroot/`, and a toy CA "Toy ACME CA R1" that believes `bob.example` is that web server. Simplified: real ACME signs every request with the account key and sends it over HTTPS; the http-01 challenge and the thumbprint are real (RFC 8555, RFC 7638).

![A sequence between get_certificate.py (Bob) and ToyCA. 1 new_order for bob.example with an account key; the CA answers with a token. 2 key authorization = token + "." + thumbprint(account key). 3 the file webroot/.well-known/acme-challenge/<token>. 4 validate(order): the CA downloads the file. 5 finalize(order, CSR) gives a certificate for 90 days.](figure.svg)

## Goal

Pass the http-01 challenge of a toy ACME CA and get a 90-day certificate.

## Ready for you

- `acme_toy.py` (a black box): `thumbprint(account_key)` gives the thumbprint of the public account key as text; `start_web_server(folder)`; `ToyCA(dns)` with `ca.new_order(domain, account_key)` (the order has `order.token`), `ca.validate(order)` (returns `"valid"` or `"invalid: ..."`) and `ca.finalize(order, csr)` (returns a certificate, or `None`).
- `cert_ready.py` (a black box): `new_key`, `make_csr`, `subject_of`, `issuer_of`, `valid_from`, `valid_until`.
- In `get_certificate.py` the web server and the CA are already started.

## Steps

Write your code in place of the `TODO` comments in `get_certificate.py`. Under each `TODO` there is a line `print("not done yet: TODO n")`: replace it with your code.

1. Make an account key (`new_key()`), ask the CA for a new order for `"bob.example"` and print `order.token`.
2. Build the key authorization: `order.token + "." + thumbprint(account_key)`.
3. Write it into the file `webroot/.well-known/acme-challenge/<token>`: build the folder name with `os.path.join("webroot", ".well-known", "acme-challenge")`, create it with `os.makedirs(folder, exist_ok=True)`, then `open(...)`, `write`, `close` as in C.
4. Ask the CA to validate the order and print the answer.
5. Make a new key for the website and a CSR for `"bob.example"`, send it with `ca.finalize(order, csr)`, and print the subject, the issuer and the dates of the certificate.

Finished early? Play Mallory, who found Bob's token: in step 2 use the thumbprint of another account key (`thumbprint(new_key())`) and run again. The CA says `invalid`, and the order cannot be used any more: the thumbprint ties the answer to the account that asked, so a copied token is worth nothing on another account.

## Expected output

The token and the thumbprint are different in every run.

<details>
<summary>Check your answer</summary>

```
1. token: S6JM86BWAylUbeYysS3AGjia1b-Whqge4T6U4SKorQI
2. key authorization: S6JM86BWAylUbeYysS3AGjia1b-Whqge4T6U4SKorQI.ZBiPuY0ddMd4NCRxqcgOX7N4UIwK6twfMMNL2tHLPjg
3. file written
   [CA] downloads http://bob.example/.well-known/acme-challenge/S6JM86BWAylUbeYysS3AGjia1b-Whqge4T6U4SKorQI
   [web server] GET /.well-known/acme-challenge/S6JM86BWAylUbeYysS3AGjia1b-Whqge4T6U4SKorQI -> 200
4. the CA says: valid
5. subject: CN=bob.example  issuer: CN=Toy ACME CA R1
   valid: 2026-11-19 to 2027-02-17
```

The CA downloaded the file from the web server and found the right text, so it signed the CSR: a certificate for 90 days. Only someone who controls the website can put that file there; certbot does the same steps over the internet.

</details>

## Run

```
python3 get_certificate.py
```

About 12 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
