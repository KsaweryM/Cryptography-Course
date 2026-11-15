# Task 4: audit Carol's certificates.
# Carol looks after the servers of Carol Corp. Her folder certs/ has every certificate she could find.
import datetime
from certinfo import load_folder, subject_cn, issuer_cn, expires, key_info, hash_name

# the day of the audit, fixed so that everybody gets the same answer
TODAY = datetime.datetime(2026, 12, 1, tzinfo=datetime.timezone.utc)
RENEW_DAYS = 30                       # renew when fewer days than this are left
WEAK_HASHES = ["md5", "sha1"]
MIN_RSA_BITS = 2048

certs = load_folder("certs")
problems = 0
for i in range(len(certs)):
    file, cert = certs[i]
    kind, bits = key_info(cert)
    print(f"{file:14} {subject_cn(cert):28} {kind:7} {bits:5} {hash_name(cert):7} from {issuer_cn(cert)}")

    # TODO 1: days_left = (expires(cert) - TODAY).days ; print it.

    # TODO 2: if days_left < 0: print "  EXPIRED"; else if days_left < RENEW_DAYS: print "  RENEW NOW".

    # TODO 3: if hash_name(cert) is in WEAK_HASHES: print "  WEAK HASH".

    # TODO 4: if the key is RSA with fewer than MIN_RSA_BITS bits: print "  WEAK KEY".
    #         Count every problem in `problems`.

print(problems, "problems in", len(certs), "certificates")
