# Task 5: play the CA and check certificate signing requests (CSRs).
#   bob.csr          Bob's request for bob.example
#   bob-changed.csr  the same request after Mallory changed bytes in it on the way
#   mallory.csr      Mallory's own request for bob.example, made with her own key
# cert_ready.py is ready: new_key, make_csr, save_csr, load_csr, subject_of, dns_names_of, key_id.
#   csr.is_signature_valid is True when the signature on the CSR verifies with the public key inside it.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
from cert_ready import new_key, make_csr, save_csr, load_csr, subject_of, dns_names_of, key_id

# TODO 1: Carol is a new customer: make her key and a CSR for "carol.example", save it as carol.csr
print("not done yet: TODO 1")

# TODO 2: load the four CSRs and, for each one, print the file name, the subject and the DNS names
print("not done yet: TODO 2")

# TODO 3: for each CSR, print whether its signature is valid
print("not done yet: TODO 3")

# TODO 4: print the key_id of the public key in bob.csr and in mallory.csr: is it the same key?
print("not done yet: TODO 4")
