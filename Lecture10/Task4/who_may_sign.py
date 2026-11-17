# Task 4: who may sign? Two chains that a TLS client must reject.
# cert_ready.py is ready: new_key, make_cert, signed_by, tls_check.
from cert_ready import new_key, make_cert, signed_by, tls_check

# Ready: Trusty Root CA and its intermediate Trusty CA 1 (the client trusts only the root)
root_key = new_key()
root = make_cert("Trusty Root CA", root_key, None, None, ca=True, path_len=1, days=20 * 365)
inter_key = new_key()
inter = make_cert("Trusty CA 1", inter_key, root, root_key, ca=True, path_len=0, days=5 * 365)

# Ready: Mallory gets an honest certificate for her own website mallory.example
mallory_key = new_key()
mallory = make_cert("mallory.example", mallory_key, inter, inter_key, ca=False, days=90,
                    dns_names=["mallory.example"])
print("1. mallory.example:          ", tls_check(mallory_key, [mallory, inter], root, "mallory.example"))

# TODO 1: Mallory signs a certificate for bank.example with HER leaf key (issuer = her certificate)


# TODO 2: check the signature of the fake certificate, then let the TLS client connect to "bank.example"


# TODO 3: a CA for the company Acme that may issue only names under acme.example (permitted=[...])


# TODO 4: the Acme CA issues www.acme.example and bank.example; let the TLS client connect to each

