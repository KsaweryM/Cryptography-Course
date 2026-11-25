# Task 11: a key from a password.
# Alice's diary app encrypts each diary with ChaCha20 (lecture 2). The key is not stored anywhere:
# it is made from the password with PBKDF2, a slow hash:
#   key = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, iterations, 32)
# A diary file: salt (16 bytes) | iterations (4 bytes) | nonce (12 bytes) | ciphertext.
import hashlib
import time
from chacha import chacha20


def read_diary(path):
    """Ready: the four parts of a diary file."""
    with open(path, "rb") as f:
        data = f.read()
    salt = data[0:16]
    iterations = int.from_bytes(data[16:20], "big")
    nonce = data[20:32]
    ciphertext = data[32:]
    return salt, iterations, nonce, ciphertext


def load_lines(path):
    """Ready: the lines of a text file."""
    out = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if line != "":
                out.append(line)
    return out


# TODO 1: Alice opens her own diary. Read diary_alice.bin, make the key from her password "violet kettle 1987"
#         (password.encode() gives the bytes), decrypt with chacha20(key, nonce, 1, ciphertext)
#         and print(f"iterations: {iterations}"), then print(text.decode())
print("not done yet: TODO 1")

# TODO 2: Mallory copied Bob's diary (diary_bob.bin) but not his password. Measure how long one key takes
#         with Bob's salt and iterations: print(f"one key: {seconds * 1000:.1f} ms")
print("not done yet: TODO 2")

# TODO 3: dictionary attack: for each word of wordlist.txt, in order, make the key and decrypt only the first
#         11 bytes (chacha20(key, nonce, 1, ciphertext[0:11])). Every diary starts with b"Dear diary,".
#         When it matches, print(f"found after {tries} tries: {word}") and stop; then print the whole diary
#         and print(f"attack: {seconds:.1f} s")
print("not done yet: TODO 3")

# TODO 4: OWASP asks for 600000 iterations of PBKDF2-HMAC-SHA256. The work grows with the iterations:
#         print(f"with 600000 iterations: about {seconds * 600000 / iterations / 60:.0f} minutes")
print("not done yet: TODO 4")
