# Task 7: two real certificates
# coventry.pem and bbc.pem were saved from www.coventry.ac.uk and www.bbc.co.uk on 15 November 2026
# (openssl s_client, see the README). cert_D.pem is Dave's certificate from Task 4, with a *. No internet needed.
from cryptography import x509
from cert_tools import load_cert, valid_from, valid_until, find_extension, key_name, oid_name


def matches(pattern, host):
    # TODO 3: True if one SAN name (pattern) fits host.
    #   pattern == host: True.
    #   pattern starts with "*." (a wildcard): the * stands for exactly one label, the left-most one.
    #     rest = pattern[1:]  (for "*.dave.example" it is ".dave.example")
    #     dot = host.find(".")  (the index of the first dot of host, -1 if none, like strchr in C)
    #     True if dot > 0 and host[dot:] == rest.
    #   Otherwise False.
    return None


def covers(cert, host):
    # TODO 4: True if one of the DNS names in the Subject Alternative Name of cert matches host.
    #   san = find_extension(cert, x509.SubjectAlternativeName)
    #   names = san.get_values_for_type(x509.DNSName); loop over names with an index and use matches().
    return None


files = ["coventry.pem", "bbc.pem", "cert_D.pem"]
for i in range(len(files)):
    cert = load_cert(files[i])
    print("==", files[i])

    # TODO 1: print the subject and the issuer (.rfc4514_string()):
    #   print("   subject:  ", ...)   print("   issuer:   ", ...)
    print("   not done yet: TODO 1")      # delete this line when TODO 1 is done

    # TODO 2: how many days is it valid? (valid_until(cert) - valid_from(cert)).days
    #   print("   days:     ", ...)
    print("   not done yet: TODO 2")      # delete this line when TODO 2 is done

    print("   key:      ", key_name(cert.public_key()))
    print("   signature:", oid_name(cert.signature_algorithm_oid))

    # TODO 5: print how many DNS names the SAN has (len(names)), and the first three of them
    #   (names[0:3]): print("   SAN names:", len(names), names[0:3])
    print("   not done yet: TODO 5")      # delete this line when TODO 5 is done

if matches("*.carol.example", "www.carol.example") is None:
    print("not done yet: TODO 3")
else:
    print("test: *.carol.example fits www.carol.example:", matches("*.carol.example", "www.carol.example"),
          "(should be True)")

# TODO 6: which of these names does each certificate cover? For every host print one line:
#   the host, then for every file "coventry.pem: True" and so on, using covers().
hosts = ["www.coventry.ac.uk", "coventry.ac.uk", "www.bbc.co.uk", "news.bbc.co.uk", "sport.bbc.co.uk",
         "play.dave.example", "dave.example", "x.play.dave.example"]
if covers(load_cert(files[0]), hosts[0]) is None:
    print("not done yet: TODO 4")
print("not done yet: TODO 6")      # delete this line when TODO 6 is done
