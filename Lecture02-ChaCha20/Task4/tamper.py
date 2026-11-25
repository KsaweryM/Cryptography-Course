# Task 4: change one byte.
from aead import seal, open_, chacha20   # aead.py is ready

key   = bytes.fromhex("0badc0de" * 8)
nonce = bytes.fromhex("000000000000000000000001")

packet = None        # Alice's packet: 11 bytes of ciphertext + a 16-byte tag
changed = None       # the packet after Mallory
no_tag = None        # what Bob would read without the tag
result = None        # what open_ says about the changed packet
result_aad = None    # what open_ says about the changed header

# TODO 1: packet = seal(key, nonce, b"Pay Bob 100")

# TODO 2: play Mallory: changed = a copy of the packet with byte 5 XOR 1

# TODO 3: without the tag: decrypt only the ciphertext part of changed (all but the last 16 bytes)
#         with chacha20(key, nonce, 1, ...): no_tag = ...

# TODO 4: with the tag: try open_(key, nonce, changed)
#         try: ...  result = "opened: " + str(plaintext)
#         except ValueError as e: result = "open_ raises: " + str(e)

# TODO 5: associated data: seal b"Pay Bob 100" with aad=b"to: Bob", then try to open the same packet
#         with aad=b"to: Eve" (the ciphertext is not touched); store the outcome in result_aad as in TODO 4

# The printing is ready: each line says "not done yet" until its TODO is done.
if packet is None:
    print("not done yet: TODO 1")
else:
    print("packet:   ", packet[:-16].hex(), "| tag", packet[-16:].hex())
if changed is None:
    print("not done yet: TODO 2")
else:
    print("changed:  ", bytes(changed[:-16]).hex(), "| tag", bytes(changed[-16:]).hex())
if no_tag is None:
    print("not done yet: TODO 3")
else:
    print("without the tag Bob reads:", no_tag)
if result is None:
    print("not done yet: TODO 4")
else:
    print("with the tag:", result)
if result_aad is None:
    print("not done yet: TODO 5")
else:
    print("header changed:", result_aad)
