"""Makes every certificate, key and CRL that the Lecture 8 tasks ship (run once; the files are in git).

    python3 make_files.py

Writes into ../TaskN/ and the same files into ../TaskN/solution/. Running it again makes NEW keys:
then the pins in Task8, the values in Task6/handshake_ready.py and the outputs copied into the READMEs
and the slides change, so run every solution again and update them.

All keys are ECDSA P-256. "Trusty Root CA" and its issuing CA play a private test CA; Mallory has her own.
Dates: the valid certificates start on 1 January 2025 or 1 November 2026 and end in 2028 or later,
so the tasks work during the whole course; the "expired" ones ended in 2026.
"""
import datetime
import hashlib
import os
import shutil

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def d(y, m, day):
    return datetime.datetime(y, m, day, 0, 0, 0)


def new_key():
    return ec.generate_private_key(ec.SECP256R1())


def name(cn, org=None):
    parts = []
    if org:
        parts.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, org))
    parts.append(x509.NameAttribute(NameOID.COMMON_NAME, cn))
    return x509.Name(parts)


def cert(subject, subject_key, issuer, issuer_key, serial, start, end, ca=False, path_len=None,
         dns=None, eku=None, issuer_pub=None):
    """issuer_pub: the public key for the Authority Key Identifier (normally the issuer key's)."""
    if issuer_pub is None:
        issuer_pub = issuer_key.public_key()
    b = x509.CertificateBuilder()
    b = b.subject_name(subject).issuer_name(issuer).public_key(subject_key.public_key())
    b = b.serial_number(serial).not_valid_before(start).not_valid_after(end)
    b = b.add_extension(x509.BasicConstraints(ca=ca, path_length=path_len), critical=True)
    if ca:
        ku = x509.KeyUsage(digital_signature=True, content_commitment=False, key_encipherment=False,
                           data_encipherment=False, key_agreement=False, key_cert_sign=True, crl_sign=True,
                           encipher_only=False, decipher_only=False)
    else:
        ku = x509.KeyUsage(digital_signature=True, content_commitment=False, key_encipherment=False,
                           data_encipherment=False, key_agreement=False, key_cert_sign=False, crl_sign=False,
                           encipher_only=False, decipher_only=False)
    b = b.add_extension(ku, critical=True)
    if eku is not None:
        b = b.add_extension(x509.ExtendedKeyUsage(eku), critical=False)
    if dns is not None:
        names = []
        for n in dns:
            names.append(x509.DNSName(n))
        b = b.add_extension(x509.SubjectAlternativeName(names), critical=False)
    b = b.add_extension(x509.SubjectKeyIdentifier.from_public_key(subject_key.public_key()), critical=False)
    b = b.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(issuer_pub), critical=False)
    return b.sign(issuer_key, hashes.SHA256())


def pem(c):
    return c.public_bytes(serialization.Encoding.PEM)


def key_pem(k):
    return k.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                           serialization.NoEncryption())


def write(task, rel, data):
    for base in (os.path.join(ROOT, task), os.path.join(ROOT, task, "solution")):
        path = os.path.join(base, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)


SERVER = [ExtendedKeyUsageOID.SERVER_AUTH]
CLIENT = [ExtendedKeyUsageOID.CLIENT_AUTH]

# ---------------------------------------------------------------- the Trusty CA (private test CA)
root_key = new_key()
root_name = name("Trusty Root CA", "Trusty CA")
root = cert(root_name, root_key, root_name, root_key, 0x01, d(2025, 1, 1), d(2036, 1, 1), ca=True)

int_key = new_key()
int_name = name("Trusty Issuing CA 1", "Trusty CA")
inter = cert(int_name, int_key, root_name, root_key, 0x0A01, d(2025, 1, 1), d(2031, 1, 1), ca=True, path_len=0)

mal_key = new_key()
mal_root_name = name("Mallory Root CA", "Mallory")
mal_root = cert(mal_root_name, mal_key, mal_root_name, mal_key, 0x66, d(2025, 1, 1), d(2036, 1, 1), ca=True)

# ---------------------------------------------------------------- Task 1: six servers
bob_key = new_key()
good = cert(name("bob.example"), bob_key, int_name, int_key, 0x1001, d(2026, 11, 1), d(2028, 11, 1),
            dns=["bob.example"], eku=SERVER)
expired = cert(name("bob.example"), bob_key, int_name, int_key, 0x1000, d(2025, 10, 1), d(2026, 10, 1),
               dns=["bob.example"], eku=SERVER)
carol_key = new_key()
wrong_name = cert(name("carol.example"), carol_key, int_name, int_key, 0x1002, d(2026, 11, 1), d(2028, 11, 1),
                  dns=["carol.example"], eku=SERVER)
mal_leaf_key = new_key()
unknown_ca = cert(name("bob.example"), mal_leaf_key, mal_root_name, mal_key, 0x6601, d(2026, 11, 1),
                  d(2028, 11, 1), dns=["bob.example"], eku=SERVER)
