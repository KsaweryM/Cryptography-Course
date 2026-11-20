# Sizes and signing times of RSA-2048 and RSA-3072 (PSS) and ECDSA P-256: the note on the slide "Task 7: what we saw".
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives import hashes
pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32)
msg = b"Pay Bob 10 pounds. Alice"
for bits in (2048, 3072):
    k = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    t = time.perf_counter()
    for i in range(200): s = k.sign(msg, pss, hashes.SHA256())
    t = (time.perf_counter() - t) / 200
    print(bits, "key bytes", k.public_key().key_size // 8, "sig bytes", len(s), "sign ms %.2f" % (t * 1000))
e = ec.generate_private_key(ec.SECP256R1())
t = time.perf_counter()
for i in range(200): e.sign(msg, ec.ECDSA(hashes.SHA256()))
print("ecdsa sign ms %.3f" % ((time.perf_counter() - t) / 200 * 1000))
