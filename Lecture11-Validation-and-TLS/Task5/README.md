# Task 5: OCSP and soft-fail

## The situation

Alice wants to know whether two certificates from **Trusty Issuing CA 1** are still good: Bob's (serial `0x1001`) and Carol's (serial `0x1002`, revoked on 10 November 2026). She asks the CA's OCSP responder, which sends back a signed answer: good, revoked or unknown. In the third case Carol's stolen key is in Mallory's hands, and Mallory, who sits between Alice and the network, simply drops Alice's question. What should Alice do when no answer comes?

![Alice's program ocsp_check.py and the OCSP responder of Trusty Issuing CA 1. Three questions: about bob.example serial 0x1001, about carol.example serial 0x1002, and again about carol.example, but this time Mallory drops the request. 1 the request goes out as DER bytes, 2 a signed answer comes back: good, revoked or unknown. 3 decide, with soft-fail and with hard-fail: accept or reject, for each of the three cases?](figure.svg)

## Goal

Ask the responder about the certificates, check the signed answer, then decide like a browser with two policies: soft-fail (no answer: accept) and hard-fail (no answer: reject).

## Ready for you

- `ocsp_ready.py` (do not change it):
  - `Responder`: the CA's OCSP responder, running inside your program (no network). `responder.ask(request_bytes)` takes the bytes of an OCSP request and returns the bytes of a signed OCSP response. When `responder.blocked` is `True`, `ask` raises `ConnectionError`, as if Mallory dropped the request.
  - `response_signed_by(response, issuer)`: `True` if the response was signed with the issuer's private key.
  - `load_cert(filename)`, `name_of(cert)`.
- `ocsp_check.py`: the three cases and the loop that prints the result.
- From the `cryptography` library: `ocsp.OCSPRequestBuilder`, `ocsp.load_der_ocsp_response` and `ocsp.OCSPCertStatus`.

## Steps

Write your code in place of the `TODO` comments in `ocsp_check.py`:

1. In `ask_status`, build the request and turn it into bytes:
   `request = ocsp.OCSPRequestBuilder().add_certificate(cert, ca, hashes.SHA1()).build()` and
   `request_bytes = request.public_bytes(serialization.Encoding.DER)`.
   (OCSP names a certificate by a SHA-1 hash of its issuer's name and key; this is not used for security.)
2. Send it: `answer = responder.ask(request_bytes)`; if it raises `ConnectionError`, return `None`. Read the answer with `response = ocsp.load_der_ocsp_response(answer)`; if `response_signed_by(response, ca)` is not `True`, return `None`. Then compare `response.certificate_status` with `ocsp.OCSPCertStatus.GOOD`, `.REVOKED` and `.UNKNOWN`, and return `"good"`, `"revoked"` or `"unknown"`.
3. In `decide(status, policy)`: `"good"` gives `"accept"`; `"revoked"` and `"unknown"` give `"reject"`; no answer (`None`) gives `"accept"` for `"soft-fail"` and `"reject"` for `"hard-fail"`.

## Expected output

Three lines. Look at the last one: Carol's certificate is revoked, but what does soft-fail do?

<details>
<summary>Check your answer</summary>

```
bob.example                         answer: good     soft-fail: accept  hard-fail: accept
carol.example                       answer: revoked  soft-fail: reject  hard-fail: reject
carol.example  Mallory blocks OCSP  answer: None     soft-fail: accept  hard-fail: reject
```

With soft-fail, one dropped question turns a revoked certificate into an accepted one; Mallory, who has Carol's key, is exactly the person who can drop it. The request is 69 bytes and the answer 263 bytes.

</details>

## Run

```
python3 ocsp_check.py
```

About 12 minutes. Python 3 and the `cryptography` library (version 41 or newer); works offline.
