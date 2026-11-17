"""Task 8: Bob's phone app pins api.bob.example. Which renewed certificates will the app still accept?"""
import base64
import hashlib

from cryptography.hazmat.primitives import serialization

from pins_ready import FILES, load_cert


def cert_pin(cert):
    """A pin of the whole certificate: base64 of the SHA-256 of its DER bytes."""
    # TODO 1: der = cert.public_bytes(serialization.Encoding.DER)
    #         return base64.b64encode(hashlib.sha256(der).digest()).decode()
    return ""


def spki_pin(cert):
    """A pin of the public key only: base64 of the SHA-256 of the SubjectPublicKeyInfo DER bytes."""
    # TODO 2: der = cert.public_key().public_bytes(serialization.Encoding.DER,
    #                                              serialization.PublicFormat.SubjectPublicKeyInfo)
    #         then the same as in cert_pin
    return ""


# What the app shipped with in 2026: a pin of the 2026 certificate, and two key pins:
# the 2026 key and a backup key that Bob keeps offline and has never used.
first = load_cert("api_2026.pem")
APP_CERT_PIN = cert_pin(first)
APP_SPKI_PINS = [spki_pin(first), "80E24poONJAEyvB/qmN1uvdylRrWLUT6ExA0k7hu+I4="]
print("app cert pin:", APP_CERT_PIN)
print("app key pins:", APP_SPKI_PINS)

for i in range(len(FILES)):
    cert = load_cert(FILES[i])
    # TODO 3: does the certificate pin match? (cert_pin(cert) == APP_CERT_PIN)
    #         does a key pin match? (spki_pin(cert) is one of APP_SPKI_PINS; use a loop)
    #         print the file name and "match" or "NO" for each kind of pin
    print("%-26s cert pin: TODO  key pin: TODO" % FILES[i])
