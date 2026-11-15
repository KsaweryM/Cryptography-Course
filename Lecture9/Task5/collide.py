# Task 5: one signature, two documents.
# Mallory made two requests that differ in 6 bytes. Trusty CA signed request A, the harmless one.
import hashlib
from trusty import load_file, verify, what_it_says

a = load_file("request_a.bin")
b = load_file("request_b.bin")
sig_md5 = load_file("signature_md5.bin")        # Trusty CA's signature over A, made with MD5
sig_sha256 = load_file("signature_sha256.bin")  # Trusty CA's signature over A, made with SHA-256

print("A says:", what_it_says(a))
print("B says:", what_it_says(b))

# TODO 1: count the bytes where a and b differ (an index loop over range(len(a))) and print the count.

# TODO 2: print the MD5 and the SHA-256 of a and of b: hashlib.md5(a).hexdigest(), hashlib.sha256(a).hexdigest()

# TODO 3: check the MD5 signature: verify(a, sig_md5, "md5") and verify(b, sig_md5, "md5"). Print both.

# TODO 4: check the SHA-256 signature the same way, on a and on b. Print both.
