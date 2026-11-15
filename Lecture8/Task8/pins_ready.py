"""Ready helpers for Task 8. You do not need to change this file."""
import os

from cryptography import x509

HERE = os.path.dirname(os.path.abspath(__file__))
CERTS = os.path.join(HERE, "certs")

# the certificates of api.bob.example: the one from 2026 and three possible renewals in December 2026
FILES = ["api_2026.pem", "api_2027_same_key.pem", "api_2027_new_key.pem", "api_2027_backup_key.pem"]


def load_cert(filename):
    with open(os.path.join(CERTS, filename), "rb") as f:
        return x509.load_pem_x509_certificate(f.read())
