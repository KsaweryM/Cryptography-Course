"""Task 6: check three CertificateVerify messages, as a TLS 1.3 client does."""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from handshake_ready import BOB_CERT, MESSAGES, transcript_hash


def signed_content(th):
    """The bytes a TLS 1.3 server signs in CertificateVerify (RFC 9846, section 4.5.2; RFC 8446, section 4.4.3)."""
    # TODO 1: 64 spaces, then the text "TLS 1.3, server CertificateVerify", then one zero byte,
    #         then the transcript hash th. In Python: b" " * 64 + b"TLS 1.3, server CertificateVerify" + ...
    return b""


def signature_ok(signature, content):
    """True if signature over content was made with the private key of BOB_CERT."""
    # TODO 2: BOB_CERT.public_key().verify(signature, content, ec.ECDSA(hashes.SHA256()))
    #         returns nothing if the signature is good and raises InvalidSignature if not
    return False


content = signed_content(transcript_hash)
print("signed content: %d bytes" % len(content))
print("bytes 64 to 97:", content[64:98])
# TODO 3: for every message in MESSAGES, print who sent it and "signature OK" or "signature BAD"
