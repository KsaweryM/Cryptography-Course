# Task 1: six servers, one name

## The situation

Alice's program wants to talk to `bob.example`. Six servers on this computer (127.0.0.1) all claim to be `bob.example`, and each one sends a different certificate: a good one, an expired one, one for another name, one from Mallory's own CA, a self-signed one, and the good one without its intermediate. Alice trusts only one root, the **Trusty Root CA**. Python's `ssl` module (which uses OpenSSL) will do the whole validation for you: treat it as a black box and see what it says about each server.

![Alice's program connect.py asks for bob.example, with a trust store that holds only Trusty Root CA. Six servers on 127.0.0.1: good sends bob.example and Trusty Issuing CA 1; expired sends bob.example with notAfter 1 Oct 2026 and the intermediate; wrong_name sends carol.example and the intermediate; unknown_ca sends bob.example issued by Mallory Root CA; self_signed sends bob.example issued by itself; no_intermediate sends bob.example without the intermediate. For each server: OK, or why not?](figure.svg)

## Goal

Connect to the six servers and print, for each one, whether Python accepts its certificate, and if not, why.

## Ready for you

- `servers.py` (do not change it): `start_servers()` starts the six servers in the background and returns a list of `(name, port)`. `ROOT_CA` is the path of `certs/root.pem`, the trust store of this task.
- `certs/`: the certificates and keys of the servers.
- `connect.py`: the loop over the servers is ready; it opens a TCP connection `sock` to each one.

## Steps

Write your code in place of the `TODO` comments in `connect.py`:

1. Make a TLS client context that trusts only our root: `context = ssl.create_default_context(cafile=ROOT_CA)`.
2. Start TLS on `sock`, asking for the name `bob.example`: `tls = context.wrap_socket(sock, server_hostname="bob.example")`. If it works, print the server's name, `OK` and `tls.version()`, then `tls.close()`.
3. If the certificate is rejected, `wrap_socket` raises `ssl.SSLCertVerificationError`. Catch it and print the server's name and `e.verify_message`, then `sock.close()`.

Hints:

- A Python function reports an error by raising an exception, not by returning an error code:

```python
try:
    tls = context.wrap_socket(sock, server_hostname="bob.example")
    print("%-16s OK, %s" % (label, tls.version()))
    tls.close()
except ssl.SSLCertVerificationError as e:
    print("%-16s REJECTED: %s" % (label, e.verify_message))
    sock.close()
```

- `"%-16s" % label` works like `printf("%-16s", label)` in C.

## Expected output

Six lines: one server is accepted, five are rejected. Look at the two lines that give the same reason.

<details>
<summary>Check your answer</summary>

```
good             OK, TLSv1.3
expired          REJECTED: certificate has expired
wrong_name       REJECTED: Hostname mismatch, certificate is not valid for 'bob.example'.
unknown_ca       REJECTED: unable to get local issuer certificate
self_signed      REJECTED: self-signed certificate
no_intermediate  REJECTED: unable to get local issuer certificate
```

`unknown_ca` and `no_intermediate` give the same message: in both cases the validator could not build a path to a root in the trust store. In the first case there is no such path; in the second the server forgot to send a certificate.

</details>

## Run

```
python3 connect.py
```

About 8 minutes. Python 3, standard library only (`ssl`, `socket`); works offline.
