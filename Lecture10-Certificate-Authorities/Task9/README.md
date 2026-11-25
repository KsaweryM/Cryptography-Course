# Task 9: is this validity allowed?

## The situation

Public TLS certificates may not live as long as their owners would like. The CA/Browser Forum and the browsers have shortened the limit several times, and the limit that counts is the one in force on the day the certificate was issued:

| Issued on or after | At most |
|---|---|
| 1 March 2018 | 825 days |
| 1 September 2020 | 398 days |
| 15 March 2026 | 200 days |
| 15 March 2027 | 100 days |
| 15 March 2029 | 47 days |

The folder `certs/` holds 8 certificates: `coventry.pem` and `python-org.pem` are real (saved on 15 November 2026), the other six were made for this task, some of them dated in the future.

![A time line of the limits: 825 days from 1 March 2018, 398 days from 1 September 2020, 200 days from 15 March 2026, 100 days from 15 March 2027, 47 days from 15 March 2029. For each of the 8 certificates in certs/: is the number of days valid within the limit on the day it was issued?](figure.svg)

## Goal

Check eight certificates against the limit that held on the day each was issued.

## Ready for you

- `certs/`: the 8 certificates; the list of file names is in `check_validity.py`.
- `cert_ready.py` (a black box): `load_cert`, `valid_from`, `valid_until`.
- `check_validity.py` already calls `max_days` once, for 1 April 2026 (it should print 200), and loads each certificate in the loop.
- A date to compare with: `datetime.datetime(2026, 3, 15, tzinfo=UTC)`; dates compare with `>=` like numbers. The difference of two dates is a duration: `(a - b).total_seconds()`.

## Steps

Write your code in place of the `TODO` comments in `check_validity.py`. Under each `TODO` there is a `print("not done yet: TODO n")` (with an `if` in TODO 2 and a `break` in TODO 3): replace all of it with your code.

1. Write `max_days(issued)`: a chain of `if` statements, the newest date first, that returns the limit from the table (and `None` before 1 March 2018).
2. In the loop, compute how many days the certificate is valid, the way the Baseline Requirements count it. The period includes both `notBefore` and `notAfter`, so add one second: `seconds = int((valid_until(cert) - valid_from(cert)).total_seconds()) + 1`. A day is 86400 seconds, and any part of a day counts as a whole day: `days = seconds // 86400`, plus 1 if `seconds % 86400 != 0` (integer division and remainder, as `/` and `%` on integers in C).
3. Compare it with `max_days(valid_from(cert))` (`days <= limit` is allowed) and print the file name, the issue date, the days, the limit, and `OK` or `TOO LONG`.

## Expected output

Predict first: is the certificate of www.python.org allowed (13 January 2026 13:03:46 to 14 February 2027 13:03:45)? And `mail-2027.pem`, from 1 April 2027 09:00:00 to 10 July 2027 09:00:00, exactly 100 times 24 hours?

<details>
<summary>Check your answer</summary>

```
limit for a certificate issued on 1 April 2026: 200
coventry.pem    2026-10-13   91 days, limit 200 : OK
python-org.pem  2026-01-13  397 days, limit 398 : OK
shop-2019.pem   2019-05-01  731 days, limit 825 : OK
shop-2021.pem   2021-03-01  731 days, limit 398 : TOO LONG
api-2026.pem    2026-04-01  398 days, limit 200 : TOO LONG
blog-2026.pem   2026-11-01  200 days, limit 200 : OK
mail-2027.pem   2027-04-01  101 days, limit 100 : TOO LONG
vpn-2029.pem    2029-06-01   91 days, limit  47 : TOO LONG
```

`python-org.pem` ends one second before 14 February 13:03:46: with the second added it lives exactly 397 days, and it was issued in January 2026, just before the limit dropped to 200 days, so it is fine; the same validity issued in April 2026 (`api-2026.pem`) is too long. `mail-2027.pem` ends on the full 24 hours: 100 times 24 hours plus the last second is more than 100 days, so it is too long. The Coventry certificate counts as 91 days: it is almost one hour longer than 90 days. In 2029 even the 90 days of Let's Encrypt will be too long.

</details>

## Run

```
python3 check_validity.py
```

About 8 minutes. Python 3 and the library `cryptography` (`pip install cryptography`, version 41 or newer). No internet needed.