self_key = new_key()
self_signed = cert(name("bob.example"), self_key, name("bob.example"), self_key, 0x5E1F, d(2026, 11, 1),
                   d(2028, 11, 1), dns=["bob.example"], eku=SERVER)

write("Task1", "certs/root.pem", pem(root))
write("Task1", "certs/good.pem", pem(good) + pem(inter))
write("Task1", "certs/good.key", key_pem(bob_key))
write("Task1", "certs/expired.pem", pem(expired) + pem(inter))
write("Task1", "certs/expired.key", key_pem(bob_key))
write("Task1", "certs/wrong_name.pem", pem(wrong_name) + pem(inter))
write("Task1", "certs/wrong_name.key", key_pem(carol_key))
write("Task1", "certs/unknown_ca.pem", pem(unknown_ca))
write("Task1", "certs/unknown_ca.key", key_pem(mal_leaf_key))
write("Task1", "certs/self_signed.pem", pem(self_signed))
write("Task1", "certs/self_signed.key", key_pem(self_key))
write("Task1", "certs/no_intermediate.pem", pem(good))
write("Task1", "certs/no_intermediate.key", key_pem(bob_key))

# ---------------------------------------------------------------- Task 3: six chains, each breaks one check
# case 1: a good chain
write("Task3", "chains/root.pem", pem(root))
write("Task3", "chains/case1.pem", pem(good) + pem(inter))
# case 2: the intermediate has expired (the leaf is still valid)
int0_key = new_key()
int0_name = name("Trusty Issuing CA 0", "Trusty CA")
inter0 = cert(int0_name, int0_key, root_name, root_key, 0x0A00, d(2024, 1, 1), d(2026, 6, 30), ca=True, path_len=0)
leaf2 = cert(name("bob.example"), bob_key, int0_name, int0_key, 0x0F01, d(2026, 3, 1), d(2028, 3, 1),
             dns=["bob.example"], eku=SERVER)
write("Task3", "chains/case2.pem", pem(leaf2) + pem(inter0))
# case 3: a wildcard that does not cover the bare name
leaf3 = cert(name("*.bob.example"), bob_key, int_name, int_key, 0x1003, d(2026, 11, 1), d(2028, 11, 1),
             dns=["*.bob.example"], eku=SERVER)
write("Task3", "chains/case3.pem", pem(leaf3) + pem(inter))
# case 4: Mallory's own leaf (CA:FALSE) signs a certificate for bob.example
mleaf_key = new_key()
mleaf_name = name("mallory.example")
mleaf = cert(mleaf_name, mleaf_key, int_name, int_key, 0x1004, d(2026, 11, 1), d(2028, 11, 1),
             dns=["mallory.example"], eku=SERVER)
fake_bob_key = new_key()
fake_bob = cert(name("bob.example"), fake_bob_key, mleaf_name, mleaf_key, 0x7777, d(2026, 11, 1), d(2028, 11, 1),
                dns=["bob.example"], eku=SERVER)
write("Task3", "chains/case4.pem", pem(fake_bob) + pem(mleaf) + pem(inter))
# case 5: Mallory makes her own "Trusty Issuing CA 1": the same name, her key
fake_int = cert(int_name, mal_key, root_name, mal_key, 0x0A01, d(2025, 1, 1), d(2031, 1, 1), ca=True, path_len=0,
                issuer_pub=root_key.public_key())
leaf5 = cert(name("bob.example"), fake_bob_key, int_name, mal_key, 0x1005, d(2026, 11, 1), d(2028, 11, 1),
             dns=["bob.example"], eku=SERVER, issuer_pub=mal_key.public_key())
write("Task3", "chains/case5.pem", pem(leaf5) + pem(fake_int))
# case 6: a client certificate (clientAuth only) on a server
leaf6 = cert(name("bob.example"), bob_key, int_name, int_key, 0x1006, d(2026, 11, 1), d(2028, 11, 1),
             dns=["bob.example"], eku=CLIENT)
write("Task3", "chains/case6.pem", pem(leaf6) + pem(inter))

# ---------------------------------------------------------------- Task 4: a CRL
bob4 = good
carol4_key = new_key()
carol4 = cert(name("carol.example"), carol4_key, int_name, int_key, 0x1002, d(2026, 11, 1), d(2028, 11, 1),
              dns=["carol.example"], eku=SERVER)


def crl(issuer_key, last, nxt, revoked):
    b = x509.CertificateRevocationListBuilder().issuer_name(int_name).last_update(last).next_update(nxt)
    for serial, when, reason in revoked:
        r = x509.RevokedCertificateBuilder().serial_number(serial).revocation_date(when)
        r = r.add_extension(x509.CRLReason(reason), critical=False)
        b = b.add_revoked_certificate(r.build())
    b = b.add_extension(x509.CRLNumber(len(revoked) + 40), critical=False)
    return b.sign(issuer_key, hashes.SHA256())


revoked = [(0x0FFE, d(2026, 9, 2), x509.ReasonFlags.superseded),
           (0x1002, datetime.datetime(2026, 11, 10, 9, 30), x509.ReasonFlags.key_compromise)]
