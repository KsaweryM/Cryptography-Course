# Task 6: hunt in a CT log.
# Alice owns alice-shop.example. She reads the CT log: was any certificate made for her domain behind her back?
from cryptography.hazmat.primitives import hashes
from ctlog import load_log, load_orders, dns_names, issuer_cn, issued_on, CAA_ID, ALLOWED

DOMAIN = "alice-shop.example"

log = load_log("ct_log.pem")
orders = load_orders("my_orders.txt")
print(len(log), "certificates in the log,", len(orders), "ordered by Alice, CAA allows", ALLOWED)

for i in range(len(log)):
    cert = log[i]
    names = dns_names(cert)

    # TODO 1: is it for Alice's domain? Yes if one of the names is DOMAIN or ends with "." + DOMAIN.
    #         (Careful: "alice-shop.example.mallory.example" is NOT Alice's.) If not, continue.

    # TODO 2: fp = cert.fingerprint(hashes.SHA256()).hex()
    #         If fp is in orders: print "mine:", the names and issued_on(cert), and continue.

    # TODO 3: an unknown certificate: print "UNKNOWN:", the names, issuer_cn(cert) and issued_on(cert).
    #         Then check CAA: if CAA_ID[issuer_cn(cert)] is in ALLOWED print
    #         "  CAA allowed this CA: ask it who ordered the certificate",
    #         else print "  this CA broke CAA: report it and ask the browsers to look at it".

    print("  not done yet: TODO 1 to 3", names)    # delete this line when TODO 1 to 3 are done
