# Task 1: is this update still trusted?

## The situation

Bob uses PhotoEdit, a program by Alice Software Ltd. His computer has five files that say they come from Alice: an installer, three updates and a copy of the installer from a mirror site. Each file carries Alice's **signature**, made with the private key of her code signing certificate. That certificate expired on 2025-01-01, so today, long after it expired, the certificate alone cannot tell Bob whether to trust a file.

Most files also carry a **timestamp**: a Time-Stamping Authority (TSA), Trusty Time Stamping, signed "this signature existed at this time". If that time is inside the validity period of Alice's certificate, the file was signed while the certificate was good, and it stays trusted.

![A time axis from 2024 to 2027. Alice's certificate (Alice Software Ltd, code signing) is valid from 2024-01-01 to 2025-01-01; a dashed line marks "expired". Five files on the left, each on its own line to "today: Bob installs" at the end of 2026, each with a question mark. photoedit-2.1-setup.exe has a TSA stamp at 2024-06-12. photoedit-2.2-update.exe has no timestamp: signed some time, we do not know when. photoedit-2.3-update.exe has a TSA stamp at 2025-03-02. photoedit-2.4-update.exe: the stamp says 2024-05-20, but Mallory edited the time in the token. photoedit-2.1-setup-mirror.exe: a TSA stamp at 2024-06-12; a mirror site, same signature, changed bytes.](figure.svg)

## Goal

Decide for each of the five files: accept it or reject it, and say why.

## Ready for you

- `codesign.py`: the checks as a black box.
  - `verify_signature(cert, data, signature)` returns `True` if the signature over `data` was made with the private key of `cert`.
  - `verify_timestamp(tsa_cert, signature, token)` returns the time written in the token (a `datetime`) if the TSA really signed it, or `None` if not.
  - `valid_from(cert)` and `valid_until(cert)` give the validity period; `NOW` is the current time.
  - `load_cert(path)` and `load_updates(path)`. Each update is a `dict`, like a C `struct` with named fields: `u["file"]`, `u["data"]`, `u["signature"]`, `u["timestamp"]` (`None` if there is none).
- `publisher.pem`: Alice's certificate. `tsa.pem`: the certificate of Trusty Time Stamping. Both chains to Trusty Code CA are already checked.
- `updates.json`: the five files with their signatures and timestamps.

## Steps

Write your code in place of the `TODO` comments in `check_updates.py`, inside the loop over the files:

1. Check Alice's signature over `u["data"]`. If it is wrong: `REJECT: bad signature`, then `continue` (as in C) to the next file.
2. No timestamp (`u["timestamp"] is None`): we only know the file is checked `NOW`. Accept it only if `NOW` is inside the validity period; otherwise `REJECT: no timestamp and the certificate expired on ...`.
3. Check the timestamp: `t = verify_timestamp(tsa, u["signature"], u["timestamp"])`. If `t is None`: `REJECT: bad timestamp`.
4. If `valid_from(publisher) <= t <= valid_until(publisher)` (Python lets you chain comparisons like this): `ACCEPT: signed on ...`; otherwise `REJECT: signed on ..., after the certificate expired`.

Hint: `t.date()` prints only the date of a `datetime`.

## Expected output

One line per file: one is accepted, four are rejected for four different reasons.

<details>
<summary>Check your answer</summary>

```
Alice's certificate is valid from 2024-01-01 to 2025-01-01
Today is 2026-11-15

photoedit-2.1-setup.exe
  ACCEPT: signed on 2024-06-12 while the certificate was valid
photoedit-2.2-update.exe
  REJECT: no timestamp and the certificate expired on 2025-01-01
photoedit-2.3-update.exe
  REJECT: signed on 2025-03-02 after the certificate expired
photoedit-2.4-update.exe
  REJECT: bad timestamp
photoedit-2.1-setup-mirror.exe
  REJECT: bad signature, the file was changed
```

"Today is" shows the day you run it. Version 2.3 was signed after the certificate expired: the key still works, but somebody (perhaps a thief) used it too late. In version 2.4 Mallory moved the time back to 2024, so the TSA's signature no longer fits.

</details>

## Run

```
python3 check_updates.py
```

About 12 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
