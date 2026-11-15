# Task 2: look into a trust store.
# trust_store.pem: the roots that Ubuntu 24.04 trusts (package ca-certificates 20260816,
#   taken from the Mozilla root program), copied on 15 November 2026.
# we1.pem: the intermediate certificate WE1 that the server www.coventry.ac.uk sends.
# cert_ready.py is ready: load_cert, load_certs, subject_of, valid_from, valid_until, key_type, signed_by.
from cert_ready import load_cert, load_certs, subject_of, valid_from, valid_until, key_type, signed_by

store = load_certs("trust_store.pem")   # a list of certificates
we1 = load_cert("we1.pem")

# TODO 1: print how many roots are in the store


# TODO 2: count the roots that signed themselves (subject == issuer)


# TODO 3: count the roots with an RSA key and with an EC key (key_type gives "RSA 4096", "EC P-384", ...)


# TODO 4: find the oldest root (the earliest valid_from) and the root that expires last


# TODO 5: find the root whose subject is the issuer of WE1, and check that it signed WE1

