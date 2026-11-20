# Task 5: OCSP and soft-fail

## The situation

Alice wants to know whether two certificates from **Trusty Issuing CA 1** are still good: Bob's (serial `0x1001`) and Carol's (serial `0x1002`, revoked on 10 November 2026). She asks the CA's OCSP responder, which sends back a signed answer: good, revoked or unknown. In the third case Carol's stolen key is in Mallory's hands, and Mallory, who sits between Alice and the network, simply drops Alice's question. What should Alice do when no answer comes? In the fourth case Mallory is smarter: she sends back an answer she recorded on 5 November, before the revocation. It says "good" and it really is signed by the CA, but it was valid only until 12 November.

![Alice's program ocsp_check.py and the OCSP responder of Trusty Issuing CA 1. Four questions: about bob.example serial 0x1001, about carol.example serial 0x1002, again about carol.example, but Mallory drops the request, and once more about carol.example, but Mallory answers with an answer she recorded on 5 Nov: good, signed by the CA, This Update 5 Nov 2026, Next Update 12 Nov 2026. 1 the request goes out as DER bytes, 2 a signed answer comes back. 3 is the answer still fresh? 4 good, revoked or unknown? 5 decide, with soft-fail and with hard-fail: accept or reject, for each of the four cases?](figure.svg)

## Goal

Ask the responder about the certificates, check the signed answer, then decide like a browser with two policies: soft-fail (no answer: accept) and hard-fail (no answer: reject).

## Ready for you

- `ocsp_ready.py` (do not change it):
  - `Responder`: the CA's OCSP responder, running inside your program (no network). `responder.ask(request_bytes)` takes the bytes of an OCSP request and returns the bytes of a signed OCSP response. `responder.mallory` says what Mallory does: `None` (nothing), `"blocks"` (`ask` raises `ConnectionError`, as if she dropped the request) or `"replays"` (`ask` returns her recorded old answer).
  - `response_signed_by(response, issuer)`: `True` if the response was signed with the issuer's private key.
  - `next_update_of(response)`: the Next Update of the answer; `NOW`: the time now. They can be compared with `<`.
  - `load_cert(filename)`, `name_of(cert)`.
- `ocsp_check.py`: the four cases and the loop that prints the result.
- From the `cryptography` library: `ocsp.OCSPRequestBuilder`, `ocsp.load_der_ocsp_response` and `ocsp.OCSPCertStatus`.

## Steps

Write your code in place of the `TODO` comments in `ocsp_check.py`:

1. In `ask_status`, build the request with `ocsp.OCSPRequestBuilder` (`add_certificate` needs the certificate, its issuer `ca` and `hashes.SHA1()`), then turn it into DER bytes with `public_bytes`. OCSP names a certificate by a SHA-1 hash of its issuer's name and key; this is not used for security.
2. Send the bytes with `responder.ask`; if it raises `ConnectionError`, return `None`. Read the answer with `ocsp.load_der_ocsp_response`; if `response_signed_by(response, ca)` is not `True`, return `None`.
3. **Freshness.** If `next_update_of(response)` is before `NOW`, return `None`: an answer that is too old is no answer, exactly like an old CRL in Task 4.
4. Compare `response.certificate_status` with `ocsp.OCSPCertStatus.GOOD`, `.REVOKED` and `.UNKNOWN`, and return `"good"`, `"revoked"` or `"unknown"`. This replaces the line `return "not done yet: TODO 1"`.
5. In `decide(status, policy)`: `"good"` gives `"accept"`; `"revoked"` and `"unknown"` give `"reject"`; no answer (`None`) gives `"accept"` for `"soft-fail"` and `"reject"` for `"hard-fail"`.

Until you write the code, every line says `not done yet`.

**Predict first:** without step 3, what would the fourth case give, with soft-fail and with hard-fail?

<details>
<summary>Hint: the calls of steps 1 and 2</summary>

```python
request = ocsp.OCSPRequestBuilder().add_certificate(cert, ca, hashes.SHA1()).build()
request_bytes = request.public_bytes(serialization.Encoding.DER)
try:
    answer = responder.ask(request_bytes)
except ConnectionError:
    return None
response = ocsp.load_der_ocsp_response(answer)
```

</details>

## Expected output

Four lines. Look at the last two: Carol's certificate is revoked, but what does soft-fail do?

<details>
<summary>Check your answer</summary>

```
bob.example                                   answer: good     soft-fail: accept  hard-fail: accept
carol.example                                 answer: revoked  soft-fail: reject  hard-fail: reject
carol.example  Mallory blocks OCSP            answer: None     soft-fail: accept  hard-fail: reject
carol.example  Mallory replays an old answer  answer: None     soft-fail: accept  hard-fail: reject
```

With soft-fail, one dropped question turns a revoked certificate into an accepted one; Mallory, who has Carol's key, is exactly the person who can drop it. The old answer is a real signature of the CA, so step 2 lets it through; only step 3 stops it. Without step 3 the last line says `answer: good`, and even hard-fail accepts. The request is 69 bytes; the answer is about 260 bytes for `good` and about 290 for `revoked` (an ECDSA signature is 70 to 72 bytes, so the size changes a little from run to run).

</details>

## Run

```
python3 ocsp_check.py
```

About 14 minutes. Python 3 and the `cryptography` library (version 41 or newer); works offline.
