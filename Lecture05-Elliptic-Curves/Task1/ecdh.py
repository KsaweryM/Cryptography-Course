import secrets
from x25519_ready import public_key, x25519

alice_private = None
bob_private = None
alice_public = None
bob_public = None
alice_secret = None
bob_secret = None

# TODO 1: the private keys: 32 random bytes each, secrets.token_bytes(32)
# TODO 2: the public keys: public_key(private)            (Alice sends hers to Bob, Bob sends his to Alice)
# TODO 3: the shared secret on both sides: x25519(my_private, other_public)

# The printing is ready: each line says "not done yet" until its TODO is done.
if alice_private is None or bob_private is None:
    print("not done yet: TODO 1")
else:
    print("Alice's private key:", alice_private.hex())
    print("Bob's private key:  ", bob_private.hex())
if alice_public is None or bob_public is None:
    print("not done yet: TODO 2")
else:
    print("Alice's public key: ", alice_public.hex())
    print("Bob's public key:   ", bob_public.hex())
if alice_secret is None or bob_secret is None:
    print("not done yet: TODO 3")
else:
    print("secret (Alice):     ", alice_secret.hex())
    print("secret (Bob):       ", bob_secret.hex())
    print("equal:", alice_secret == bob_secret)
    print("size of the secret:", len(alice_secret), "bytes (Diffie-Hellman in Lecture 4: 256 bytes)")
