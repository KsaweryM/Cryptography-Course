# Task 2: a signed name card
# Trusty CA signs the card "name=bob.example;key=<Bob's public key>".
# Alice checks the card with the public key of Trusty CA. Can Mallory change it?
from signing import load_private_key, load_public_key, sign, verify, key_hex

ca_private = load_private_key("trusty_ca_private.pem")   # only Trusty CA has this
ca_public = load_public_key("trusty_ca_public.pem")      # Alice already has this
bob_public = load_public_key("bob_public.pem")
mallory_private = load_private_key("mallory_private.pem")
mallory_public = load_public_key("mallory_public.pem")

print("Bob's key:    ", key_hex(bob_public))
print("Mallory's key:", key_hex(mallory_public))

# TODO 1: make Bob's card: the bytes b"name=bob.example;key=" followed by key_hex(bob_public)
#         (key_hex gives text; .encode() turns text into bytes). Print it.
card = b""

# TODO 2: Trusty CA signs the card with its private key. Print the signature as hex (signature.hex()).
signature = b""

# TODO 3: Alice checks the card: verify with the public key of Trusty CA. Print the result.

# TODO 4: Mallory keeps the signature but puts her own key in the card:
#         fake = b"name=bob.example;key=" followed by key_hex(mallory_public).
#         Alice checks fake with the same signature. Print the result.

# TODO 5: Mallory signs fake with her own private key. Alice checks it with the public key
#         of Trusty CA, as always. Print the result.
