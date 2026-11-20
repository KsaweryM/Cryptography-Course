# Task 5: one signature, two certificates.
# Mallory prepared the to-be-signed parts (tbsCertificate) of two certificates that differ in 6 bytes.
# Trusty CA signed A, the harmless one.
import hashlib
from trusty import load_file, verify, what_it_says

a = load_file("tbs_a.bin")
b = load_file("tbs_b.bin")
sig_md5 = load_file("signature_md5.bin")        # Trusty CA's signature over A, made with MD5
sig_sha256 = load_file("signature_sha256.bin")  # Trusty CA's signature over A, made with SHA-256

print("A says:", what_it_says(a))
print("B says:", what_it_says(b))

# Ready: what you already saw in Lecture 7, Task 4 (the collision of Wang and others, 2004)
differ = 0
for i in range(len(a)):
    if a[i] != b[i]:
        differ = differ + 1
print("bytes that differ:", differ, "of", len(a))
print("MD5     A:", hashlib.md5(a).hexdigest())
print("MD5     B:", hashlib.md5(b).hexdigest())
print("SHA-256 A:", hashlib.sha256(a).hexdigest())
print("SHA-256 B:", hashlib.sha256(b).hexdigest())

# TODO 1: check the MD5 signature: verify(a, sig_md5, "md5") and verify(b, sig_md5, "md5").
#         Print both: "MD5 signature on A:    " and "MD5 signature on B:    ".
print("not done yet: TODO 1")    # delete this line when TODO 1 is done

# TODO 2: check the SHA-256 signature the same way, on a and on b:
#         "SHA-256 signature on A:" and "SHA-256 signature on B:".
print("not done yet: TODO 2")    # delete this line when TODO 2 is done
