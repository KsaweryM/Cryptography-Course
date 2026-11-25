# Task 6: find the Signed Certificate Timestamps (SCTs) in real certificates.
#   coventry.pem    the certificate of www.coventry.ac.uk, saved on 15 November 2026
#   python-org.pem  the certificate of www.python.org, saved on 15 November 2026
#   my-shop.pem     a certificate made with make_cert, never sent to a log
# cert_ready.py is ready: load_cert, subject_of, issuer_of, valid_from, valid_until, scts_of, sct_time.
#   For an SCT `s`: s.log_id is the ID of the log (bytes), sct_time(s) is when the log signed it.
# ct_logs.py is ready: LOGS turns a log ID in hex capitals into the name of the log.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
from cert_ready import load_cert, subject_of, issuer_of, valid_from, valid_until, scts_of, sct_time
from ct_logs import LOGS

files = ["coventry.pem", "python-org.pem", "my-shop.pem"]

for i in range(len(files)):
    cert = load_cert(files[i])
    print(files[i], ":", subject_of(cert), "issued by", issuer_of(cert))
    print("  valid from:", valid_from(cert))

    # TODO 1: get the list of SCTs of this certificate and print how many there are
    print("not done yet: TODO 1")


    # TODO 2: for each SCT, print the name of its log (LOGS[s.log_id.hex().upper()]) and its time
    print("not done yet: TODO 2")


    # TODO 3: for each SCT, print how many minutes lie between valid_from and the time of the SCT
    print("not done yet: TODO 3")


    # TODO 4: print how many days the certificate is valid (valid_until - valid_from)
    print("not done yet: TODO 4")

    print()
