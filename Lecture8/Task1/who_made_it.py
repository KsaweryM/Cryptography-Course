import hashlib
import hmac


def read_file(path):
    # like fopen(path, "rb") + fread in C: the whole file as bytes
    with open(path, "rb") as f:
        return f.read()


alice_update = read_file("alice_update.sh")      # what Alice really published
mallory_update = read_file("mallory_update.sh")  # what Bob downloaded after Mallory changed the server

# The download page shows a SHA-256. Mallory changed the page too: this is the hash Bob reads there now.
PAGE_HASH = "b4d421a73b76fa85cff1735acc3396eff57390b3f512e36115c827a87aad982d"

# Alice and Bob met once and agreed on a secret MAC key (32 bytes). Mallory does not know it.
SHARED_KEY = bytes.fromhex("bec2b625c368e6ae0f6c683f100aafab0ca830101c6240648f476421e0fc4c1c")
# Alice sends this HMAC-SHA256 tag of her update; Mallory can copy it, but cannot make a new one.
ALICE_TAG = bytes.fromhex("4e35cdfccc5185bbb3ff90d2427ce61b5edfb87e30ed35f882157fdaff466b63")

# TODO 1: Bob checks the file he downloaded against the page:
#         hashlib.sha256(mallory_update).hexdigest() == PAGE_HASH
hash_check = None

# TODO 2: Bob checks the tag: he computes the HMAC of the file he got and compares it with ALICE_TAG.
#         hmac.new(SHARED_KEY, data, "sha256").digest() gives the 32-byte tag of data;
#         hmac.compare_digest(x, y) compares two tags (like memcmp(x, y, 32) == 0).
#         Do it for alice_update and for mallory_update.
tag_check_alice = None
tag_check_mallory = None

# TODO 3: Bob writes a note and makes its tag himself, with the same SHARED_KEY:
#         bob_tag = hmac.new(SHARED_KEY, note, "sha256").digest()
#         Then Carol, a judge who is given the key, checks the note and bob_tag the same way as in TODO 2.
note = b"Alice owes Bob 500 pounds. Signed: Alice"
carol_check = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if hash_check is None:
    print("not done yet: TODO 1")
else:
    print("hash check of Mallory's file:", hash_check)
if tag_check_alice is None or tag_check_mallory is None:
    print("not done yet: TODO 2")
else:
    print("tag check of Alice's file:  ", tag_check_alice)
    print("tag check of Mallory's file:", tag_check_mallory)
if carol_check is None:
    print("not done yet: TODO 3")
else:
    print("Carol's check of the note:  ", carol_check)
