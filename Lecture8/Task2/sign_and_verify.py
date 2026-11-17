from signing import load_private_key, load_public_key, sign, verify

alice_private = load_private_key("alice_private.pem")    # only Alice has this file
alice_public = load_public_key("alice_public.pem")       # everybody may have this one
mallory_private = load_private_key("mallory_private.pem")

message = b"Bob, the meeting is moved to Friday 10:00. Alice"
changed = b"Bob, the meeting is moved to Friday 11:00. Alice"   # Mallory changed one character

# TODO 1: Alice signs the message: sign(alice_private, message)
signature = None

# TODO 2: Bob checks it with Alice's public key: verify(alice_public, message, signature)
check_message = None

# TODO 3: Bob gets the changed message with Alice's signature: verify(alice_public, changed, signature)
check_changed = None

# TODO 4: Mallory signs the changed message with her own private key: sign(mallory_private, changed).
#         Bob checks that signature with Alice's public key.
mallory_signature = None
check_mallory = None

# TODO 5: Alice signs the same message once more: sign(alice_private, message).
#         Is the new signature equal to the first one? (== compares bytes like memcmp in C)
same = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if signature is None:
    print("not done yet: TODO 1")
else:
    print("signature:", len(signature), "bytes")
    print(signature.hex())
if check_message is None:
    print("not done yet: TODO 2")
else:
    print("Bob checks the message:          ", check_message)
if check_changed is None:
    print("not done yet: TODO 3")
else:
    print("Bob checks the changed message:  ", check_changed)
if mallory_signature is None or check_mallory is None:
    print("not done yet: TODO 4")
else:
    print("Bob checks Mallory's signature:  ", check_mallory)
if same is None:
    print("not done yet: TODO 5")
else:
    print("the second signature is the same:", same)
