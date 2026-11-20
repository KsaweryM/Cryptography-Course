"""Task 5: ask the OCSP responder about two certificates, then decide like a browser.
What happens when Mallory blocks the question, or answers it with an old answer?"""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import ocsp

from ocsp_ready import NOW, Responder, load_cert, name_of, next_update_of, response_signed_by

responder = Responder()
ca = load_cert("issuing_ca.pem")            # the CA that issued the certificates and signs the answers

# (the certificate, what Mallory does with the OCSP request: None, "blocks" or "replays")
CASES = [("bob.pem", None), ("carol.pem", None), ("carol.pem", "blocks"), ("carol.pem", "replays")]


def ask_status(cert):
    """Returns "good", "revoked" or "unknown", or None when there is no valid answer."""
    # TODO 1: build the request (ocsp.OCSPRequestBuilder, add_certificate with the issuer ca and
    #         hashes.SHA1(), then build) and turn it into DER bytes (public_bytes)
    # TODO 2: send it with responder.ask. If it raises ConnectionError, return None.
    #         Read the answer with ocsp.load_der_ocsp_response.
    #         If response_signed_by(response, ca) is not True, return None
    # TODO 3: the freshness. If next_update_of(response) is before NOW, the answer is too old:
    #         return None (an old answer is no answer)
    # TODO 4: response.certificate_status is ocsp.OCSPCertStatus.GOOD, .REVOKED or .UNKNOWN:
    #         return "good", "revoked" or "unknown"
    return "not done yet: TODO 1"


def decide(status, policy):
    """policy is "soft-fail" or "hard-fail". Returns "accept" or "reject"."""
    # TODO 5: "good" -> "accept"; "revoked" or "unknown" -> "reject".
    #         No answer (None): soft-fail accepts, hard-fail rejects.
    return "not done yet: TODO 5"


NOTES = {None: "", "blocks": "Mallory blocks OCSP", "replays": "Mallory replays an old answer"}
for k in range(len(CASES)):
    cert = load_cert(CASES[k][0])
    responder.mallory = CASES[k][1]
    status = ask_status(cert)
    print("%-14s %-30s answer: %-8s soft-fail: %-7s hard-fail: %s"
          % (name_of(cert), NOTES[CASES[k][1]], status, decide(status, "soft-fail"), decide(status, "hard-fail")))
