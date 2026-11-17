# Task 5: the leaked table without salt.
# The shop stored sha256(password) for every user. Mallory has the table and a list of common passwords.
import hashlib


def load_users(path):
    """Ready: reads lines user:digest. Returns two lists of the same length: names[i] and digests[i]."""
    names = []
    digests = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            parts = line.split(":")
            names.append(parts[0])
            digests.append(parts[1])
    return names, digests


def load_words(path):
    """Ready: the list of guesses, one per line."""
    words = []
    with open(path) as f:
        for line in f:
            words.append(line.rstrip("\n"))
    return words


names, digests = load_users("leaked_users.txt")
words = load_words("wordlist.txt")
print(f"{len(names)} users, {len(words)} guesses in the list")


# TODO 1: the server's check at login. Return True if sha256(typed) in hex equals the stored digest of user.
#         Find the index of user in names (an index loop), then compare
#         hashlib.sha256(typed.encode()).hexdigest() with digests[index].
def check_login(user, typed):
    return None


TRIES = ["monkey123", "monkey124"]
for t in range(len(TRIES)):
    ok = check_login("alice", TRIES[t])
    if ok is None:
        print("not done yet: TODO 1")
    else:
        print(f"alice types {TRIES[t]}: {ok}")

# TODO 2: the dictionary attack. For every word: compute its digest ONCE (count it in hashes = hashes + 1),
#         then compare it with the digest of every user. On a match, print f"{names[u]}: {word}"
#         and count the user in cracked.
hashes = 0
cracked = 0

# TODO 3: print the summary:
#   print(f"cracked {cracked} of {len(names)} users with {hashes} SHA-256 computations")
print("not done yet: TODO 2 and 3")

# TODO 4: look at the table: which users have the same digest? Print their names (two index loops).
print("not done yet: TODO 4")