good_crl = crl(int_key, d(2026, 11, 15), d(2027, 12, 31), revoked)
old_crl = crl(int_key, d(2026, 10, 1), d(2026, 10, 8), revoked[:1])
fake_crl = crl(mal_key, d(2026, 11, 15), d(2027, 12, 31), revoked[:1])
write("Task4", "files/issuing_ca.pem", pem(inter))
write("Task4", "files/bob.pem", pem(bob4))
write("Task4", "files/carol.pem", pem(carol4))
write("Task4", "files/crl.pem", good_crl.public_bytes(serialization.Encoding.PEM))
write("Task4", "files/old_crl.pem", old_crl.public_bytes(serialization.Encoding.PEM))
write("Task4", "files/fake_crl.pem", fake_crl.public_bytes(serialization.Encoding.PEM))

# ---------------------------------------------------------------- Task 5: OCSP
write("Task5", "files/issuing_ca.pem", pem(inter))
write("Task5", "files/issuing_ca.key", key_pem(int_key))
write("Task5", "files/bob.pem", pem(bob4))
write("Task5", "files/carol.pem", pem(carol4))

# ---------------------------------------------------------------- Task 6: CertificateVerify
mal6_key = new_key()
today_hash = hashlib.sha256(b"ClientHello ServerHello EncryptedExtensions Certificate, today").digest()
old_hash = hashlib.sha256(b"ClientHello ServerHello EncryptedExtensions Certificate, yesterday").digest()


def content(h):
    return b" " * 64 + b"TLS 1.3, server CertificateVerify" + b"\x00" + h


sig_bob_today = bob_key.sign(content(today_hash), ec.ECDSA(hashes.SHA256()))
sig_mallory = mal6_key.sign(content(today_hash), ec.ECDSA(hashes.SHA256()))
sig_bob_old = bob_key.sign(content(old_hash), ec.ECDSA(hashes.SHA256()))
write("Task6", "files/bob.pem", pem(good))
vals = ("# Made by Lecture8/checks/make_files.py\n"
        "TODAY_HASH = '%s'\nOLD_HASH = '%s'\nSIG_BOB_TODAY = '%s'\nSIG_MALLORY = '%s'\nSIG_BOB_OLD = '%s'\n"
        % (today_hash.hex(), old_hash.hex(), sig_bob_today.hex(), sig_mallory.hex(), sig_bob_old.hex()))
write("Task6", "files/values.py", vals.encode())

# ---------------------------------------------------------------- Task 7: mutual TLS
staff_key = new_key()
staff_name = name("Bob Staff CA", "Bob Ltd")
staff = cert(staff_name, staff_key, staff_name, staff_key, 0x5A, d(2025, 1, 1), d(2036, 1, 1), ca=True)
alice_key = new_key()
alice = cert(name("Alice"), alice_key, staff_name, staff_key, 0x5A01, d(2026, 11, 1), d(2028, 11, 1), eku=CLIENT)
mal7_key = new_key()
mal7 = cert(name("Alice"), mal7_key, name("Alice"), mal7_key, 0x5A02, d(2026, 11, 1), d(2028, 11, 1), eku=CLIENT)
write("Task7", "certs/server_root.pem", pem(root))
write("Task7", "certs/server.pem", pem(good) + pem(inter))
write("Task7", "certs/server.key", key_pem(bob_key))
write("Task7", "certs/staff_ca.pem", pem(staff))
write("Task7", "certs/alice.pem", pem(alice))
write("Task7", "certs/alice.key", key_pem(alice_key))
write("Task7", "certs/mallory.pem", pem(mal7))
write("Task7", "certs/mallory.key", key_pem(mal7_key))

# ---------------------------------------------------------------- Task 8: pinning
api_name = name("api.bob.example")
k1 = new_key()
k2 = new_key()
k3 = new_key()
api_2026 = cert(api_name, k1, int_name, int_key, 0x2026, d(2026, 1, 10), d(2027, 1, 10), dns=["api.bob.example"],
                eku=SERVER)
api_same = cert(api_name, k1, int_name, int_key, 0x2027, d(2026, 12, 20), d(2027, 12, 20), dns=["api.bob.example"],
                eku=SERVER)
api_new = cert(api_name, k2, int_name, int_key, 0x2028, d(2026, 12, 20), d(2027, 12, 20), dns=["api.bob.example"],
               eku=SERVER)
api_backup = cert(api_name, k3, int_name, int_key, 0x2029, d(2026, 12, 20), d(2027, 12, 20),
                  dns=["api.bob.example"], eku=SERVER)
write("Task8", "certs/api_2026.pem", pem(api_2026))
write("Task8", "certs/api_2027_same_key.pem", pem(api_same))
write("Task8", "certs/api_2027_new_key.pem", pem(api_new))
write("Task8", "certs/api_2027_backup_key.pem", pem(api_backup))
backup_spki = k3.public_key().public_bytes(serialization.Encoding.DER,
                                          serialization.PublicFormat.SubjectPublicKeyInfo)
import base64
print("Task 8 backup pin:", base64.b64encode(hashlib.sha256(backup_spki).digest()).decode())
print("done")
