# Task 7: two real certificates
# coventry.pem and bbc.pem were saved from www.coventry.ac.uk and www.bbc.co.uk on 15 November 2026
# (openssl s_client, see the README). No internet needed.
from cryptography import x509
from cert_tools import load_cert, valid_from, valid_until, find_extension, key_name, oid_name


def covers(cert, host):
    # TODO 3: True if host is one of the DNS names in the Subject Alternative Name of cert.
    #   san = find_extension(cert, x509.SubjectAlternativeName)
    #   names = san.get_values_for_type(x509.DNSName); loop over names and compare with ==.
    return False


files = ["coventry.pem", "bbc.pem"]
for i in range(len(files)):
    cert = load_cert(files[i])
    print("==", files[i])

    # TODO 1: print the subject and the issuer (.rfc4514_string()).

    # TODO 2: how many days is it valid? (valid_until(cert) - valid_from(cert)).days

    print("   key:      ", key_name(cert.public_key()))
    print("   signature:", oid_name(cert.signature_algorithm_oid))

    # TODO 4: print how many DNS names the SAN has (len(names)), and the first three of them.

# TODO 5: which of these names does each certificate cover? Use covers() for every pair.
hosts = ["www.coventry.ac.uk", "coventry.ac.uk", "www.bbc.co.uk", "news.bbc.co.uk", "sport.bbc.co.uk"]
