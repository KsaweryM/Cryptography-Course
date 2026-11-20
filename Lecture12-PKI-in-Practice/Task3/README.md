# Task 3: four servers, two clients

## The situation

Bob's program talks to `shop.alice.example` over TLS. In testing the certificate check failed once, so somebody wrote `verify=False` and forgot it. Now Mallory is in the network. Four servers on your own computer (127.0.0.1) all answer "Welcome to Alice's shop": only one of them is the real shop.

![A laptop running client.py, which wants shop.alice.example and trusts Trusty CA. Four arrows with question marks go to four servers. Port 8443, the real shop: subject shop.alice.example, issuer Trusty CA, valid until 2045-09-01. Port 8444, Mallory: subject shop.alice.example, issuer itself (self-signed). Port 8445, Mallory: subject mallory.example, issuer Trusty CA. Port 8446, an old copy: subject shop.alice.example, issuer Trusty CA, valid until 2025-08-20. All four answer "Welcome to Alice's shop. Please log in." Which ones does a client with verify=False talk to? Which ones does a correct client refuse, and why?](figure.svg)

The certificates of the task were made on 2026-11-19. The three that should work are valid until 2045-09-01, so the task keeps working for years; a real public certificate lives at most 200 days (2026), and fewer later. The expired copy really expired on 2025-08-20.

## Goal

Connect to the four servers twice: first as the broken client, then as a correct one. See which servers each client accepts.

## Ready for you

- `servers.py`: `start_servers()` starts the four servers in the background, `PORTS` lists their ports, and `fetch(context, port)` connects with your `ssl.SSLContext`, asks for the page of `shop.alice.example` and returns the answer. If the certificate check fails, `fetch` raises `ssl.SSLCertVerificationError`.
- `certs/trusty-ca.pem`: the certificate of Trusty CA, the only CA this client should trust.
- Python's own `ssl` module. An `SSLContext` is the set of rules for a connection: which CAs to trust and what to check.

## Steps

Write your code in place of the `TODO` comments in `client.py`:

1. The broken client, which is what `verify=False` does: `broken = ssl.create_default_context()`, then `broken.check_hostname = False` and `broken.verify_mode = ssl.CERT_NONE`.
2. For every port in `PORTS`, print the port and `fetch(broken, port)`.
3. The correct client: `good = ssl.create_default_context(cafile="certs/trusty-ca.pem")`. It checks the chain, the dates and the name.
4. For every port, `try:` to print `fetch(good, port)`; `except ssl.SSLCertVerificationError as e:` print `refused:` and `e.verify_message`.

Each half of the file ends with a line that prints `not done yet: ...`; delete it when you have done those steps.

## Expected output

The broken client talks to all four servers. The correct one talks only to the real shop and gives a different reason for each of the other three.

<details>
<summary>Check your answer</summary>

```
The broken client (verify=False):
  8443 [the real shop] Welcome to Alice's shop. Please log in.
  8444 [Mallory, self-signed] Welcome to Alice's shop. Please log in.
  8445 [Mallory, her own name] Welcome to Alice's shop. Please log in.
  8446 [an expired copy] Welcome to Alice's shop. Please log in.
The correct client:
  8443 [the real shop] Welcome to Alice's shop. Please log in.
  8444 refused: self-signed certificate
  8445 refused: Hostname mismatch, certificate is not valid for 'shop.alice.example'.
  8446 refused: certificate has expired
```

The words in brackets are only there for this task: a real Mallory says exactly what the real shop says. With an older OpenSSL the second message reads `self signed certificate`. Port 8445 is the sneaky one: the certificate is real and signed by Trusty CA, but for another name, so only the name check catches it.

</details>

## Run

```
python3 client.py
```

About 12 minutes. Python 3 (the `ssl` module is built in). The servers use the ports 8443 to 8446; if one is busy, close the program that uses it.
