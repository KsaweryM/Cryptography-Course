from signing import load_public_key, public_key_from_hex, verify, key_hex


def read_file(path):
    # like fopen(path, "rb") + fread in C: the whole file as bytes
    with open(path, "rb") as f:
        return f.read()


# Dave's Notes app downloads three files from the update server: the update, its signature and the public key.
# alice_server/ is Alice's real server. mallory_server/ is what Dave gets when Mallory controls the server.

# The key that Alice built into the Notes app when Dave installed it (32 bytes as hex).
BUILT_IN_KEY = "64ecb2f9acdd37ad69e20f64f73eb74fa218fc59e75237f7e51e51fc9778ec42"

# TODO 1: the update from Alice's server: read update.sh and update.sig, load public_key.pem with
#         load_public_key(path), and check with verify(public_key, data, signature).
alice_check = None

# TODO 2: the same three lines for the files in mallory_server/
mallory_check = None

# TODO 3: whose key did Mallory's server send? Compare key_hex(that key) with BUILT_IN_KEY (== on two strings).
mallory_key_is_alices = None

# TODO 4: check Mallory's update and signature with the built-in key: public_key_from_hex(BUILT_IN_KEY)
mallory_check_built_in = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if alice_check is None:
    print("not done yet: TODO 1")
else:
    print("Alice's server, key from the server:  ", alice_check)
if mallory_check is None:
    print("not done yet: TODO 2")
else:
    print("Mallory's server, key from the server:", mallory_check)
if mallory_key_is_alices is None:
    print("not done yet: TODO 3")
else:
    print("the key from Mallory's server is Alice's key:", mallory_key_is_alices)
if mallory_check_built_in is None:
    print("not done yet: TODO 4")
else:
    print("Mallory's server, built-in key:       ", mallory_check_built_in)
