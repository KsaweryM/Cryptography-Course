# Cryptography Course

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A hands-on course on **how modern ciphers work and how they break**, and on **how we know
whose public key we hold**.

The course has two parts. **Lectures 1 to 5** are about cryptography. **Lectures 6 to 9** are
about **PKI** (public key infrastructure): certificates, the authorities that sign them, how
programs check them, and how they are used and misused in practice.

The first part starts with **stream ciphers**: encrypting byte by byte with XOR and a keystream, and
the classic cipher **RC4**, followed step by step and then broken. It moves to the ciphers that
replaced it, **Salsa20 and ChaCha20**, and then to **public-key cryptography**: **RSA**,
**Diffie-Hellman** and **ElGamal**, and finally the same ideas on **elliptic curves**. Every
lecture has small tasks in **Python 3**: you measure, attack and repair real algorithms
instead of only reading about them.

- **Lecture 1** shows why a small sensor needs a **stream cipher**, builds one from XOR and a
  keystream (with the one-time pad as the ideal), and shows the mistake that removes the key:
  **using the same keystream twice**, and why encryption does not protect integrity. Then
  **RC4** from the inside, cell by cell (key scheduling and byte generation), its **biases**
  measured in Python, the **WEP** disaster and the end of RC4.
- **Lecture 2** makes a keystream from a **key, a nonce and a counter**, with only three
  operations on 32-bit words: **add, rotate, XOR**. It shows **Salsa20** briefly and
  **ChaCha20** in full (the 4 by 4 state, quarter rounds, 20 rounds), why twenty rounds, why it
  is fast on any processor, and **ChaCha20-Poly1305**, which also protects integrity.
- **Lecture 3** starts from the problems of one shared key and solves them with a **key pair**.
  It explains the hard problems behind public-key cryptography (factoring, the discrete
  logarithm), **arithmetic modulo n**, **RSA** keys and encryption, and why real RSA needs
  randomness (OAEP). Euclid's algorithm and fast powers are explained step by step in the
  simulators (see below).
- **Lecture 4** agrees on a secret in public with **Diffie-Hellman**, shows why it is safe while
  the discrete logarithm is hard, the **man in the middle** and forward secrecy. Then
  **ElGamal** encryption, and what happens when the random number is reused.
- **Lecture 5** shows why **elliptic curves** give the same safety with keys about 12 times
  shorter: points on a curve modulo p, **adding points** by hand, **scalar multiplication** and
  the ECDLP, **ECDH** and ElGamal on a small curve, then **X25519** with HKDF.

The second part starts where public-key cryptography leaves a gap: a public key does not say
whose it is.

- **Lecture 6** shows how **Mallory in the middle** swaps a public key, and how a signed name
  card stops her: a **certificate**. It opens the **X.509** format field by field (serial,
  issuer, subject, validity, the public key) and its **extensions** (SAN and wildcards, Basic
  Constraints, Key Usage, key identifiers), the **DER** and **PEM** encodings, the
  **fingerprint**, **self-signed** certificates and the real certificate of
  www.coventry.ac.uk.
- **Lecture 7** follows a **chain of trust** from a real website through an intermediate to a
  root in the **trust store**, and shows who the **certificate authorities** are and who
  checks them. You build a small PKI of your own and see what stops a CA from signing too much
  (**Basic Constraints**, pathLen, Name Constraints). Then the life of a certificate: the key
  pair, the **CSR**, **DV, OV and EV** checks, issuance, **Certificate Transparency** logs,
  **ACME** and Let's Encrypt, renewal and ever shorter validity.
- **Lecture 8** checks a chain the way a browser does: **path building** and **six checks**
  (signatures, dates, the name, may it sign, what the key is for, a trust anchor). Then
  **revocation**: CRL, OCSP, soft-fail, stapling, CRLite and short-lived certificates. Finally
  certificates in the **TLS 1.3 handshake** (Certificate and CertificateVerify), **mutual TLS**
  for clients, and **pinning** in apps.
- **Lecture 9** shows PKI beyond the padlock: **code signing** with timestamps, signed **PDF
  documents**, **S/MIME** mail and **logging in with a certificate**. Then five good
  practices and the usual mistakes (unprotected keys, turning validation off, forgotten
  renewals, weak algorithms, no inventory), and real **incidents** (the MD5 collision, Flame,
  Comodo, DigiNotar, Symantec, expired certificates) with the lessons they brought: CT, CAA and
  shorter certificates.

The first part does not teach digital signatures. The second part uses them as a black box
(sign and verify), with a short Recall slide.

Author: **Ksawery Możdżyński**

---

## Course Structure

The course is divided into nine lectures in two parts: cryptography (1 to 5) and PKI (6 to 9).

