# Ready helper for Task 5: Trusty CA's public key and what a request says. Treat it as a black box.
#
#   load_file(path)                         -> the bytes of a file
#   CA_PUBLIC_KEY                           -> Trusty CA's RSA public key (from trusty-ca-public.pem)
#   verify(data, signature, hash_name)      -> True / False: is this Trusty CA's signature over data?
#                                              hash_name is "md5" or "sha256": the hash the CA used
#   what_it_says(data)                      -> the sentence that a program reading this request shows
#
# Simplified: a real certificate keeps the strange collision bytes inside the public key field,
# where nobody reads them. Here one byte of those bytes (byte 19) chooses which sentence is shown.
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def load_file(path):
    with open(path, "rb") as f:
        return f.read()


CA_PUBLIC_KEY = serialization.load_pem_public_key(load_file("trusty-ca-public.pem"))


def verify(data, signature, hash_name):
    if hash_name == "md5":
        h = hashes.MD5()
    else:
        h = hashes.SHA256()
    try:
        CA_PUBLIC_KEY.verify(signature, data, padding.PKCS1v15(), h)
        return True
    except InvalidSignature:
        return False


def what_it_says(data):
    lines = data[128:].decode().split("\n")
    if data[19] == 0x87:
        wanted = "TEXT0: "
    else:
        wanted = "TEXT1: "
    for i in range(len(lines)):
        if lines[i].startswith(wanted):
            return lines[i][len(wanted):]
    return "?"
