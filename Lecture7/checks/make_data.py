# Makes the data files of Tasks 4, 5, 6 and 8 (run from Lecture7/: python3 checks/make_data.py).
# Running it again gives the same files: the salts come from a fixed seed, so that the README files,
# the slides and the lecturer's guide stay correct. If you change anything here, update them.
#
# Task 4 needs two real collisions, taken from public files:
#   - MD5: the two 128-byte messages of Wang, Feng, Lai and Yu (2004), as in Lecture12/Task5 (bytes 0 to 127
#     of request_a.bin and request_b.bin there);
#   - SHA-1: bytes 0 to 319 of shattered-1.pdf and shattered-2.pdf (https://shattered.io, 2017), downloaded
#     2026-11-17; pass the folder with the two PDFs as the first argument.
import hashlib
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")


def write(path, data):
    with open(os.path.join(ROOT, path), "wb") as f:
        f.write(data)
    print("wrote", path, len(data), "bytes")


# ---------------- Task 4: real collisions ----------------
md5_a = bytes.fromhex(
    "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")
md5_b = bytearray(md5_a)
# the 6 bytes that differ (Wang et al. 2004): bytes 19, 45, 59, 83, 109, 123 get +0x80 or -0x80
for i in (19, 45, 59, 83, 109, 123):
    md5_b[i] = md5_b[i] ^ 0x80
md5_b = bytes(md5_b)
assert hashlib.md5(md5_a).digest() == hashlib.md5(md5_b).digest()
write("Task4/md5_a.bin", md5_a)
write("Task4/md5_b.bin", md5_b)

if len(sys.argv) > 1:
    s1 = open(os.path.join(sys.argv[1], "shattered-1.pdf"), "rb").read()[:320]
    s2 = open(os.path.join(sys.argv[1], "shattered-2.pdf"), "rb").read()[:320]
    assert hashlib.sha1(s1).digest() == hashlib.sha1(s2).digest()
    write("Task4/sha1_a.bin", s1)
    write("Task4/sha1_b.bin", s2)
else:
    print("Task 4 SHA-1 files kept (give the folder with shattered-1.pdf and shattered-2.pdf to remake them)")

# ---------------- the word list of Tasks 5 and 6 ----------------
# Made up for this course in the style of real lists of common passwords (no real leaked data).
TOP = ["123456", "password", "123456789", "12345", "12345678", "qwerty", "1234567", "111111", "1234567890",
       "123123", "abc123", "1234", "password1", "iloveyou", "1q2w3e4r", "000000", "qwerty123", "zaq12wsx",
       "dragon", "sunshine", "princess", "letmein", "654321", "monkey", "27653", "1qaz2wsx", "123321",
       "qwertyuiop", "superman", "asdfghjkl", "football", "baseball", "welcome", "shadow", "master",
       "michael", "jennifer", "trustno1", "hello", "freedom", "whatever", "qazwsx", "ninja", "mustang",
       "password123", "admin", "login", "starwars", "passw0rd", "charlie", "aa123456", "donald", "batman",
       "access", "flower", "hottie", "loveme", "pokemon", "solo", "666666", "7777777", "987654321"]
WORDS = ["dragon", "sunshine", "princess", "monkey", "football", "baseball", "soccer", "hockey", "summer",
         "winter", "spring", "autumn", "liverpool", "chelsea", "arsenal", "london", "coventry", "england",
         "london", "paris", "berlin", "tiger", "lion", "eagle", "falcon", "panther", "wolf", "bear", "shark",
         "cookie", "cheese", "pizza", "banana", "apple", "orange", "lemon", "cherry", "chocolate", "coffee",
         "purple", "yellow", "silver", "golden", "orange", "black", "blue", "green", "red", "pink",
         "jordan", "thomas", "daniel", "jessica", "ashley", "hannah", "andrew", "joshua", "matthew",
         "oliver", "harry", "george", "emily", "sophie", "charlotte", "william", "james", "jack", "lucy",
         "computer", "internet", "secret", "magic", "music", "guitar", "piano", "rocket", "galaxy", "planet",
         "matrix", "hunter", "killer", "ranger", "pirate", "angel", "devil", "heaven", "flower", "butterfly",
         "family", "friends", "lovely", "happy", "smile", "forever", "always", "nothing", "sparky", "buster",
         "bailey", "maggie", "molly", "buddy", "rocky", "lucky", "ginger", "pepper", "biscuit", "teddy",
         "letmein", "welcome", "hello", "master", "freedom", "shadow", "passion", "dream", "star", "moon"]
SUFFIX = ["", "1", "12", "123", "1234", "!", "01", "007", "69", "99", "2000", "2023", "2024", "2025", "2026"]
words = []
seen = {}
for i in range(len(TOP)):
    if TOP[i] not in seen:
        seen[TOP[i]] = True
        words.append(TOP[i])
for i in range(len(WORDS)):
    for j in range(len(SUFFIX)):
        for w in (WORDS[i], WORDS[i].capitalize()):
            cand = w + SUFFIX[j]
            if cand not in seen:
                seen[cand] = True
                words.append(cand)
text = ("\n".join(words) + "\n").encode()
write("Task5/wordlist.txt", text)
write("Task6/wordlist.txt", text)

# ---------------- the users of Tasks 5 and 6 ----------------
USERS = [("alice", "monkey123"), ("bob", "Liverpool1"), ("carol", "iloveyou"), ("dave", "iloveyou"),
         ("erin", "Tr0ub4dor&3"), ("frank", "qwerty"), ("grace", "dragon2024"),
         ("heidi", "correct horse battery staple"), ("ivan", "123456"), ("judy", "Summer2025"),
         ("oscar", "football!"), ("peggy", "kx7#Qm2v!pL9")]
for name, pw in USERS:
    assert (pw in seen) == (name not in ("erin", "heidi", "peggy")), name

lines = ["# Leaked from the database of a small web shop. user:sha256(password) in hex. No salt."]
for name, pw in USERS:
    lines.append(name + ":" + hashlib.sha256(pw.encode()).hexdigest())
write("Task5/leaked_users.txt", ("\n".join(lines) + "\n").encode())

rng = random.Random(7)
lines = ["# Leaked from the database of a better web shop. user:salt:sha256(salt + password), all in hex."]
for name, pw in USERS:
    salt = bytes(rng.randrange(256) for _ in range(16))
    lines.append(name + ":" + salt.hex() + ":" + hashlib.sha256(salt + pw.encode()).hexdigest())
write("Task6/leaked_users.txt", ("\n".join(lines) + "\n").encode())

# ---------------- Task 8: one bcrypt text, cost 4 ----------------
sys.path.insert(0, os.path.join(ROOT, "Task8"))
import bcrypt_ready
TOP20 = TOP[:20]
salt_text = bcrypt_ready._b64_encode(bytes(rng.randrange(256) for _ in range(16)))
stored = bcrypt_ready.bcrypt_with_salt("sunshine", 4, salt_text)
assert "sunshine" in TOP20
write("Task8/stolen_bcrypt.txt", ("# victor, from the database of a shop that uses bcrypt\n" + stored + "\n").encode())
write("Task8/top20.txt", ("\n".join(TOP20) + "\n").encode())
