# Task 6: the leaked table with salt.
# This shop stored, for every user, a random salt and sha256(salt + password). The salt is not secret.
import hashlib


def load_users(path):
    """Ready: reads lines user:salt:digest. Returns three lists: names[i], salts[i] (bytes), digests[i] (hex)."""
    names = []
    salts = []
    digests = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            parts = line.split(":")
            names.append(parts[0])
            salts.append(bytes.fromhex(parts[1]))
            digests.append(parts[2])
    return names, salts, digests


def load_words(path):
    """Ready: the list of guesses, one per line."""
    words = []
    with open(path) as f:
        for line in f:
            words.append(line.rstrip("\n"))
    return words


names, salts, digests = load_users("leaked_users.txt")
words = load_words("wordlist.txt")
print(f"{len(names)} users, {len(words)} guesses in the list")
print(f"chloe: salt {salts[2].hex()}  digest {digests[2][:16]}...")
print(f"dave:  salt {salts[3].hex()}  digest {digests[3][:16]}...")

# TODO 1: the server's check at login, for user number u:
#         hashlib.sha256(salts[u] + typed.encode()).hexdigest() == digests[u]
def check_login(u, typed):
    return None


ok = check_login(0, "monkey123")
if ok is None:
    print("not done yet: TODO 1")
else:
    print("alice types monkey123:", ok)

# TODO 2: the dictionary attack, user by user. For every user u, go through the words:
#         compute sha256(salts[u] + word) (count it: hashes = hashes + 1) and compare with digests[u].
#         On a match print f"{names[u]}: {word}", count the user in cracked and stop with this user (break).
hashes = 0
cracked = 0

# TODO 3: print the summary:
#   print(f"cracked {cracked} of {len(names)} users with {hashes} SHA-256 computations")
print("not done yet: TODO 2 and 3")
