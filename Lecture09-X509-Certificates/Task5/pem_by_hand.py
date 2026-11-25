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
#         (line.startswith("-----")). print("Base64 characters:", len(b64))
b64 = ""

# TODO 2: decode it: der = base64.b64decode(b64). Print len(der) and the first 8 bytes as hex,
#         one byte at a time: "%02X " % der[i]   ->   DER bytes: 293  first 8: 30 82 ...
der = b""

# TODO 3: compare with the library: cert = load_cert("bob.pem") and
#         cert.public_bytes(serialization.Encoding.DER). print("same as the library:", <der == ...>)
same = None

# TODO 4: the fingerprint: fp = hashlib.sha256(der).digest(). Print it as hex with ":" between bytes:
#         print("fingerprint by hand:", ...), then the same for cert.fingerprint(hashes.SHA256()):
#         print("fingerprint library:", ...)
fp = b""

# TODO 5: change one bit: copy = bytearray(der); copy[100] = copy[100] ^ 1.
#         print("one bit changed:    ", <the fingerprint of bytes(copy)>), then count how many of
#         the 32 bytes differ from fp: print("bytes changed:", changed, "of 32")
changed = None

# Delete each line below when its TODO is done.
if b64 == "":
    print("not done yet: TODO 1")
if der == b"":
    print("not done yet: TODO 2")
if same is None:
    print("not done yet: TODO 3")
if fp == b"":
    print("not done yet: TODO 4")
if changed is None:
    print("not done yet: TODO 5")
