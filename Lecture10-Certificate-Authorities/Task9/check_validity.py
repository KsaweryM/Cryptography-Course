# Task 9: is this validity allowed? Check certificates against the CA/Browser Forum limits.
# certs/ holds 8 certificates: coventry.pem and python-org.pem are real (saved on 15 November 2026),
#   the other six were made for this task (some are dated in the future).
# cert_ready.py is ready: load_cert, subject_of, valid_from, valid_until.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
import datetime
from cert_ready import load_cert, subject_of, valid_from, valid_until

UTC = datetime.timezone.utc


def max_days(issued):
    # TODO 1: return the longest validity (in days) allowed for a certificate issued on `issued`:
    #   from 1 Mar 2018: 825, from 1 Sep 2020: 398, from 15 Mar 2026: 200,
    #   from 15 Mar 2027: 100, from 15 Mar 2029: 47.  Example: datetime.datetime(2026, 3, 15, tzinfo=UTC)
    print("not done yet: TODO 1")
    return None


files = ["coventry.pem", "python-org.pem", "shop-2019.pem", "shop-2021.pem",
         "api-2026.pem", "blog-2026.pem", "mail-2027.pem", "vpn-2029.pem"]

# Ready: a first test of max_days (it should say 200)
print("limit for a certificate issued on 1 April 2026:", max_days(datetime.datetime(2026, 4, 1, tzinfo=UTC)))

for i in range(len(files)):
    cert = load_cert("certs/" + files[i])
    days = None

    # TODO 2: compute how many days the certificate is valid, the way the Baseline Requirements count:
    #   seconds = (valid_until - valid_from) + 1 second (both ends count); every started day counts as a day
    if days is None:
        print("not done yet: TODO 2")

    # TODO 3: compare it with max_days(valid_from(cert)) and print the file, the issue date, days, limit, OK or TOO LONG
    print("not done yet: TODO 3")
    break    # remove this line when TODO 3 is done: then the loop checks all 8 files
