from x25519_ready import public_key, x25519, hkdf

# Private keys: 32 random bytes each (here the test values from RFC 7748, section 6.1)
alice_private = bytes.fromhex("77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a")
bob_private = bytes.fromhex("5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb")

# TODO 1: the public keys: public_key(private)            (this is d x G on Curve25519)
alice_public = None
bob_public = None

# TODO 2: the shared secret on both sides: x25519(my_private, other_public)
alice_secret = None
bob_secret = None

# TODO 3: derive a 32-byte key for ChaCha20 from Alice's secret: hkdf(alice_secret, b"lecture 5 chat key")
key = None

# TODO 4: one secret, two keys, one per direction: the same secret with two different labels (info)
#         hkdf(alice_secret, b"Alice to Bob") and hkdf(alice_secret, b"Bob to Alice")
key_alice_to_bob = None
key_bob_to_alice = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if alice_public is None or bob_public is None:
    print("not done yet: TODO 1")
else:
    print("Alice's public key: ", alice_public.hex())
    print("Bob's public key:   ", bob_public.hex())
if alice_secret is None or bob_secret is None:
    print("not done yet: TODO 2")
else:
    print("secret (Alice):     ", alice_secret.hex())
    print("secret (Bob):       ", bob_secret.hex())
    print("equal:", alice_secret == bob_secret)
if key is None:
    print("not done yet: TODO 3")
else:
    print("ChaCha20 key:       ", key.hex())
if key_alice_to_bob is None or key_bob_to_alice is None:
    print("not done yet: TODO 4")
else:
    print("key Alice to Bob:   ", key_alice_to_bob.hex())
    print("key Bob to Alice:   ", key_bob_to_alice.hex())
    print("different:", key_alice_to_bob != key_bob_to_alice)
