# Task 3: build your own small PKI: a root, an intermediate and a leaf.
# cert_ready.py is ready: new_key, make_cert, save_cert, ca_flag, subject_of, issuer_of, signed_by, tls_check.
#   make_cert(cn, key, issuer, issuer_key, ca=..., path_len=..., days=..., dns_names=[...])
#   issuer=None makes a self-signed certificate.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
from cert_ready import new_key, make_cert, save_cert, ca_flag, subject_of, issuer_of, signed_by, tls_check

# TODO 1: the root CA "Trusty Root CA": a new key, a self-signed CA certificate, 20 years, path_len=1
print("not done yet: TODO 1")

# TODO 2: the intermediate CA "Trusty Issuing CA 1", signed by the root: 5 years, path_len=0
print("not done yet: TODO 2")

# TODO 3: the leaf for Bob's website "bob.example", signed by the intermediate: 90 days, not a CA
print("not done yet: TODO 3")

# TODO 4: save the three certificates and print subject, issuer and ca_flag of each
print("not done yet: TODO 4")

# TODO 5: check every signature link, then let a TLS client that trusts only your root connect,
#   once with the chain [leaf, intermediate] and once with [leaf] only
print("not done yet: TODO 5")
