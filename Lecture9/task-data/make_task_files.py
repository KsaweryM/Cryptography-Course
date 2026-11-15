# Makes the ready files (certificates, keys, data) of the Lecture 9 tasks.
# Run once: python3 make_task_files.py   (needs cryptography 41+ and the openssl command for Task 4)
# The files are shipped in the task folders, so the fingerprints and dates on the slides stay the same.
# Running it again makes NEW keys and certificates: then update the READMEs, the figures and main.tex.
import datetime
import hashlib
import json
import os
import subprocess
import sys

from cryptography import x509
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa, ed25519, padding

HERE = os.path.dirname(os.path.abspath(__file__))
L9 = os.path.dirname(HERE)
UTC = datetime.timezone.utc


def d(y, m, day, h=0, mi=0):
    return datetime.datetime(y, m, day, h, mi, tzinfo=UTC)


def name(cn, org=None):
    attrs = [x509.NameAttribute(NameOID.COMMON_NAME, cn)]
    if org:
        attrs.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, org))
    return x509.Name(attrs)


def make_cert(subject, issuer, pub, issuer_key, start, end, ca=False, dns=None, eku=None, serial=None, h=None):
    b = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(pub)
    b = b.serial_number(serial if serial else x509.random_serial_number())
    b = b.not_valid_before(start).not_valid_after(end)
    b = b.add_extension(x509.BasicConstraints(ca=ca, path_length=None), critical=True)
    if dns:
        names = []
        for n in dns:
            names.append(x509.DNSName(n))
        b = b.add_extension(x509.SubjectAlternativeName(names), critical=False)
    if eku:
        b = b.add_extension(x509.ExtendedKeyUsage(eku), critical=eku == [ExtendedKeyUsageOID.TIME_STAMPING])
    if isinstance(issuer_key, ed25519.Ed25519PrivateKey):
        return b.sign(issuer_key, None)
    return b.sign(issuer_key, h if h else hashes.SHA256())


def pem(cert):
    return cert.public_bytes(serialization.Encoding.PEM)


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    mode = "wb" if isinstance(data, bytes) else "w"
    with open(path, mode) as f:
        f.write(data)


def keypem(key):
    return key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                             serialization.NoEncryption())


# ---------------------------------------------------------------- Task 1: code signing and timestamps
def task1():
    t = os.path.join(L9, "Task1")
    ca_key = ec.generate_private_key(ec.SECP256R1())
    ca_name = name("Trusty Code CA", "Trusty CA")
    pub_key = ec.generate_private_key(ec.SECP256R1())
    tsa_key = ec.generate_private_key(ec.SECP256R1())
    publisher = make_cert(name("Alice Software Ltd", "Alice Software Ltd"), ca_name, pub_key.public_key(), ca_key,
                          d(2024, 1, 1), d(2025, 1, 1), eku=[ExtendedKeyUsageOID.CODE_SIGNING])
    tsa = make_cert(name("Trusty Time Stamping", "Trusty CA"), ca_name, tsa_key.public_key(), ca_key,
                    d(2023, 1, 1), d(2033, 1, 1), eku=[ExtendedKeyUsageOID.TIME_STAMPING])
    write(os.path.join(t, "publisher.pem"), pem(publisher))
    write(os.path.join(t, "tsa.pem"), pem(tsa))

    def sign(data):
        return pub_key.sign(data, ec.ECDSA(hashes.SHA256()))

    def stamp(signature, when):
        time = when.strftime("%Y-%m-%dT%H:%M:%SZ")
        msg = hashlib.sha256(signature).digest() + time.encode()
        return {"time": time, "tsa_signature": tsa_key.sign(msg, ec.ECDSA(hashes.SHA256())).hex()}

    ups = []
    a = b"PhotoEdit 2.1 installer\n" + bytes(range(64))
    sa = sign(a)
    ups.append({"file": "photoedit-2.1-setup.exe", "data": a.hex(), "signature": sa.hex(),
                "timestamp": stamp(sa, d(2024, 6, 12, 10, 15))})
    b = b"PhotoEdit 2.2 update\n" + bytes(range(64, 128))
    sb = sign(b)
    ups.append({"file": "photoedit-2.2-update.exe", "data": b.hex(), "signature": sb.hex(), "timestamp": None})
    c = b"PhotoEdit 2.3 update\n" + bytes(range(128, 192))
    sc = sign(c)
    ups.append({"file": "photoedit-2.3-update.exe", "data": c.hex(), "signature": sc.hex(),
                "timestamp": stamp(sc, d(2025, 3, 2, 22, 40))})
    e = b"PhotoEdit 2.4 update\n" + bytes(range(192, 256))
    se = sign(e)
    tok = stamp(se, d(2025, 5, 20, 3, 5))
    tok["time"] = "2024-05-20T03:05:00Z"   # Mallory edits the time, the TSA signature stays
    ups.append({"file": "photoedit-2.4-update.exe", "data": e.hex(), "signature": se.hex(), "timestamp": tok})
    m = a.replace(b"installer", b"installer + a little extra", 1)
    ups.append({"file": "photoedit-2.1-setup-mirror.exe", "data": m.hex(), "signature": sa.hex(),
                "timestamp": stamp(sa, d(2024, 6, 12, 10, 15))})
    write(os.path.join(t, "updates.json"), json.dumps(ups, indent=2) + "\n")


