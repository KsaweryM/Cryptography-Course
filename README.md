# Cryptography Course

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A hands-on course on **how modern ciphers work and how they break**.

The course starts with **stream ciphers**: encrypting byte by byte with XOR and a keystream, and
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
  logarithm), **arithmetic modulo n** and Euclid's algorithm, **RSA** keys, encryption and
  **digital signatures**, and why real RSA needs padding (OAEP, PSS).
- **Lecture 4** agrees on a secret in public with **Diffie-Hellman**, shows why it is safe while
  the discrete logarithm is hard, the **man in the middle** and forward secrecy. Then
  **ElGamal** encryption and signatures, and what happens when the random number is reused.
- **Lecture 5** shows why **elliptic curves** give the same safety with keys about 12 times
  shorter: points on a curve modulo p, **adding points** by hand, **scalar multiplication** and
  the ECDLP, **ECDH and X25519** with HKDF, ElGamal and **ECDSA** on a curve, and the famous
  case of a games console that reused one random number in every signature.

Author: **Ksawery Możdżyński**

---

## Course Structure

The course is divided into five lectures:

| # | Title | Topics |
|---|-------|--------|
| **1** | Stream Ciphers and RC4 | Block vs. stream, XOR, one-time pad, keystream, keystream reuse, bit flipping and integrity, RC4 (KSA and PRGA), brute force, biases, WEP, nonces, the end of RC4 |
| **2** | Salsa20 and ChaCha20 | Keystream from a counter, nonce, add-rotate-XOR, Salsa20, the ChaCha20 state and quarter round, 20 rounds and diffusion, speed without special hardware, ChaCha20-Poly1305 |
| **3** | Public-Key Cryptography and RSA | Problems of a shared key, key pairs, hybrid encryption, factoring and the discrete logarithm, arithmetic modulo n, Euclid's algorithm, RSA keys, encryption and signatures, OAEP and PSS |
| **4** | Diffie-Hellman and ElGamal | Agreeing on a key in public, Diffie-Hellman, the discrete logarithm, ephemeral keys and forward secrecy, the man in the middle, ElGamal encryption and signatures, reusing k |
| **5** | Elliptic-Curve Cryptography | Why shorter keys, curves modulo p, point addition and doubling, scalar multiplication, the ECDLP, ECDH and X25519, HKDF, ElGamal and ECDSA on a curve, key sizes and speed |

Each lecture takes about 130 to 145 minutes, tasks included.

---

## Tasks

Every task has its own folder `LectureN/TaskK/` with a `README.md` and a starter file with
`TODO` lines. A few tasks are on paper and have no folder.

- Python 3.8 or newer, **nothing to install**: the tasks use only the standard library.
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
modular arithmetic when they are needed.

---

## License

© Ksawery Możdżyński. The slides, their LaTeX sources and the PDFs in this repository are licensed under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to use, share and adapt the material for any purpose, including teaching and commercial use,
as long as you give appropriate credit, provide a link to the license and indicate if changes were made.
A suggested attribution:

> "Cryptography Course" by Ksawery Możdżyński, licensed under CC BY 4.0.

If you find the course useful, a star ⭐ is always appreciated!
