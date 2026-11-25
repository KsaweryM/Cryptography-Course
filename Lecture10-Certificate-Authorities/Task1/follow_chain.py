# Task 1: follow a real chain of trust.
# The three certificates of www.coventry.ac.uk, saved on 15 November 2026:
#   leaf.pem          the website (sent by the server)
#   intermediate.pem  WE1 of Google Trust Services (sent by the server)
#   root.pem          GTS Root R4 (from the trust store of Ubuntu 24.04)
# cert_ready.py is ready: load_cert, subject_of, issuer_of, valid_from, valid_until, signed_by.
from cert_ready import load_cert, subject_of, issuer_of, valid_from, valid_until, signed_by

# TODO 1: load the three certificates into a list, the leaf first
print("not done yet: TODO 1")


# TODO 2: for each certificate print its subject, its issuer and its dates
print("not done yet: TODO 2")


# TODO 3: for each link, check that the issuer of certificate i is the subject of certificate i + 1
print("not done yet: TODO 3")


# TODO 4: for each link, check that certificate i + 1 signed certificate i
print("not done yet: TODO 4")


# TODO 5: check that the root signed itself, and that the leaf did not sign the intermediate
print("not done yet: TODO 5")

