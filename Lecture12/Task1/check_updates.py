# Task 1: is this update still trusted?
# Bob's computer checks five files signed by Alice Software Ltd.
from codesign import load_cert, load_updates, verify_signature, verify_timestamp, valid_from, valid_until, NOW

publisher = load_cert("publisher.pem")      # Alice Software Ltd, code signing
tsa       = load_cert("tsa.pem")            # Trusty Time Stamping
updates   = load_updates("updates.json")

print("Alice's certificate is valid from", valid_from(publisher).date(), "to", valid_until(publisher).date())
print("Today is", NOW.date())
print()

for i in range(len(updates)):
    u = updates[i]
    print(u["file"])

    # TODO 1: check Alice's signature over u["data"] with verify_signature(publisher, ...).
    #         If it is wrong: print "  REJECT: bad signature, the file was changed" and continue.

    # TODO 2: no timestamp (u["timestamp"] is None): we do not know when it was signed, only that it is NOW.
    #         Accept only if NOW is inside the validity period, otherwise print
    #         "  REJECT: no timestamp and the certificate expired on ..." and continue.

    # TODO 3: t = verify_timestamp(tsa, u["signature"], u["timestamp"]).
    #         If t is None: print "  REJECT: bad timestamp" and continue.

    # TODO 4: if valid_from(publisher) <= t <= valid_until(publisher): print "  ACCEPT: signed on ...",
    #         otherwise print "  REJECT: signed on ..., after the certificate expired".