| # | Title | Topics |
|---|-------|--------|
| **1** | Stream Ciphers and RC4 | Block vs. stream, XOR, one-time pad, keystream, keystream reuse, bit flipping and integrity, RC4 (KSA and PRGA), brute force, biases, WEP, nonces, the end of RC4 |
| **2** | Salsa20 and ChaCha20 | Keystream from a counter, nonce, add-rotate-XOR, Salsa20, the ChaCha20 state and quarter round, 20 rounds and diffusion, speed without special hardware, ChaCha20-Poly1305 |
| **3** | Public-Key Cryptography and RSA | Problems of a shared key, key pairs, hybrid encryption, factoring and the discrete logarithm, arithmetic modulo n, the modular inverse, RSA keys and encryption, OAEP |
| **4** | Diffie-Hellman and ElGamal | Agreeing on a key in public, Diffie-Hellman, the discrete logarithm, ephemeral keys and forward secrecy, the man in the middle, ElGamal encryption, reusing k |
| **5** | Elliptic-Curve Cryptography | Why shorter keys, curves modulo p, point addition and doubling, scalar multiplication, the ECDLP, ECDH and X25519, HKDF, ElGamal on a curve, key sizes and speed |
| **6** | Why PKI and the X.509 Certificate | Mallory in the middle, a signed name card, certificate authorities, X.509 and tbsCertificate, names, validity, the public key, extensions (SAN, wildcards, Basic Constraints, Key Usage, EKU, SKI and AKI), DER, PEM, fingerprints, self-signed certificates, a real certificate |
| **7** | Certificate Authorities and the Certificate Lifecycle | CAs and who checks them, root, intermediate and leaf, checking a chain, trust stores and root programs, cross-signing, Basic Constraints, pathLen, Name Constraints, private PKI, CSR, DV, OV and EV, Certificate Transparency and SCTs, ACME and Let's Encrypt, renewal and shorter validity |
| **8** | Validation, Revocation and Certificates in TLS | Validation as a black box, path building, missing intermediates, six checks, typical errors, CRL, OCSP, soft-fail, stapling, Must-Staple, CRLite, short-lived certificates, the TLS 1.3 handshake, CertificateVerify, mutual TLS, pinning |
| **9** | PKI in Practice: Good Practices and Incidents | Extended Key Usage, code signing and timestamps, signed PDFs and eIDAS, S/MIME, client certificates and 802.1X, protecting private keys (files, TPM, HSM), never turning validation off, automatic renewal, weak algorithms, inventories, incidents from MD5 to Symantec, CT, CAA, shorter certificates |

Lectures 1 to 5 take about 130 to 145 minutes each, Lectures 6 to 9 about 170 minutes each,
tasks included.

---

## Simulators

The slides link to interactive pages that show each algorithm step by step:
https://ksawerym.github.io/Cryptography-simulators/ (RC4, ChaCha20, RSA, Diffie-Hellman,
elliptic curves, and the mathematics behind them). Some demos in the lectures are run there.

Lectures 6 to 9 link to the **PKI simulator**:
https://ksawerym.github.io/Cryptography-simulators/pki/. It tells the Mallory story, opens
real certificates field by field down to the DER bytes, builds and checks chains of trust,
shows revocation, the TLS 1.3 handshake with mutual TLS, and pinning.

---

## Tasks

Every task has its own folder `LectureN/TaskK/` with a `README.md` and a starter file with
`TODO` lines. A few tasks are on paper and have no folder.

- Lectures 1 to 5: Python 3.8 or newer, **nothing to install**: the tasks use only the standard library.
- Lectures 6 to 9: Python 3 and one library, `cryptography` (version 41 or newer):
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
- [Lecture 6: Why PKI and the X.509 Certificate](builded_presentation/Lecture_6_Why_PKI_and_the_X.509_Certificate.pdf)
- [Lecture 7: Certificate Authorities and the Certificate Lifecycle](builded_presentation/Lecture_7_Certificate_Authorities_and_the_Certificate_Lifecycle.pdf)
- [Lecture 8: Validation, Revocation and Certificates in TLS](builded_presentation/Lecture_8_Validation_Revocation_and_Certificates_in_TLS.pdf)
- [Lecture 9: PKI in Practice: Good Practices and Incidents](builded_presentation/Lecture_9_PKI_in_Practice_Good_Practices_and_Incidents.pdf)

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
Each lecture folder also has its own `Makefile` (`make` inside `Lecture4/` builds only that lecture).

---

## Who is this for?

- Students taking their first course on cryptography
- Programmers who use encryption libraries and want to understand what happens inside them
- Teachers looking for ready-made, hands-on slides with exercises

No prior cryptography knowledge is assumed. Short "Recall" slides explain hex, XOR and
modular arithmetic when they are needed, and in the PKI part key pairs, hashes and signatures.

---

## License

© Ksawery Możdżyński. The slides, their LaTeX sources and the PDFs in this repository are licensed under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to use, share and adapt the material for any purpose, including teaching and commercial use,
as long as you give appropriate credit, provide a link to the license and indicate if changes were made.
A suggested attribution:

> "Cryptography Course" by Ksawery Możdżyński, licensed under CC BY 4.0.

If you find the course useful, a star ⭐ is always appreciated!