# ---------------------------------------------------------------- Task 2: a key file
def task2():
    key = rsa.generate_private_key(65537, 2048)
    write(os.path.join(L9, "Task2", "server.key"), keypem(key))


# ---------------------------------------------------------------- Task 3: four TLS servers
def task3():
    c = os.path.join(L9, "Task3", "certs")
    ca_key = ec.generate_private_key(ec.SECP256R1())
    ca = make_cert(name("Trusty CA", "Trusty CA"), name("Trusty CA", "Trusty CA"), ca_key.public_key(), ca_key,
                   d(2025, 1, 1), d(2035, 1, 1), ca=True)
    write(os.path.join(c, "trusty-ca.pem"), pem(ca))
    srv = [ec.generate_private_key(ec.SECP256R1()) for _ in range(4)]
    shop = make_cert(name("shop.alice.example"), ca.subject, srv[0].public_key(), ca_key,
                     d(2026, 9, 1), d(2027, 3, 20), dns=["shop.alice.example"], eku=[ExtendedKeyUsageOID.SERVER_AUTH])
    selfsigned = make_cert(name("shop.alice.example"), name("shop.alice.example"), srv[1].public_key(), srv[1],
                           d(2026, 9, 1), d(2027, 3, 20), dns=["shop.alice.example"])
    own = make_cert(name("mallory.example"), ca.subject, srv[2].public_key(), ca_key,
                    d(2026, 9, 1), d(2027, 3, 20), dns=["mallory.example"], eku=[ExtendedKeyUsageOID.SERVER_AUTH])
    expired = make_cert(name("shop.alice.example"), ca.subject, srv[3].public_key(), ca_key,
                        d(2025, 2, 1), d(2025, 8, 20), dns=["shop.alice.example"], eku=[ExtendedKeyUsageOID.SERVER_AUTH])
    names = ["shop", "mallory-selfsigned", "mallory-own-name", "shop-expired"]
    certs = [shop, selfsigned, own, expired]
    for i in range(4):
        write(os.path.join(c, names[i] + ".pem"), pem(certs[i]))
        write(os.path.join(c, names[i] + ".key"), keypem(srv[i]))


# ---------------------------------------------------------------- Task 4: Carol's inventory
def task4():
    c = os.path.join(L9, "Task4", "certs")
    ca_key = ec.generate_private_key(ec.SECP384R1())
    ca_name = name("Carol Corp Internal CA", "Carol Corp")
    pub_ca_name = name("Trusty CA", "Trusty CA")
    pub_ca_key = ec.generate_private_key(ec.SECP256R1())
    items = [
        ("www.pem", "www.carol-corp.example", ec.generate_private_key(ec.SECP256R1()), pub_ca_name, pub_ca_key,
         d(2026, 10, 12), d(2027, 4, 30)),
        ("mail.pem", "mail.carol-corp.example", rsa.generate_private_key(65537, 2048), pub_ca_name, pub_ca_key,
         d(2026, 6, 14), d(2026, 12, 12)),
        ("vpn.pem", "vpn.carol-corp.example", rsa.generate_private_key(65537, 3072), ca_name, ca_key,
         d(2026, 2, 20), d(2027, 2, 20)),
        ("printer.pem", "printer.carol-corp.example", rsa.generate_private_key(65537, 2048), ca_name, ca_key,
         d(2024, 10, 3), d(2026, 10, 3)),
        ("api.pem", "api.carol-corp.example", ec.generate_private_key(ec.SECP384R1()), pub_ca_name, pub_ca_key,
         d(2026, 6, 7), d(2026, 12, 24)),
        ("build.pem", "build.carol-corp.example", ed25519.Ed25519PrivateKey.generate(), ca_name, ca_key,
         d(2026, 7, 1), d(2027, 7, 1)),
    ]
    for f, cn, key, iss, iss_key, start, end in items:
        cert = make_cert(name(cn, "Carol Corp"), iss, key.public_key(), iss_key, start, end, dns=[cn])
        write(os.path.join(c, f), pem(cert))
    # the old ones: cryptography refuses to sign with SHA-1 or MD5, so openssl makes them
    old = [("intranet.pem", "intranet.carol-corp.example", "sha1", "1024", "1200"),
           ("camera.pem", "camera.carol-corp.example", "md5", "2048", "700")]
    for f, cn, md, bits, days in old:
        tmpkey = os.path.join(HERE, "build-" + f + ".key")
        subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:" + bits, "-nodes", "-keyout", tmpkey,
                        "-out", os.path.join(c, f), "-" + md, "-days", days, "-subj", "/CN=" + cn + "/O=Carol Corp",
                        "-addext", "subjectAltName=DNS:" + cn], check=True, capture_output=True)
        os.remove(tmpkey)


