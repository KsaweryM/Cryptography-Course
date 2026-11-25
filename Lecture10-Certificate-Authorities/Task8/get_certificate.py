# Task 8: get a certificate the way Let's Encrypt gives one: ACME with the http-01 challenge.
# acme_toy.py is ready: thumbprint, start_web_server, ToyCA (new_order, validate, finalize).
# cert_ready.py is ready: new_key, make_csr, subject_of, issuer_of, valid_from, valid_until.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
import os
from acme_toy import thumbprint, start_web_server, ToyCA
from cert_ready import new_key, make_csr, subject_of, issuer_of, valid_from, valid_until

# Ready: Bob's web server serves the folder webroot/, and bob.example points to it
port = start_web_server("webroot")
ca = ToyCA({"bob.example": port})

# TODO 1: make an account key and ask the CA for a new order for "bob.example"; print the token
print("not done yet: TODO 1")


# TODO 2: build the key authorization: the token, a dot, the thumbprint of the account key
print("not done yet: TODO 2")


# TODO 3: put it into the file webroot/.well-known/acme-challenge/<token>
print("not done yet: TODO 3")


# TODO 4: ask the CA to validate the order and print the answer
print("not done yet: TODO 4")


# TODO 5: make a key and a CSR for the website, send the CSR to finalize, print the certificate
print("not done yet: TODO 5")

