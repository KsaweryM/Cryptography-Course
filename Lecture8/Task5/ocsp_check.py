"""Task 5: ask the OCSP responder about two certificates, then decide like a browser.
What happens when Mallory blocks the question?"""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import ocsp

from ocsp_ready import Responder, load_cert, name_of, response_signed_by

responder = Responder()
ca = load_cert("issuing_ca.pem")            # the CA that issued the certificates and signs the answers

# (the certificate, does Mallory block the OCSP request?)
CASES = [("bob.pem", False), ("carol.pem", False), ("carol.pem", True)]


def ask_status(cert):
    """Returns "good", "revoked" or "unknown", or None when there is no valid answer."""
    # TODO 1: build the request and turn it into bytes:
    #         request = ocsp.OCSPRequestBuilder().add_certificate(cert, ca, hashes.SHA1()).build()
    #         request_bytes = request.public_bytes(serialization.Encoding.DER)
    # TODO 2: send it: answer = responder.ask(request_bytes). If it raises ConnectionError, return None.
    #         response = ocsp.load_der_ocsp_response(answer)
    #         If not response_signed_by(response, ca), return None.
    #         response.certificate_status is ocsp.OCSPCertStatus.GOOD, .REVOKED or .UNKNOWN:
    #         return "good", "revoked" or "unknown"
    return None


def decide(status, policy):
    """policy is "soft-fail" or "hard-fail". Returns "accept" or "reject"."""
    # TODO 3: "good" -> "accept"; "revoked" or "unknown" -> "reject".
    #         No answer (None): soft-fail accepts, hard-fail rejects.
    return "?"


for k in range(len(CASES)):
    cert = load_cert(CASES[k][0])
    responder.blocked = CASES[k][1]
    status = ask_status(cert)
    note = "Mallory blocks OCSP" if CASES[k][1] else ""
    print("%-14s %-20s answer: %-8s soft-fail: %-7s hard-fail: %s"
          % (name_of(cert), note, status, decide(status, "soft-fail"), decide(status, "hard-fail")))
