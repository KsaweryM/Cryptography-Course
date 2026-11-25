# Makes the two encrypted diaries of Task 11 (run from Lecture07-Collisions-and-Passwords/: python3 checks/make_task11.py).
# Fixed salts and nonces, so that running it again gives the same files; if you change anything, update
# Task11/README.md and the slide "Task 11: what we saw".
# File format: salt (16 bytes) | iterations (4 bytes, big-endian) | nonce (12 bytes) | ChaCha20 ciphertext (counter 1)
# key = PBKDF2-HMAC-SHA256(password, salt, iterations, 32 bytes)
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(ROOT, "Task11"))
from chacha import chacha20


def make(path, password, salt_hex, nonce_hex, iterations, text):
    salt = bytes.fromhex(salt_hex)
    nonce = bytes.fromhex(nonce_hex)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations, 32)
    data = salt + iterations.to_bytes(4, "big") + nonce + chacha20(key, nonce, 1, text.encode())
    with open(os.path.join(ROOT, path), "wb") as f:
        f.write(data)
    print("wrote", path, len(data), "bytes, key", key.hex()[:16] + "...")


make("Task11/diary_alice.bin", "violet kettle 1987", "a3f1094c7d2e58b6013f9ac4e27d6b80", "4b1e7790c2a35d08e6f19a2c",
     10000, "Dear diary, today I moved my savings to the new bank. The PIN is in the blue notebook.\n")
make("Task11/diary_bob.bin", "Cookie12", "17c08e5b92d4a63f0b8e71c25a9d3e46", "9d2c51e0a7b8346f1c0e5d92",
     10000, "Dear diary, Mallory asked again about the bike. I said no.\n")