# ---------------------------------------------------------------- Task 5: one signature, two documents
COLL_A = ("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
          "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
          "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
          "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")
COLL_B = ("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89"
          "55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b"
          "d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0"
          "e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70")
SUFFIX = (b"\nTEXT0: Trusty CA certifies: shop.alice.example is a website. It may NOT sign certificates.\n"
          b"TEXT1: Trusty CA certifies: Mallory is a CA. She may sign certificates for any website.\n")


def task5():
    t = os.path.join(L9, "Task5")
    a = bytes.fromhex(COLL_A) + SUFFIX
    b = bytes.fromhex(COLL_B) + SUFFIX
    assert hashlib.md5(a).digest() == hashlib.md5(b).digest()
    write(os.path.join(t, "request_a.bin"), a)
    write(os.path.join(t, "request_b.bin"), b)
    key = rsa.generate_private_key(65537, 2048)
    write(os.path.join(t, "trusty-ca-public.pem"), key.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    write(os.path.join(t, "signature_md5.bin"), key.sign(a, padding.PKCS1v15(), hashes.MD5()))
    write(os.path.join(t, "signature_sha256.bin"), key.sign(a, padding.PKCS1v15(), hashes.SHA256()))


# ---------------------------------------------------------------- Task 6: a CT log
def task6():
    t = os.path.join(L9, "Task6")
    cas = {}
    for cn in ["Trusty CA", "Shady CA", "Green CA"]:
        cas[cn] = ec.generate_private_key(ec.SECP256R1())
    entries = [
        ("bob-bakery.example", ["bob-bakery.example", "www.bob-bakery.example"], "Green CA", d(2026, 10, 2)),
        ("alice-shop.example", ["alice-shop.example", "www.alice-shop.example"], "Trusty CA", d(2026, 10, 5)),
        ("carol.example", ["carol.example"], "Green CA", d(2026, 10, 9)),
        ("api.alice-shop.example", ["api.alice-shop.example"], "Trusty CA", d(2026, 10, 14)),
        ("alice-shop.example.mallory.example", ["alice-shop.example.mallory.example"], "Green CA", d(2026, 10, 21)),
        ("dave.example", ["dave.example", "mail.dave.example"], "Trusty CA", d(2026, 10, 25)),
        ("alice-shop.example", ["alice-shop.example", "www.alice-shop.example"], "Shady CA", d(2026, 11, 2)),
        ("login.alice-shop.example", ["login.alice-shop.example"], "Trusty CA", d(2026, 11, 6)),
        ("bob.example", ["bob.example"], "Shady CA", d(2026, 11, 9)),
    ]
    out = b""
    mine = []
    for cn, dns, ca, start in entries:
        k = ec.generate_private_key(ec.SECP256R1())
        cert = make_cert(name(cn), name(ca, ca), k.public_key(), cas[ca], start, start + datetime.timedelta(days=199),
                         dns=dns, eku=[ExtendedKeyUsageOID.SERVER_AUTH])
        out += pem(cert)
        if ca == "Trusty CA" and cn in ("alice-shop.example", "api.alice-shop.example"):
            mine.append(cert.fingerprint(hashes.SHA256()).hex())
    write(os.path.join(t, "ct_log.pem"), out)
    text = "# SHA-256 fingerprints of the certificates that Alice ordered for alice-shop.example\n"
    for m in mine:
        text += m + "\n"
    write(os.path.join(t, "my_orders.txt"), text)


if __name__ == "__main__":
    todo = sys.argv[1:] if len(sys.argv) > 1 else ["1", "2", "3", "4", "5", "6"]
    for n in todo:
        globals()["task" + n]()
        print("Task" + n + ": done")
