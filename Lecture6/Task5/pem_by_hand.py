# Task 5: PEM by hand
# A PEM file is Base64 text between two marker lines. Under it are the DER bytes of the certificate.
# Decode it yourself, then compute the SHA-256 fingerprint and compare with the library.
import base64
import hashlib

from cryptography.hazmat.primitives import hashes, serialization
from cert_tools import load_cert

with open("bob.pem") as f:
    lines = f.read().splitlines()      # a list of the lines of the file, without "\n"

# TODO 1: join the Base64 lines into one text: skip the lines that start with "-----"
#         (line.startswith("-----")). Print how many characters you got.
b64 = ""

# TODO 2: decode it: der = base64.b64decode(b64). Print len(der) and the first 8 bytes as hex,
#         one byte at a time: "%02X " % der[i]
der = b""

# TODO 3: compare with the library: cert = load_cert("bob.pem") and
#         cert.public_bytes(serialization.Encoding.DER). Print whether the two are equal (==).

# TODO 4: the fingerprint: fp = hashlib.sha256(der).digest(). Print it as hex with ":" between bytes.
#         Compare with cert.fingerprint(hashes.SHA256()).

# TODO 5: change one bit: copy = bytearray(der); copy[100] = copy[100] ^ 1.
#         Print the fingerprint of bytes(copy). How many of the 32 bytes changed?
