from x25519_ready import public_key, x25519, hkdf

# Private keys: 32 random bytes each (here the test values from RFC 7748, section 6.1)
ania_private = bytes.fromhex("77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a")
bartek_private = bytes.fromhex("5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb")

# TODO 1: the public keys: public_key(private)            (this is d x G on Curve25519)
# TODO 2: the shared secret on both sides: x25519(my_private, other_public)
# TODO 3: print both secrets (.hex()) and whether they are equal
# TODO 4: derive a 32-byte key for ChaCha20: hkdf(secret, b"lecture 5 chat key")
#         and print it (.hex())
