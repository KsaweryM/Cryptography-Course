"""Ready parts of Task 5: the CA's OCSP responder and two helpers. You do not need to change this file.

The responder runs inside this program (no network): responder.ask(request) takes the bytes of an
OCSP request and returns the bytes of a signed OCSP response, as a real responder does over HTTP.
When responder.blocked is True, Mallory drops the request and ask() raises ConnectionError.
"""
import datetime
import os

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509 import ocsp
from cryptography.x509.oid import NameOID

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = os.path.join(HERE, "files")


def load_cert(filename):
    with open(os.path.join(FILES, filename), "rb") as f:
        return x509.load_pem_x509_certificate(f.read())


def name_of(cert):
    """The Common Name of the subject, only to print it."""
    return cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def response_signed_by(response, issuer):
    """True if the OCSP response was signed with the private key of issuer."""
    try:
        issuer.public_key().verify(response.signature, response.tbs_response_bytes,
                                   ec.ECDSA(response.signature_hash_algorithm))
        return True
    except Exception:
        return False


class Responder:
    """The OCSP responder of Trusty Issuing CA 1. Carol's certificate (serial 0x1002) is revoked."""

    def __init__(self):
        self.ca = load_cert("issuing_ca.pem")
        with open(os.path.join(FILES, "issuing_ca.key"), "rb") as f:
            self.key = serialization.load_pem_private_key(f.read(), None)
        self.known = [load_cert("bob.pem"), load_cert("carol.pem")]
        self.revoked = {0x1002: datetime.datetime(2026, 11, 10, 9, 30)}
        self.blocked = False

    def ask(self, request_bytes):
        if self.blocked:
            raise ConnectionError("no answer from the OCSP responder")
        request = ocsp.load_der_ocsp_request(request_bytes)
        now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None, microsecond=0)
        builder = ocsp.OCSPResponseBuilder()
        for i in range(len(self.known)):
            cert = self.known[i]
            if cert.serial_number != request.serial_number:
                continue
            if cert.serial_number in self.revoked:
                builder = builder.add_response(cert, self.ca, hashes.SHA1(), ocsp.OCSPCertStatus.REVOKED, now,
                                               now + datetime.timedelta(days=7), self.revoked[cert.serial_number],
                                               x509.ReasonFlags.key_compromise)
            else:
                builder = builder.add_response(cert, self.ca, hashes.SHA1(), ocsp.OCSPCertStatus.GOOD, now,
                                               now + datetime.timedelta(days=7), None, None)
            builder = builder.responder_id(ocsp.OCSPResponderEncoding.HASH, self.ca)
            response = builder.sign(self.key, hashes.SHA256())
            return response.public_bytes(serialization.Encoding.DER)
        return ocsp.OCSPResponseBuilder.build_unsuccessful(
            ocsp.OCSPResponseStatus.UNAUTHORIZED).public_bytes(serialization.Encoding.DER)
