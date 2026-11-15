"""Ready helpers for Task 4: they load the files and read CRL fields with the `cryptography` library.
You do not need to change this file."""
import datetime
import os

from cryptography import x509
from cryptography.x509.oid import NameOID

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = os.path.join(HERE, "files")

# the time now, in UTC, without a time zone (the same form as next_update and revoked_on)
NOW = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)


def load_cert(filename):
    with open(os.path.join(FILES, filename), "rb") as f:
        return x509.load_pem_x509_certificate(f.read())


def load_crl(filename):
    with open(os.path.join(FILES, filename), "rb") as f:
        return x509.load_pem_x509_crl(f.read())


def name_of(cert):
    """The Common Name of the subject, only to print it."""
    return cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def next_update(crl):
    """Next Update of the CRL, in UTC: after this time the list is too old to use."""
    if hasattr(crl, "next_update_utc"):
        return crl.next_update_utc.replace(tzinfo=None)
    return crl.next_update


def revoked_on(entry):
    """The revocation date of one entry of the CRL, in UTC."""
    if hasattr(entry, "revocation_date_utc"):
        return entry.revocation_date_utc.replace(tzinfo=None)
    return entry.revocation_date


def reason_of(entry):
    """The reason code of one entry, for example "keyCompromise", or "unspecified"."""
    try:
        reason = entry.extensions.get_extension_for_class(x509.CRLReason).value.reason
    except x509.ExtensionNotFound:
        return "unspecified"
    names = {"key_compromise": "keyCompromise", "superseded": "superseded",
             "ca_compromise": "cACompromise", "affiliation_changed": "affiliationChanged",
             "cessation_of_operation": "cessationOfOperation", "certificate_hold": "certificateHold",
             "privilege_withdrawn": "privilegeWithdrawn", "unspecified": "unspecified"}
    return names.get(reason.name, reason.name)
