# Task 4: which certificate fits?
# Four certificates from Trusty CA. Read their extensions and decide what each one may be used for.
from cryptography import x509
from cert_tools import load_cert, find_extension, ext_name, oid_name

files = ["cert_A.pem", "cert_B.pem", "cert_C.pem", "cert_D.pem"]

for i in range(len(files)):
    cert = load_cert(files[i])
    print("==", files[i], " subject:", cert.subject.rfc4514_string())

    # TODO 1: the names in the Subject Alternative Name.
    #   san = find_extension(cert, x509.SubjectAlternativeName)   (None if there is none)
    #   san.get_values_for_type(x509.DNSName) gives a list of the DNS names. Print it, or "none".

    # TODO 2: is it a CA? bc = find_extension(cert, x509.BasicConstraints); print bc.ca.

    # TODO 3: what may the key do? ku = find_extension(cert, x509.KeyUsage);
    #   print ku.digital_signature and ku.key_cert_sign.
    #   eku = find_extension(cert, x509.ExtendedKeyUsage) (None if there is none):
    #   a list of purposes (OIDs); print oid_name(eku[k]) for each k

    # TODO 4: which extensions are critical? Loop over cert.extensions (a list of ext)
    #   and print ext_name(ext) for every ext with ext.critical == True.
