from x25519_ready import public_key, x25519, hkdf

# Ready: the X25519 exchange, with the private keys of RFC 7748, section 6.1 (the same steps as Task 1)
alice_private = bytes.fromhex("77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a")
bob_private = bytes.fromhex("5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb")
alice_secret = x25519(alice_private, public_key(bob_private))   # Alice: her private key, Bob's public key
bob_secret = x25519(bob_private, public_key(alice_private))     # Bob: his private key, Alice's public key

# TODO 1: one 32-byte key for ChaCha20 from Alice's secret: hkdf(alice_secret, b"lecture 5 chat key")
key = None

# TODO 2: one secret, two keys, one per direction: Alice's secret with two different labels (info)
#         hkdf(alice_secret, b"Alice to Bob") and hkdf(alice_secret, b"Bob to Alice")
alice_key_to_bob = None
alice_key_from_bob = None

# TODO 3: Bob does the same with his own secret, bob_secret, and the same two labels
bob_key_from_alice = None
bob_key_to_alice = None

# TODO 4: Mallory sends Alice 32 zero bytes in place of Bob's public key (a point of small order).
#         a) Alice computes the secret with it: x25519(alice_private, mallory_public)
#         b) write is_all_zero(secret): True when every byte is 0 (a loop over the 32 bytes, like a loop in C)
mallory_public = bytes(32)
mallory_secret = None


def is_all_zero(secret):
    return None

# The printing is ready: each line says "not done yet" until its TODO is done.
print("shared secret:            ", alice_secret.hex())
if key is None:
    print("not done yet: TODO 1")
else:
    print("ChaCha20 key:             ", key.hex())
if alice_key_to_bob is None or alice_key_from_bob is None:
    print("not done yet: TODO 2")
else:
    print("key Alice to Bob (Alice): ", alice_key_to_bob.hex())
    print("key Bob to Alice (Alice): ", alice_key_from_bob.hex())
    print("different:", alice_key_to_bob != alice_key_from_bob)
if bob_key_from_alice is None or bob_key_to_alice is None:
    print("not done yet: TODO 3")
else:
    print("key Alice to Bob (Bob):   ", bob_key_from_alice.hex())
    print("key Bob to Alice (Bob):   ", bob_key_to_alice.hex())
    print("the same on both sides:", bob_key_from_alice == alice_key_to_bob and bob_key_to_alice == alice_key_from_bob)
if mallory_secret is None or is_all_zero(bytes(32)) is None:
    print("not done yet: TODO 4")
else:
    print("secret with Mallory's key: ", mallory_secret.hex())
    print("all zero, refused:", is_all_zero(mallory_secret), "| real secret refused:", is_all_zero(alice_secret))
