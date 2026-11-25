# Makes the ready files of the Lecture 9 tasks (keys, certificates, helper modules). Not for students.
# The keys come from fixed seeds, so every run gives the same files (Ed25519 signatures are deterministic).
#   python3 make_files.py
import datetime
import hashlib
import os
import shutil

from cryptography import x509
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

HERE = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(HERE)
UTC = datetime.timezone.utc


def key(name):
    return Ed25519PrivateKey.from_private_bytes(hashlib.sha256(("lecture6 " + name).encode()).digest())


def write_private(k, path):
    with open(path, "wb") as f:
        f.write(k.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                serialization.NoEncryption()))


def write_public(k, path):
    with open(path, "wb") as f:
        f.write(k.public_key().public_bytes(serialization.Encoding.PEM,
                                            serialization.PublicFormat.SubjectPublicKeyInfo))


def write_cert(c, path):
    with open(path, "wb") as f:
        f.write(c.public_bytes(serialization.Encoding.PEM))


def name(cn, o=None, c=None):
    attrs = []
    if c:
        attrs.append(x509.NameAttribute(NameOID.COUNTRY_NAME, c))
    if o:
        attrs.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, o))
    attrs.append(x509.NameAttribute(NameOID.COMMON_NAME, cn))
    return x509.Name(attrs)


CA = key("Trusty CA")
BOB = key("Bob")
MALLORY = key("Mallory")
ALICE = key("Alice")
CAROL = key("Carol")
DAVE = key("Dave")
SHOP = key("alice-shop")

CA_NAME = name("Trusty CA", "Trusty CA Ltd", "GB")
BOB_NAME = name("bob.example", "Bob Ltd", "GB")


def bob_cert():
    # exactly what Task 3 builds
    b = x509.CertificateBuilder()
    b = b.subject_name(BOB_NAME)
    b = b.issuer_name(CA_NAME)
    b = b.serial_number(0x4F3A9C2E71D05B88)
    b = b.not_valid_before(datetime.datetime(2026, 11, 1, tzinfo=UTC))
    b = b.not_valid_after(datetime.datetime(2027, 1, 30, tzinfo=UTC))
    b = b.public_key(BOB.public_key())
    return b.sign(CA, None)


def ku(**on):
    names = ["digital_signature", "content_commitment", "key_encipherment", "data_encipherment",
             "key_agreement", "key_cert_sign", "crl_sign", "encipher_only", "decipher_only"]
    args = {}
    for n in names:
        args[n] = on.get(n, False)
    return x509.KeyUsage(**args)


def task4_cert(subject, k, serial, sans, ca, eku, usage, pathlen=None, bc_critical=True, eku_critical=False):
    b = x509.CertificateBuilder().subject_name(subject).issuer_name(CA_NAME)
    b = b.serial_number(serial).public_key(k.public_key())
    b = b.not_valid_before(datetime.datetime(2026, 11, 1, tzinfo=UTC))
    b = b.not_valid_after(datetime.datetime(2027, 1, 30, tzinfo=UTC) if not ca else
                          datetime.datetime(2031, 11, 1, tzinfo=UTC))
    if sans:
        dns = []
        for s in sans:
            dns.append(x509.DNSName(s))
        b = b.add_extension(x509.SubjectAlternativeName(dns), critical=False)
    b = b.add_extension(x509.BasicConstraints(ca=ca, path_length=pathlen), critical=bc_critical)
    b = b.add_extension(usage, critical=True)
    if eku:
        b = b.add_extension(x509.ExtendedKeyUsage(eku), critical=eku_critical)
    b = b.add_extension(x509.SubjectKeyIdentifier.from_public_key(k.public_key()), critical=False)
    b = b.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(CA.public_key()), critical=False)
    return b.sign(CA, None)


def copy(src, task):
    shutil.copy(os.path.join(HERE, src), os.path.join(L6, task, src))


def main():
    # Task 2: a signed name card
    t = os.path.join(L6, "Task2")
    write_private(CA, os.path.join(t, "trusty_ca_private.pem"))
    write_public(CA, os.path.join(t, "trusty_ca_public.pem"))
    write_public(BOB, os.path.join(t, "bob_public.pem"))
    write_private(MALLORY, os.path.join(t, "mallory_private.pem"))
    write_public(MALLORY, os.path.join(t, "mallory_public.pem"))
    copy("signing.py", "Task2")

    # Task 3: Bob's certificate
    t = os.path.join(L6, "Task3")
    write_private(CA, os.path.join(t, "trusty_ca_private.pem"))
    write_public(CA, os.path.join(t, "trusty_ca_public.pem"))
    write_public(BOB, os.path.join(t, "bob_public.pem"))
    write_public(MALLORY, os.path.join(t, "mallory_public.pem"))
    copy("cert_tools.py", "Task3")
    copy("signing.py", "Task3")

    # Task 4: four certificates
    t = os.path.join(L6, "Task4")
    certs = {
        "cert_A.pem": task4_cert(name("www.alice-shop.example", "Alice Shop Ltd", "GB"), SHOP, 0x1A2B3C4D5E6F7081,
                                 ["alice-shop.example", "www.alice-shop.example"], False,
                                 [ExtendedKeyUsageOID.SERVER_AUTH], ku(digital_signature=True), bc_critical=False),
        "cert_B.pem": task4_cert(name("Trusty CA Issuing 1", "Trusty CA Ltd", "GB"), key("Trusty Issuing"),
                                 0x2B3C4D5E6F708192, None, True, None,
                                 ku(digital_signature=True, key_cert_sign=True, crl_sign=True), pathlen=0),
        "cert_C.pem": task4_cert(name("Carol Software Ltd", "Carol Software Ltd", "GB"), CAROL, 0x3C4D5E6F708192A3,
                                 None, False, [ExtendedKeyUsageOID.CODE_SIGNING], ku(digital_signature=True),
                                 eku_critical=True),
        "cert_D.pem": task4_cert(name("*.dave.example", "Dave Games Ltd", "GB"), DAVE, 0x4D5E6F708192A3B4,
                                 ["*.dave.example"], False,
                                 [ExtendedKeyUsageOID.SERVER_AUTH, ExtendedKeyUsageOID.CLIENT_AUTH],
                                 ku(digital_signature=True)),
    }
    for fn in certs:
        write_cert(certs[fn], os.path.join(t, fn))
    copy("cert_tools.py", "Task4")

    # Task 5: Bob's certificate, ready
    t = os.path.join(L6, "Task5")
    write_cert(bob_cert(), os.path.join(t, "bob.pem"))
    copy("cert_tools.py", "Task5")

    # Task 6: a self-signed certificate
    t = os.path.join(L6, "Task6")
    write_private(ALICE, os.path.join(t, "alice_private.pem"))
    write_private(MALLORY, os.path.join(t, "mallory_private.pem"))
    copy("cert_tools.py", "Task6")
    copy("signing.py", "Task6")

    # Task 7: two real certificates, saved on 15 November 2026
    t = os.path.join(L6, "Task7")
    shutil.copy(os.path.join(HERE, "cov_leaf.pem"), os.path.join(t, "coventry.pem"))
    shutil.copy(os.path.join(HERE, "bbc_leaf.pem"), os.path.join(t, "bbc.pem"))
    shutil.copy(os.path.join(L6, "Task4", "cert_D.pem"), os.path.join(t, "cert_D.pem"))
    copy("cert_tools.py", "Task7")

    # for the slides
    write_cert(bob_cert(), os.path.join(HERE, "bob.pem"))
    print("done")


main()
