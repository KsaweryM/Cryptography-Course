"""Task 4: is Bob's or Carol's certificate revoked? Ask three CRLs, and trust only a good one."""
from crl_ready import NOW, load_cert, load_crl, name_of, next_update, revoked_on, reason_of

ca = load_cert("issuing_ca.pem")                 # the CA that issued both certificates and signs the CRL
certs = [load_cert("bob.pem"), load_cert("carol.pem")]
LISTS = ["crl.pem", "old_crl.pem", "fake_crl.pem"]


def list_is_good(crl):
    """Returns "OK", or why this CRL must not be used."""
    # TODO 1: the signature. crl.is_signature_valid(ca.public_key()) is True only if the CA signed it.
    #         If not, return "bad signature"
    # TODO 2: the freshness. If next_update(crl) is before NOW,
    #         return "too old (next update was %s)" % next_update(crl).date()
    return "OK"


for k in range(len(LISTS)):
    crl = load_crl(LISTS[k])
    verdict = list_is_good(crl)
    if verdict != "OK":
        print("%-13s REJECT the list: %s" % (LISTS[k], verdict))
        continue
    print("%-13s list OK (next update %s)" % (LISTS[k], next_update(crl).date()))
    for i in range(len(certs)):
        cert = certs[i]
        # TODO 3: look the serial number up in the list:
        #         entry = crl.get_revoked_certificate_by_serial_number(cert.serial_number)
        #         entry is None: print "not revoked";
        #         else print "REVOKED on", revoked_on(entry), "reason:", reason_of(entry)
        print("    %-14s serial %#x  TODO" % (name_of(cert), cert.serial_number))
