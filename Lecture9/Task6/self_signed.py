# Task 6: a self-signed certificate
# Alice makes a certificate for www.alice.example and signs it with her own key.
# What does its signature prove? Mallory tries two tricks.
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cert_tools import load_private_key, make_cert
from signing import verify

alice_private = load_private_key("alice_private.pem")
mallory_private = load_private_key("mallory_private.pem")

name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "www.alice.example")])


def check(cert):
    # TODO 3: verify the signature of cert with the public key inside the same cert:
    #   the signed bytes are cert.tbs_certificate_bytes, the signature is cert.signature.
    #   Return the result of verify(public_key, data, signature).
    return None


# TODO 1: Alice makes her self-signed certificate: the subject and the issuer are both name,
#         the public key is alice_private.public_key(), and alice_private signs it:
#         make_cert(subject, issuer, public_key, signing_key)
cert = None

# TODO 2: print the subject, the issuer (.rfc4514_string()) and whether they are equal (==).

print("Alice's certificate, signature OK:", check(cert))

# TODO 4: Mallory puts her own public key into Alice's certificate.
#   der = bytearray(cert.public_bytes(serialization.Encoding.DER))
#   find where Alice's 32-byte key starts: pos = der.find(alice_raw), and copy the 32 bytes of
#   mallory_raw over it (a loop over i from 0 to 31). Then load the result:
#   x509.load_der_x509_certificate(bytes(der)), and print check() of it.
alice_raw = alice_private.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
mallory_raw = mallory_private.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)

# TODO 5: Mallory makes her own self-signed certificate with the same name and her own key.
#         Print check() of it. What does a good signature on a self-signed certificate prove?
