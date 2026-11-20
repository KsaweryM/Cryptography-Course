# Task 1: is this update still trusted?
# Bob's computer checks six files signed by Alice Software Ltd.
from codesign import (load_cert, load_updates, load_crl, verify_signature, verify_timestamp,
                      valid_from, valid_until, revoked_since, NOW)

publisher = load_cert("publisher.pem")      # Alice Software Ltd, code signing
tsa       = load_cert("tsa.pem")            # Trusty Time Stamping
crl       = load_crl("code-ca.crl")         # the revocation list of Trusty Code CA
updates   = load_updates("updates.json")
stolen    = revoked_since(crl, publisher)   # since when Alice's key must not be trusted

print("Alice's certificate is valid from", valid_from(publisher).date(), "to", valid_until(publisher).date())
print("Revoked: her key is not trusted since", stolen.date())
print("Today is", NOW.date())
print()

for i in range(len(updates)):
    u = updates[i]
    print(u["file"])

    # TODO 1: check Alice's signature over u["data"] with verify_signature(publisher, u["data"], u["signature"]).
    #         If it is wrong: print "  REJECT: bad signature, the file was changed" and continue.

    # TODO 2: no timestamp (u["timestamp"] is None): we do not know when it was signed, only that it is NOW.
    #         Accept only if NOW is inside the validity period, otherwise print
    #         "  REJECT: no timestamp and the certificate expired on 2025-01-01" (the date from valid_until)
    #         and continue.

    # TODO 3: t = verify_timestamp(tsa, u["signature"], u["timestamp"]).
    #         If t is None: print "  REJECT: bad timestamp" and continue.

    # TODO 4: if t is not inside the validity period (valid_from(publisher) <= t <= valid_until(publisher)):
    #         print "  REJECT: signed on 2025-03-02 after the certificate expired" (the date from t) and continue.

    # TODO 5: if t >= stolen: print "  REJECT: signed on ... after the key was stolen (revoked since ...)";
    #         otherwise print "  ACCEPT: signed on ... while the certificate was valid". Then continue.

    print("  not done yet: TODO 1 to 5")    # delete this line when every TODO prints a verdict
