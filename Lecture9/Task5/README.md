# Task 5: PEM by hand

## The situation

`bob.pem` is a text file: Base64 between a `BEGIN CERTIFICATE` line and an `END CERTIFICATE` line. Under the text are the DER bytes of the certificate, and the SHA-256 of those bytes is its fingerprint. Usually a library does all this for you; here you do it yourself and compare.

![The text of bob.pem: the BEGIN line, Base64 lines starting with MIIBITCB1KADAgECAghPOpwu..., the END line. Steps 1 and 2 (join the lines, Base64 decode) give the DER bytes 30 82 01 21 30 81 D4 A0 ..., 293 bytes. Step 3: the same as the library? Step 4: SHA-256 gives the fingerprint E8:C5:56:C2:... Step 5: flip one bit of byte 100: how many of the 32 bytes of the fingerprint change?](figure.svg)

## Goal

Turn `bob.pem` into DER bytes yourself, compute its SHA-256 fingerprint, then change one bit and compute it again.

Predict first: if one bit of the certificate changes, how many of the 32 bytes of the fingerprint change?

## Ready for you

- `bob.pem`: the certificate of `bob.example`, issued by Trusty CA (the same as the result of Task 3).
- `cert_tools.py`: `load_cert(path)` reads a certificate with the library.
- In `pem_by_hand.py`: `lines`, the list of the lines of `bob.pem`, without `"\n"`.
- Python's `base64.b64decode(text)` (text to bytes) and `hashlib.sha256(data).digest()` (32 bytes).

## Steps

Write your code in place of the `TODO` comments in `pem_by_hand.py`:

1. Join the Base64 lines into one text: loop over `lines` and skip the lines that start with five hyphens (`line.startswith("-----")`). Print how many characters you got.
2. Decode it: `der = base64.b64decode(b64)`. Print `len(der)` and the first 8 bytes as hex, one byte at a time with `"%02X " % der[i]` (the same as `printf("%02X ", der[i])` in C).
3. Compare with the library: `cert = load_cert("bob.pem")`, then print `der == cert.public_bytes(serialization.Encoding.DER)`.
4. The fingerprint: `fp = hashlib.sha256(der).digest()`. Print it as hex with `:` between the bytes, and also `cert.fingerprint(hashes.SHA256())` in the same way.
5. Change one bit: `copy = bytearray(der)` (a list of bytes you may change), then `copy[100] = copy[100] ^ 1`. Print the fingerprint of `bytes(copy)` and count how many of its 32 bytes differ from `fp`.

## Expected output

The number of Base64 characters and of DER bytes, the first bytes, `True`, two equal fingerprints, and a new fingerprint after the change.

<details>
<summary>Check your answer</summary>

```
Base64 characters: 392
DER bytes: 293  first 8: 30 82 01 21 30 81 D4 A0 
same as the library: True
fingerprint by hand: E8:C5:56:C2:D8:3E:72:C3:FB:F0:53:83:64:04:97:A0:A6:72:48:1B:86:79:A6:F4:CB:82:B0:8E:11:71:F8:1C
fingerprint library: E8:C5:56:C2:D8:3E:72:C3:FB:F0:53:83:64:04:97:A0:A6:72:48:1B:86:79:A6:F4:CB:82:B0:8E:11:71:F8:1C
one bit changed:     A2:C3:4F:BA:8C:D0:59:AB:D3:3F:CB:3B:9F:E4:F1:64:32:63:79:53:4D:77:1D:7F:62:4B:8C:52:74:F2:EC:FC
bytes changed: 32 of 32
```

`30 82 01 21`: a SEQUENCE whose length is in the next 2 bytes, `0x0121` = 289, so 4 + 289 = 293 bytes. Byte 100 is a digit of the start time: `00:00` became `00:10`. One bit, and every byte of the fingerprint changed (now and then one byte stays the same by chance).

</details>

## Run

```
python3 pem_by_hand.py
openssl x509 -in bob.pem -noout -fingerprint -sha256
```

About 10 minutes. Python 3 and the library `cryptography` (version 41 or newer). The second command is optional: OpenSSL computes the same fingerprint.
