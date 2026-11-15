# Task 3: Bob's certificate
# Trusty CA issues an X.509 certificate for bob.example: the name, Bob's public key, the dates,
# and the signature of Trusty CA over all of it.
import datetime

from cryptography import x509
from cryptography.x509.oid import NameOID
from cert_tools import load_private_key, load_public_key, save_cert, show

UTC = datetime.timezone.utc

ca_private = load_private_key("trusty_ca_private.pem")
bob_public = load_public_key("bob_public.pem")

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

# TODO 2: fill in the rest of the fields, one call per field, as in the line above:
#   builder = builder.subject_name(subject)
#   builder = builder.serial_number(0x4F3A9C2E71D05B88)
#   builder = builder.not_valid_before(datetime.datetime(2026, 11, 1, tzinfo=UTC))
#   builder = builder.not_valid_after(datetime.datetime(2027, 1, 30, tzinfo=UTC))
#   builder = builder.public_key(bob_public)

# TODO 3: Trusty CA signs: cert = builder.sign(ca_private, None)
#         (None: an Ed25519 key needs no separate hash algorithm)
cert = None

# TODO 4: save the certificate to "bob.pem" with save_cert, then print it with show(cert).
