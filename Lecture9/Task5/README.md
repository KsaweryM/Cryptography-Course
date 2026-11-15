# Task 5: one signature, two documents

## The situation

A CA never signs a whole certificate directly: it signs its **hash**. If two different documents have the same hash, one signature fits both. For MD5 such pairs are easy to make since 2004.

Mallory prepared two requests, A and B, that differ in only 6 of 308 bytes. A program that reads them shows two very different sentences: A asks for an ordinary website certificate, B makes Mallory a CA. She sends the harmless A to Trusty CA, which signs it. Trusty CA signed A twice: once over MD5 (as some CAs still did in 2008) and once over SHA-256.

![Two files of 308 bytes. request_a.bin: bytes 0 to 127 are strange bytes; the 6 that differ are 87, 71, f2, b4, a8, 2b at bytes 19, 45, 59, 83, 109, 123; then the text, the same in both, and a program shows: "shop.alice.example is a website. It may NOT sign certificates." request_b.bin: the 6 bytes are 07, f1, 72, 34, 28, ab, and the program shows: "Mallory is a CA. She may sign certificates for any website." Under each file: MD5 = ? and SHA-256 = ?. Trusty CA signs A, RSA over MD5 and over SHA-256. Does the same signature fit B?](figure.svg)

The 128 strange bytes are the famous MD5 collision of Wang, Feng, Lai and Yu (2004). In the real attack of 2008 the researchers computed their own collision for two certificates.

## Goal

Show that the MD5 signature over A is also a valid signature over B, and that the SHA-256 signature is not.

## Ready for you

- `trusty.py`: `load_file(path)`; `verify(data, signature, hash_name)` returns `True` if Trusty CA signed `data` with the hash `"md5"` or `"sha256"`; `what_it_says(data)` the sentence a program shows for a request.
- `request_a.bin`, `request_b.bin`, `signature_md5.bin`, `signature_sha256.bin` (both signatures are over A), `trusty-ca-public.pem`.
- Python's `hashlib`: `hashlib.md5(data).hexdigest()` and `hashlib.sha256(data).hexdigest()` return the hash as hex text.

## Steps

Write your code in place of the `TODO` comments in `collide.py`:

1. Count the bytes where `a` and `b` differ: an index loop over `range(len(a))`, as in C. Print the count.
2. Print the MD5 and the SHA-256 of `a` and of `b`.
3. Check the MD5 signature on `a` and on `b`: `verify(a, sig_md5, "md5")`, `verify(b, sig_md5, "md5")`. Print both.
4. Do the same with `sig_sha256` and `"sha256"`.

## Expected output

The same MD5, different SHA-256; the MD5 signature fits both requests, the SHA-256 signature only A.

<details>
<summary>Check your answer</summary>

```
A says: Trusty CA certifies: shop.alice.example is a website. It may NOT sign certificates.
B says: Trusty CA certifies: Mallory is a CA. She may sign certificates for any website.
bytes that differ: 6 of 308
MD5     A: 7e58325ffced260e7cf07eb336bf0907
MD5     B: 7e58325ffced260e7cf07eb336bf0907
SHA-256 A: 99cfc680cafeeddc57c0d92de1c79bfc418ddad3676da15d4b17ae94ab3f991e
SHA-256 B: 748ac700ab50682b30ec1dfcc89aa2898d2ef9cf15aad984faef9ca25c20cb9b
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

About 8 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
