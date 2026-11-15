"""Ready parts of Task 6: Bob's certificate and three CertificateVerify messages. Do not change this file.

The values were recorded from three handshakes with a server that says it is bob.example:
    today, Bob's server          signed with Bob's private key over today's transcript hash
    today, Mallory's server      sends a copy of Bob's certificate, but signs with her own key
    today, Mallory replays       sends Bob's real signature from yesterday's handshake
A transcript hash is the SHA-256 of all handshake messages so far (ClientHello ... Certificate).
"""
import os

from cryptography import x509

from files.values import TODAY_HASH, OLD_HASH, SIG_BOB_TODAY, SIG_MALLORY, SIG_BOB_OLD

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "files", "bob.pem"), "rb") as f:
    BOB_CERT = x509.load_pem_x509_certificate(f.read())     # the certificate all three servers sent

# the transcript hash of the handshake that Alice is doing now (32 bytes)
transcript_hash = bytes.fromhex(TODAY_HASH)

# (who sent it, the signature in CertificateVerify)
MESSAGES = [
    ("Bob, today", bytes.fromhex(SIG_BOB_TODAY)),
    ("Mallory with Bob's certificate", bytes.fromhex(SIG_MALLORY)),
    ("Mallory replays Bob's old signature", bytes.fromhex(SIG_BOB_OLD)),
]
