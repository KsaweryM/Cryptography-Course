"""Ready helpers for Task 3: they read certificate fields with the `cryptography` library.
You do not need to change this file. Treat every function as a black box."""
import datetime
import os

from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

HERE = os.path.dirname(os.path.abspath(__file__))
CHAINS = os.path.join(HERE, "chains")

# the time now, in UTC, without a time zone (the same form as valid_from and valid_until)
NOW = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)


def load_chain(filename):
    """The certificates the server sent, in its order: [leaf, intermediate, ...]."""
    with open(os.path.join(CHAINS, filename), "rb") as f:
        return x509.load_pem_x509_certificates(f.read())


def load_store():
    """The trust store of this task: a list with one root, the Trusty Root CA."""
    return load_chain("root.pem")


def name_of(cert):
    """The Common Name of the subject, only to print it."""
    return cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def signed_by(cert, issuer):
    """True if the signature on cert was made with the private key of issuer
    (and the issuer name in cert is the subject name of issuer)."""
    try:
        cert.verify_directly_issued_by(issuer)
        return True
    except (ValueError, TypeError, InvalidSignature):
        return False


def valid_from(cert):
    """Not Before, in UTC."""
    if hasattr(cert, "not_valid_before_utc"):
        return cert.not_valid_before_utc.replace(tzinfo=None)
    return cert.not_valid_before


def valid_until(cert):
    """Not After, in UTC."""
    if hasattr(cert, "not_valid_after_utc"):
        return cert.not_valid_after_utc.replace(tzinfo=None)
    return cert.not_valid_after


def dns_names(cert):
    """The DNS names in the Subject Alternative Name, for example ["bob.example"]."""
    try:
        san = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
    except x509.ExtensionNotFound:
        return []
    return san.get_values_for_type(x509.DNSName)


def is_ca(cert):
    """True if Basic Constraints says CA:TRUE."""
    try:
        return cert.extensions.get_extension_for_class(x509.BasicConstraints).value.ca
    except x509.ExtensionNotFound:
        return False


def key_purposes(cert):
    """The Extended Key Usage as a list of short names, for example ["serverAuth"]."""
    try:
        eku = cert.extensions.get_extension_for_class(x509.ExtendedKeyUsage).value
    except x509.ExtensionNotFound:
        return []
    names = []
    for oid in eku:
        if oid == ExtendedKeyUsageOID.SERVER_AUTH:
            names.append("serverAuth")
        elif oid == ExtendedKeyUsageOID.CLIENT_AUTH:
            names.append("clientAuth")
        else:
            names.append(oid.dotted_string)
    return names
