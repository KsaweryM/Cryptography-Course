# Task 3: Bob's certificate
# Trusty CA issues an X.509 certificate for bob.example: the name, Bob's public key, the dates,
# and the signature of Trusty CA over all of it. Then Alice checks that signature.
import datetime

from cryptography import x509
from cryptography.x509.oid import NameOID
from cert_tools import load_private_key, load_public_key, save_cert, show
from signing import verify

UTC = datetime.timezone.utc

ca_private = load_private_key("trusty_ca_private.pem")    # only Trusty CA has this
ca_public = load_public_key("trusty_ca_public.pem")       # Alice already has this
bob_public = load_public_key("bob_public.pem")
mallory_public = load_public_key("mallory_public.pem")

# The names, ready. A name is a list of attributes: country (C), organisation (O), common name (CN).
issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "GB"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Trusty CA Ltd"),
    x509.NameAttribute(NameOID.COMMON_NAME, "Trusty CA"),
])

# TODO 1: the subject: C = GB, O = Bob Ltd, CN = bob.example, in this order, as in issuer above.
subject = None

builder = x509.CertificateBuilder()
builder = builder.issuer_name(issuer)

# TODO 2: fill in the rest of the fields, one call per field, as in the line above
#   (the calls and the values are in the README, step 2).

# TODO 3: Trusty CA signs: cert = builder.sign(ca_private, None)
#         (None: an Ed25519 key needs no separate hash algorithm)
cert = None

# TODO 4: save the certificate to "bob.pem" with save_cert, then print it with show(cert).

# TODO 5: Alice checks the CA's signature: verify(key, signed bytes, signature) with
#   the signed bytes cert.tbs_certificate_bytes and the signature cert.signature.
#   Check once with ca_public and once with mallory_public:
#   print("signature checked with Trusty CA's key:", ok_ca)
#   print("signature checked with Mallory's key:  ", ok_mallory)
ok_ca = None
ok_mallory = None

# Delete each line below when its TODO is done.
if subject is None:
    print("not done yet: TODO 1")
if cert is None:
    print("not done yet: TODO 2 and TODO 3")
    print("not done yet: TODO 4")
if ok_ca is None:
    print("not done yet: TODO 5")
