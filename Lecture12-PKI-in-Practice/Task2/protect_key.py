# Task 2: lock the key file.
# server.key is the private key of a web server. Right now anyone who can read the file has the key.
import os
from cryptography.hazmat.primitives import serialization

PASSPHRASE = b"purple-otter-42-teapot"     # in real life: typed in at start, or kept by a secrets manager

# TODO 1: read server.key (open(..., "rb").read()), print its first line and the file mode:
#         oct(os.stat("server.key").st_mode & 0o777)
#         Load it with serialization.load_pem_private_key(data, password=None) and print key.key_size.
print("not done yet: TODO 1")    # delete this line when TODO 1 is done

# TODO 2: write the same key to server-locked.key, encrypted with PASSPHRASE:
#         key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
#                           serialization.BestAvailableEncryption(PASSPHRASE))
#         Print the first line of the new file.
print("not done yet: TODO 2")    # delete this line when TODO 2 is done

# TODO 3: play Mallory, who copied server-locked.key: load it with password=None, then with b"123456".
#         Catch the errors (try / except (TypeError, ValueError) as e) and print them.
#         Then load it with PASSPHRASE and print key.key_size.
print("not done yet: TODO 3")    # delete this line when TODO 3 is done

# TODO 4: only the owner may read and write the file: os.chmod("server-locked.key", 0o600).
#         Print the new file mode as in TODO 1.
print("not done yet: TODO 4")    # delete this line when TODO 4 is done
