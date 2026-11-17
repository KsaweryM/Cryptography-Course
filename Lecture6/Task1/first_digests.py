import hashlib

# SHA-256 of b"abc", as printed in the standard (FIPS 180-4 example, NIST)
FIPS_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

# TODO 1: the digest of b"abc" as 64 hex digits: hashlib.sha256(b"abc").hexdigest()
abc_hex = None

# TODO 2: the digests (as bytes) of a short text and of empty data: hashlib.sha256(...).digest()
#         short text: b"Hello, Bob!"      empty data: b""
short_digest = None
empty_digest = None

# TODO 3: the digest (as bytes) of the whole file invoice.txt
#         read it with open("invoice.txt", "rb").read(), then hash the bytes
file_data = None
file_digest = None

# TODO 4: the digest (as bytes) of one million zero bytes: bytes(1000000)
big_digest = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if abc_hex is None:
    print("not done yet: TODO 1")
else:
    print("SHA-256(abc):    ", abc_hex)
    print("same as FIPS 180-4:", abc_hex == FIPS_ABC)
if short_digest is None or empty_digest is None:
    print("not done yet: TODO 2")
else:
    print("short text: 11 bytes in,", len(short_digest), "bytes out:", short_digest.hex())
    print("empty data:  0 bytes in,", len(empty_digest), "bytes out:", empty_digest.hex())
if file_data is None or file_digest is None:
    print("not done yet: TODO 3")
else:
    print("invoice.txt:", len(file_data), "bytes in,", len(file_digest), "bytes out:", file_digest.hex())
if big_digest is None:
    print("not done yet: TODO 4")
else:
    print("1000000 zero bytes in,", len(big_digest), "bytes out:", big_digest.hex())
