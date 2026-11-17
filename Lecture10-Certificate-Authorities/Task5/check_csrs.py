# Task 5: play the CA and check three certificate signing requests (CSRs).
#   bob.csr          Bob's request for bob-shop.example
#   bob-changed.csr  the same request after Mallory changed bytes in it on the way
#   mallory.csr      Mallory's own request for bob-shop.example, made with her own key
# cert_ready.py is ready: new_key, make_csr, save_csr, load_csr, subject_of, dns_names_of, key_id.
#   csr.is_signature_valid is True when the signature on the CSR verifies with the public key inside it.
from cert_ready import new_key, make_csr, save_csr, load_csr, subject_of, dns_names_of, key_id

# TODO 1: make your own key and a CSR for "alice-shop.example", save it as alice.csr


# TODO 2: load the four CSRs and, for each one, print the file name, the subject and the DNS names


# TODO 3: for each CSR, print whether its signature is valid


# TODO 4: print the key_id of the public key in bob.csr and in mallory.csr: is it the same key?

