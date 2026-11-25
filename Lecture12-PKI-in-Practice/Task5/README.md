# Task 5: one signature, two certificates

## The situation

A CA does not sign a certificate as a whole: it signs the hash of its **tbsCertificate**, the part "to be signed" with all the fields (Lecture 9). If two different tbsCertificates have the same hash, one signature fits both. For MD5 such pairs are easy to make since 2004 (Lecture 7, Task 4).

Mallory prepared two tbsCertificates, A and B, that differ in only 6 of 306 bytes. A program that reads them shows two very different sentences: A is an ordinary website certificate, B makes Mallory a CA. She gets Trusty CA to sign the harmless A. Trusty CA signed A twice: once over MD5 (as some CAs still did in 2008) and once over SHA-256.

A real CA writes some fields itself, such as the serial number and the validity dates, so Mallory cannot prepare the bytes alone: she must guess exactly what the CA will write. In 2008 the researchers did exactly that (see the slide "2008: the rogue CA in PKI detail"). Here Trusty CA simply signs the bytes Mallory gives it.

![Two files of 306 bytes. tbs_a.bin: bytes 0 to 127 are strange bytes; the 6 that differ are 87, 71, f2, b4, a8, 2b at bytes 19, 45, 59, 83, 109, 123; then the text, the same in both, and a program shows: "shop.bob.example is a website. It may NOT sign certificates." tbs_b.bin: the 6 bytes are 07, f1, 72, 34, 28, ab, and the program shows: "Mallory is a CA. She may sign certificates for any website." Under each file: MD5 the same, SHA-256 different. Trusty CA signs A, RSA over MD5 and over SHA-256. Does the same signature fit B?](figure.svg)

The 128 strange bytes are the famous MD5 collision of Wang, Feng, Lai and Yu (2004), the pair from Lecture 7. In the real attack of 2008 the researchers computed their own collision for two certificates.

## Goal

Show that the MD5 signature over A is also a valid signature over B, and that the SHA-256 signature is not.

## Ready for you

- `trusty.py`: `load_file(path)`; `verify(data, signature, hash_name)` returns `True` if Trusty CA signed `data` with the hash `"md5"` or `"sha256"`; `what_it_says(data)` the sentence a program shows for a tbsCertificate.
- `tbs_a.bin`, `tbs_b.bin`, `signature_md5.bin`, `signature_sha256.bin` (both signatures are over A), `trusty-ca-public.pem`.
- In `collide.py`, already done (you did it in Lecture 7): the count of the bytes that differ and the MD5 and SHA-256 of A and B.

## Steps

Write your code in place of the `TODO` comments in `collide.py`, and delete the `not done yet` line under each TODO when it is done:

1. Check the MD5 signature on `a` and on `b`: `verify(a, sig_md5, "md5")`, `verify(b, sig_md5, "md5")`. Print both.
2. Do the same with `sig_sha256` and `"sha256"`.

Predict first: the MD5 of A and B is the same; will Trusty CA's MD5 signature over A fit B?

## Expected output

The MD5 signature fits both tbsCertificates, the SHA-256 signature only A.

<details>
<summary>Check your answer</summary>

```
A says: Trusty CA certifies: shop.bob.example is a website. It may NOT sign certificates.
B says: Trusty CA certifies: Mallory is a CA. She may sign certificates for any website.
bytes that differ: 6 of 306
MD5     A: c1ce19ef2bff14e3d0a24b79426459cb
MD5     B: c1ce19ef2bff14e3d0a24b79426459cb
SHA-256 A: f8a5fde58bf3b7ce9b524e114e238b9a0b5fde6e176e7293de577041dac7c9d0
SHA-256 B: 646d9bfca497b64a994b87635f48b7fc34976aa3fef739473010af36a1290e49
MD5 signature on A:     True
MD5 signature on B:     True
SHA-256 signature on A: True
SHA-256 signature on B: False
```

Trusty CA only ever saw A, yet its signature now makes B, Mallory's CA, look genuine. Simplified: in a real certificate the strange bytes hide inside the public key field, where nobody reads them, and the certificate's `CA:TRUE` flag does the job of the sentence.

</details>

## Run

```
python3 collide.py
```

About 5 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
