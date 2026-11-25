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
    #   san.get_values_for_type(x509.DNSName) gives a list of the DNS names.
    #   print("   SAN:         ", <the list, or "none">)
    print("   not done yet: TODO 1")      # delete this line when TODO 1 is done

    # TODO 2: is it a CA? bc = find_extension(cert, x509.BasicConstraints)
    #   print("   CA:          ", bc.ca)
    print("   not done yet: TODO 2")      # delete this line when TODO 2 is done

    # TODO 3: what may the key do? ku = find_extension(cert, x509.KeyUsage)
    #   print("   key usage:    digital_signature", ku.digital_signature, " key_cert_sign", ku.key_cert_sign)
    #   eku = find_extension(cert, x509.ExtendedKeyUsage) (None if there is none): a list of purposes (OIDs).
    #   Put oid_name(eku[k]) for each k into a list and print it: print("   ext. usage:  ", <the list, or "none">)
    print("   not done yet: TODO 3")      # delete this line when TODO 3 is done

    # TODO 4: which extensions are critical? Loop over cert.extensions (a list of ext) and put
    #   ext_name(ext) into a list for every ext with ext.critical == True.
    #   print("   critical:    ", <the list>)
    print("   not done yet: TODO 4")      # delete this line when TODO 4 is done
