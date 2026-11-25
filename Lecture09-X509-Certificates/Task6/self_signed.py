# Task 6: a self-signed certificate
# Alice makes a certificate for www.alice.example and signs it with her own key.
# What does its signature prove? Mallory makes one too. Where can trust come from?
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cert_tools import load_private_key, make_cert, colon_hex
from signing import verify

alice_private = load_private_key("alice_private.pem")
mallory_private = load_private_key("mallory_private.pem")

name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "www.alice.example")])

# Alice read this out to Bob on the phone (idea 3 of Task 1): the SHA-256 fingerprint of her certificate.
ALICE_FP = "6F:4B:D6:04:C8:F5:0B:73:21:E8:88:C3:69:39:47:95:08:C7:61:83:CB:49:5C:14:39:C8:D1:F6:EB:D1:4B:54"


# TODO 1: Alice makes her self-signed certificate: the subject and the issuer are both name,
#         the public key is alice_private.public_key(), and alice_private signs it:
#         make_cert(subject, issuer, public_key, signing_key)
alice_cert = None

# TODO 2: print the subject and the issuer (.rfc4514_string()) and whether they are equal (==):
#         print("subject:", ...)   print("issuer: ", ...)   print("issuer == subject:", ...)


def check(cert):
    # TODO 3: verify the signature of cert with the public key inside the same cert:
    #   the signed bytes are cert.tbs_certificate_bytes, the signature is cert.signature,
    #   the key is cert.public_key(). Return the result of verify(public_key, data, signature).
    return None


# TODO 4: Mallory makes her own self-signed certificate with the same name, her public key
#         and her private key.
mallory_cert = None

# TODO 5: Bob knows ALICE_FP. For both certificates: compute the fingerprint,
#         colon_hex(cert.fingerprint(hashes.SHA256())), and compare it with ALICE_FP (==).
alice_fp_ok = None
mallory_fp_ok = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if alice_cert is None:
    print("not done yet: TODO 1 and TODO 2")
if alice_cert is None or check(alice_cert) is None:
    print("not done yet: TODO 3")
else:
    print("Alice's certificate, signature OK:  ", check(alice_cert))
if mallory_cert is None:
    print("not done yet: TODO 4")
elif check(mallory_cert) is not None:
    print("Mallory's certificate, signature OK:", check(mallory_cert))
if alice_fp_ok is None:
    print("not done yet: TODO 5")
else:
    print("Alice's certificate, fingerprint = ALICE_FP:  ", alice_fp_ok)
    print("Mallory's certificate, fingerprint = ALICE_FP:", mallory_fp_ok)
