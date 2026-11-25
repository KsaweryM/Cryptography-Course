# Task 10: a password hash that needs memory (scrypt).
# hashlib.scrypt is in the Python standard library (it calls OpenSSL, C code).
#   hashlib.scrypt(password, salt=salt, n=n, r=8, p=1, maxmem=limit, dklen=32)
#   n: how many 128 * r byte pieces scrypt keeps in its table; memory = 128 * r * n bytes
#   maxmem: the most memory scrypt may use; if it needs more, it raises ValueError
import hashlib
import time

password = b"violet kettle 1987"
salt = bytes.fromhex("5d0c7b2e9a41f3686e1d22b07c9a4f15")
MIB = 1024 * 1024

# TODO 1: for k in 12, 13, 14, 15 (range(12, 16)): n = 2 ** k. Measure
#         hashlib.scrypt(password, salt=salt, n=n, r=8, p=1, maxmem=64 * MIB, dklen=32)
#         three times and keep the shortest time (the computer does other things too); compute memory = 128 * 8 * n, and print(f"n = 2^{k}: {seconds:.3f} s, {memory // MIB} MiB")
print("not done yet: TODO 1")

# TODO 2: a device that gives scrypt at most 16 MiB: call scrypt with n = 2 ** 15 and maxmem = 16 * MIB
#         inside try: ... except ValueError: ... and print "n = 2^15 with at most 16 MiB: refused"
#         (or "n = 2^15 with at most 16 MiB: done" if it works)
print("not done yet: TODO 2")

# TODO 3: one graphics card: 24 GiB of memory, 16384 cores. How many guesses fit in its memory at once?
#         bcrypt needs about 4 KiB per guess, scrypt with n = 2^15 needs 32 MiB per guess.
#         print(f"bcrypt: {bcrypt_at_once} guesses fit at once")
#         print(f"scrypt n = 2^15: {scrypt_at_once} guesses fit at once, for 16384 cores")
print("not done yet: TODO 3")
