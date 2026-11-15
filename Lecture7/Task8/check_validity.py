# Task 8: is this validity allowed? Check certificates against the CA/Browser Forum limits.
# certs/ holds 8 certificates: coventry.pem and python-org.pem are real (saved on 15 November 2026),
#   the other six were made for this task (some are dated in the future).
# cert_ready.py is ready: load_cert, subject_of, valid_from, valid_until.
import datetime
from cert_ready import load_cert, subject_of, valid_from, valid_until

UTC = datetime.timezone.utc


def max_days(issued):
    # TODO 1: return the longest validity (in days) allowed for a certificate issued on `issued`:
    #   from 1 Mar 2018: 825, from 1 Sep 2020: 398, from 15 Mar 2026: 200,
    #   from 15 Mar 2027: 100, from 15 Mar 2029: 47.  Example: datetime.datetime(2026, 3, 15, tzinfo=UTC)

    return None


files = ["coventry.pem", "python-org.pem", "shop-2019.pem", "shop-2021.pem",
         "api-2026.pem", "blog-2026.pem", "mail-2027.pem", "vpn-2029.pem"]

for i in range(len(files)):
    cert = load_cert("certs/" + files[i])

    # TODO 2: compute how many days the certificate is valid: valid_until - valid_from


    # TODO 3: compare it with max_days(valid_from(cert)) and print the file, the issue date, days, limit, OK or TOO LONG

