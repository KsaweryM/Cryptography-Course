"""Task 3: check six certificate chains yourself. Each case breaks at most one rule."""
from certs_ready import (NOW, load_chain, load_store, name_of, signed_by, valid_from, valid_until,
                         dns_names, is_ca, key_purposes)

# (the file the server sent, the name Alice typed)
CASES = [
    ("case1.pem", "bob.example"),
    ("case2.pem", "bob.example"),
    ("case3.pem", "bob.example"),
    ("case4.pem", "bob.example"),
    ("case5.pem", "bob.example"),
    ("case6.pem", "bob.example"),
]


def name_matches(pattern, host):
    """True if a DNS name from the certificate (pattern) covers the host name."""
    # TODO 3a: return True if pattern and host are equal, ignoring upper and lower case (.lower()).
    #          A wildcard "*.bob.example" covers exactly ONE more label in front of ".bob.example":
    #          "www.bob.example" yes, "bob.example" no, "a.b.bob.example" no.
    return False


def check(chain, store, host):
    """chain[0] is the leaf. Returns "OK", or which check failed and on which certificate."""
    n = len(chain)

    # TODO 1: signatures. For every i from 0 to n - 2: chain[i] must be signed_by chain[i + 1],
    #         else return "check 1: certificate %d is not signed by certificate %d" % (i, i + 1).
    #         The last one, chain[n - 1], must be signed by a root in store (the trust anchor),
    #         else return "check 1: certificate %d is not signed by a trusted root" % (n - 1)

    # TODO 2: dates. Every certificate: valid_from(c) <= NOW <= valid_until(c),
    #         else return "check 2: certificate %d is not valid now (until %s)" % (i, valid_until(c).date())

    # TODO 3b: the name. host must match at least one of dns_names(chain[0]) (use name_matches),
    #          else return "check 3: %s is not in %s" % (host, dns_names(chain[0]))

    # TODO 4: Basic Constraints. Every certificate except the leaf must be a CA (is_ca),
    #         else return "check 4: certificate %d (%s) is not a CA" % (i, name_of(chain[i]))

    # TODO 5: Extended Key Usage. "serverAuth" must be in key_purposes(chain[0]),
    #         else return "check 5: the leaf is for %s, not for a server" % key_purposes(chain[0])

    # TODO 6: every check passed: return "OK" in place of the line below
    return "not done yet: TODO 1"


store = load_store()
for k in range(len(CASES)):
    chain = load_chain(CASES[k][0])
    print("%s  %d certificates  %s" % (CASES[k][0], len(chain), check(chain, store, CASES[k][1])))
