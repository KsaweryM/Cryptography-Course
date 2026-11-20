# Task 7: log in with a certificate

## The situation

Bob's server `bob.example` does not use passwords. It uses **mutual TLS**: during the handshake it asks the client for a certificate, and it lets in only clients whose certificate was issued by **Bob Staff CA**, Bob's private CA for his staff. Alice has such a certificate. Mallory made her own certificate that also says `CN = Alice`, signed by herself.

![Three clients connect to Bob's server bob.example: Alice with a certificate CN = Alice issued by Bob Staff CA; Alice with no certificate; Mallory with a certificate CN = Alice issued by "Alice", made by Mallory. For clients, the server trusts only Bob Staff CA. What does the server say to each? Steps: 1 trust the server's root, 2 load your certificate and key, 3 connect and read the answer.](figure.svg)

## Goal

Connect to Bob's server three times: as Alice with her certificate, without a certificate, and as Mallory, and print what happens.

## Ready for you

- `mtls_ready.py` (do not change it): `start_server()` starts Bob's server on 127.0.0.1 and returns its port. The server greets the client by the name in its certificate. `SERVER_ROOT` is the root that the client trusts for the server; `ALICE` and `MALLORY` are pairs `(certificate file, key file)`.
- `certs/`: all the certificates and keys.
- `client.py`: the three cases and the loop that prints the result of `log_in()`.

## Steps

Write your code in place of the `TODO` comments in `client.py`, in `log_in(cert_and_key)`:

1. Make a client context that trusts the server's root: `context = ssl.create_default_context(cafile=SERVER_ROOT)`.
2. If `cert_and_key` is not `None`, give the context our certificate and private key: `context.load_cert_chain(cert_and_key[0], cert_and_key[1])`.
3. Connect: `sock = socket.create_connection(("127.0.0.1", port))`, then `tls = context.wrap_socket(sock, server_hostname="bob.example")`, read the answer `tls.recv(100)` and return it as text (`.decode()`). On `ssl.SSLError` return `"rejected: " + e.reason`.

Until you write the code, every line says `not done yet: TODO 1`.

Hint: in TLS 1.3 the client sends its certificate at the end of the handshake, so `wrap_socket` may succeed and the rejection arrives only when you read. Put both `wrap_socket` and `recv` inside the same `try`.

## Expected output

Alice is let in; the other two are rejected, for two different reasons.

<details>
<summary>Check your answer</summary>

```
Alice           hello, Alice: you are logged in
no certificate  rejected: TLSV13_ALERT_CERTIFICATE_REQUIRED
Mallory         rejected: TLSV1_ALERT_UNKNOWN_CA
```

Mallory's certificate says `CN = Alice` too, but the server checks who issued it before it reads the name: the issuer is not Bob Staff CA, so the server answers with the alert `unknown_ca`.

</details>

## Run

```
python3 client.py
```

About 10 minutes. Python 3, standard library only (`ssl`, `socket`); works offline.
