# Task 3: build your own small PKI: a root, an intermediate and a leaf.
# cert_ready.py is ready: new_key, make_cert, save_cert, ca_flag, subject_of, issuer_of, signed_by, tls_check.
#   make_cert(cn, key, issuer, issuer_key, ca=..., path_len=..., days=..., dns_names=[...])
#   issuer=None makes a self-signed certificate.
from cert_ready import new_key, make_cert, save_cert, ca_flag, subject_of, issuer_of, signed_by, tls_check

# TODO 1: the root CA "Trusty Root CA": a new key, a self-signed CA certificate, 20 years, path_len=1


# TODO 2: the intermediate CA "Trusty CA 1", signed by the root: 5 years, path_len=0


# TODO 3: the leaf for Alice's website "alice-shop.example", signed by the intermediate: 90 days, not a CA


# TODO 4: save the three certificates and print subject, issuer and ca_flag of each


# TODO 5: check every signature link, then let a TLS client that trusts only your root connect

