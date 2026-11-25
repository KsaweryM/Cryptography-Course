# Task 4: who may sign? Three chains that a TLS client must reject.
# cert_ready.py is ready: new_key, make_cert, signed_by, tls_check.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
from cert_ready import new_key, make_cert, signed_by, tls_check

# Ready: Trusty Root CA (no path length limit) and its intermediate Trusty Issuing CA 1
#   (the client trusts only the root)
root_key = new_key()
root = make_cert("Trusty Root CA", root_key, None, None, ca=True, path_len=None, days=20 * 365)
inter_key = new_key()
inter = make_cert("Trusty Issuing CA 1", inter_key, root, root_key, ca=True, path_len=0, days=5 * 365)

# Ready: Mallory gets an honest certificate for her own website mallory.example
mallory_key = new_key()
mallory = make_cert("mallory.example", mallory_key, inter, inter_key, ca=False, days=90,
                    dns_names=["mallory.example"])
print("1. mallory.example:          ", tls_check(mallory_key, [mallory, inter], root, "mallory.example"))

# TODO 1: Mallory signs a certificate for bank.example with HER leaf key (issuer = her certificate)
print("not done yet: TODO 1")


# TODO 2: check the signature of the fake certificate, then let the TLS client connect to "bank.example"
print("not done yet: TODO 2")


# TODO 3: a CA for the company Acme that may issue only names under acme.example (permitted=[...])
print("not done yet: TODO 3")


# TODO 4: the Acme CA issues www.acme.example and bank.example; let the TLS client connect to each
print("not done yet: TODO 4")


# TODO 5: Acme makes one more CA below Acme Corp CA (path_len=0 there!) and lets it issue www.acme.example;
#   let the TLS client connect with the chain [leaf, sub, acme]
print("not done yet: TODO 5")
