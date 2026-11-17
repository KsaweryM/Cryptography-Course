# Cryptography Course

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A hands-on course on **how modern ciphers work and how they break**, how **hash functions and
digital signatures** protect data, and how we know **whose public key we hold**.

The course has three parts: **ciphers** (Lectures 1 to 5), **hash functions and signatures** (Lectures 6
to 8) and **PKI**, public key infrastructure (Lectures 9 to 12). Every lecture has small tasks in
**Python 3**: you measure, attack and repair real algorithms instead of only reading about them.

Author: **Ksawery Możdżyński**

---

## Course Structure

| # | Title | What it covers |
|---|-------|----------------|
| **1** | Stream Ciphers and RC4 | A keystream XORed with the data, the one-time pad, and what goes wrong when a keystream is reused. RC4 from the inside, its biases and the WEP disaster. |
| **2** | Salsa20 and ChaCha20 | A keystream from a key, a nonce and a counter with only add, rotate and XOR. ChaCha20 in full and ChaCha20-Poly1305, which also protects integrity. |
| **3** | Public-Key Cryptography and RSA | The problems of one shared key, solved with a key pair and hybrid encryption. Factoring, arithmetic modulo n, RSA keys and encryption, and why real RSA needs OAEP. |
| **4** | Diffie-Hellman and ElGamal | Agreeing on a secret in public, the discrete logarithm, forward secrecy and the man in the middle. ElGamal encryption and what happens when its random number is reused. |
| **5** | Elliptic-Curve Cryptography | Why curves give the same safety with keys about 12 times shorter: adding points, scalar multiplication and the ECDLP. ECDH and ElGamal on a small curve, then X25519 with a key derivation. |
| **6** | Hash Functions | What a hash function is, its properties (avalanche, preimage and collision resistance) and what it is used for. MD5, SHA-1 and SHA-256: how they are built and which are still safe. |
| **7** | Breaking Hashes: Collisions and Passwords | The birthday paradox and real collisions in MD5 and SHA-1. Storing passwords safely: dictionary attacks, salt and bcrypt. |
| **8** | Digital Signatures | Why a hash or a MAC does not prove who wrote a message, and how a signature does. RSA signatures, hash-and-sign, Ed25519 and ECDSA, and what a signature guarantees. |
| **9** | Why PKI and the X.509 Certificate | How Mallory swaps a public key and how a certificate stops her. The X.509 format field by field, its encodings and a real certificate. |
| **10** | Certificate Authorities and the Certificate Lifecycle | Chains of trust, trust stores and who checks the CAs. The life of a certificate from the CSR to Certificate Transparency, ACME and renewal. |
| **11** | Validation, Revocation and Certificates in TLS | How a browser checks a chain and what revocation can and cannot do. Certificates in the TLS 1.3 handshake, mutual TLS and pinning. |
| **12** | PKI in Practice: Good Practices and Incidents | Code signing, signed documents, S/MIME and client certificates. Good practices, common mistakes and real incidents from MD5 to Symantec. |

Lectures 1 to 5 take about 130 to 145 minutes each, Lectures 6 to 8 about 220 minutes each and
Lectures 9 to 12 about 170 minutes each, tasks included.

---

## Simulators

The slides link to interactive pages that show the hard parts step by step:
https://ksawerym.github.io/Cryptography-simulators/

---

## Tasks

Every task has its own folder `LectureN/TaskK/` with a `README.md` and a starter file with
`TODO` lines. A few tasks are on paper and have no folder.

- Lectures 1 to 7: Python 3.8 or newer, **nothing to install**: the tasks use only the standard library.
- Lectures 8 to 12: Python 3 and one library, `cryptography` (version 41 or newer):
  `pip install cryptography`. The tasks work offline, with ready PEM files in the task folders.
- Each task stands on its own: if one does not work out, the next one still does.
- Solutions are discussed during the lecture and are not published in this repository.

---

## Pre-built PDFs

Ready-to-use presentation slides are available in the [`builded_presentation/`](builded_presentation/) folder:

- [Lecture 1: Stream Ciphers and RC4](builded_presentation/Lecture_1_Stream_Ciphers_and_RC4.pdf)
- [Lecture 2: Salsa20 and ChaCha20](builded_presentation/Lecture_2_Salsa20_and_ChaCha20.pdf)
- [Lecture 3: Public-Key Cryptography and RSA](builded_presentation/Lecture_3_Public_Key_Cryptography_and_RSA.pdf)
- [Lecture 4: Diffie-Hellman and ElGamal](builded_presentation/Lecture_4_Diffie-Hellman_and_ElGamal.pdf)
- [Lecture 5: Elliptic-Curve Cryptography](builded_presentation/Lecture_5_Elliptic-Curve_Cryptography.pdf)
- [Lecture 6: Hash Functions](builded_presentation/Lecture_6_Hash_Functions.pdf)
- [Lecture 7: Breaking Hashes: Collisions and Passwords](builded_presentation/Lecture_7_Breaking_Hashes_Collisions_and_Passwords.pdf)
- [Lecture 8: Digital Signatures](builded_presentation/Lecture_8_Digital_Signatures.pdf)
- [Lecture 9: Why PKI and the X.509 Certificate](builded_presentation/Lecture_9_Why_PKI_and_the_X.509_Certificate.pdf)
- [Lecture 10: Certificate Authorities and the Certificate Lifecycle](builded_presentation/Lecture_10_Certificate_Authorities_and_the_Certificate_Lifecycle.pdf)
- [Lecture 11: Validation, Revocation and Certificates in TLS](builded_presentation/Lecture_11_Validation_Revocation_and_Certificates_in_TLS.pdf)
- [Lecture 12: PKI in Practice: Good Practices and Incidents](builded_presentation/Lecture_12_PKI_in_Practice_Good_Practices_and_Incidents.pdf)

---

## Building the presentations yourself

Requirements:
- `latexmk`
- A full TeX distribution (TeX Live / MiKTeX) with Beamer and the usual packages (`tikz`, `pgfplots`, `fontawesome5`, `listings`, etc.)

```bash
# Build everything
make

# Build a single lecture, by its number
make 4

# Build one lecture from scratch, even if nothing changed
make rebuild-4

# List the available lectures
make list

# Clean auxiliary files and PDFs
make clean
```

The Makefile automatically places the resulting PDFs in `builded_presentation/`.
Each lecture folder also has its own `Makefile` (`make` inside `Lecture04-Diffie-Hellman/` builds only that lecture).

---

## Who is this for?

- Students taking their first course on cryptography
- Programmers who use encryption libraries and want to understand what happens inside them
- Teachers looking for ready-made, hands-on slides with exercises

No prior cryptography knowledge is assumed. Short "Recall" slides explain hex, XOR and
modular arithmetic when they are needed, and later key pairs, hashes and signatures.

---

## License

© Ksawery Możdżyński. The slides, their LaTeX sources and the PDFs in this repository are licensed under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to use, share and adapt the material for any purpose, including teaching and commercial use,
as long as you give appropriate credit, provide a link to the license and indicate if changes were made.
A suggested attribution:

> "Cryptography Course" by Ksawery Możdżyński, licensed under CC BY 4.0.

If you find the course useful, a star ⭐ is always appreciated!
