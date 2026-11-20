# Task 6: CertificateVerify by hand

## The situation

In a TLS 1.3 handshake the server sends its certificate, then a **CertificateVerify** message: a signature, made with the private key of its certificate, over the hash of all handshake messages so far (the transcript hash). Alice is in the middle of a handshake with a server that says it is `bob.example`. You have three recorded CertificateVerify signatures: one from Bob's real server, one from Mallory, who sends a copy of Bob's certificate but has only her own key, and one that Mallory recorded from Bob's server yesterday and now replays.

![The 130 bytes that a TLS 1.3 server signs: 64 spaces (0x20), the 33 bytes "TLS 1.3, server CertificateVerify", one zero byte, and the 32-byte transcript hash 9483...556a. TODO 1: build these 130 bytes. Bob's certificate bob.pem gives the public key. Three signatures: Bob, today; Mallory, with a copy of Bob's certificate; Mallory, replaying Bob's signature from yesterday. TODO 2 and 3: verify each one.](figure.svg)

## Goal

Build the exact bytes that a TLS 1.3 server signs (RFC 9846, section 4.5.2; in the older RFC 8446, section 4.4.3) and check the three signatures with the public key from Bob's certificate.

## Ready for you

- `handshake_ready.py` (do not change it): `BOB_CERT` (Bob's certificate, the one all three servers sent), `transcript_hash` (32 bytes, the hash of today's handshake so far) and `MESSAGES`, a list of `(who, signature)`.
- `files/`: Bob's certificate and the recorded values.
- `certificate_verify.py`: the frame of the program.

## Steps

Write your code in place of the `TODO` comments in `certificate_verify.py`:

1. In `signed_content(th)`: return 64 spaces, then `b"TLS 1.3, server CertificateVerify"`, then one zero byte `b"\x00"`, then the transcript hash `th`. In Python, `b" " * 64` is 64 spaces and `+` joins byte strings.
2. In `signature_ok(signature, content)`: verify the signature with the public key of `BOB_CERT` (`public_key().verify`, ECDSA with SHA-256, as in Lecture 8). `verify` returns nothing if the signature is good and raises `InvalidSignature` if it is not: return `True` or `False`.
3. At the end: for every `(who, signature)` in `MESSAGES`, print who sent it and `signature OK` or `signature BAD`, in place of the line `print("not done yet: TODO 3")`.

Until you write the code, the program prints `not done yet: TODO 1` and `not done yet: TODO 3`.

<details>
<summary>Hint: the call of step 2</summary>

```python
try:
    BOB_CERT.public_key().verify(signature, content, ec.ECDSA(hashes.SHA256()))
    return True
except InvalidSignature:
    return False
```

</details>

## Expected output

The content is 130 bytes; only one of the three signatures is good.

<details>
<summary>Check your answer</summary>

```
signed content: 130 bytes
bytes 64 to 97: b'TLS 1.3, server CertificateVerify\x00'
Bob, today                           signature OK
Mallory with Bob's certificate       signature BAD
Mallory replays Bob's old signature  signature BAD
```

A certificate is public, so Mallory can copy it, but without Bob's private key she cannot sign. A recorded signature does not help either: it was made over another transcript, and the transcript of every handshake contains fresh random values. The 64 spaces and the text with the word `server` stop a signature from being reused in another protocol or by the other side (a client signs `TLS 1.3, client CertificateVerify`).

</details>

## Run

```
python3 certificate_verify.py
```

About 10 minutes. Python 3 and the `cryptography` library (version 41 or newer); works offline.
