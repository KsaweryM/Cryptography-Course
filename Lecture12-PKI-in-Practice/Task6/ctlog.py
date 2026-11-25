# Ready helper for Task 6: a saved piece of a Certificate Transparency log. Treat it as a black box.
#
#   load_log(path)        -> a list of the certificates in the log (oldest first)
#   load_orders(path)     -> the SHA-256 fingerprints (hex strings) of the certificates Bob ordered
#   dns_names(cert)       -> the DNS names in the certificate, e.g. ["bob.example", "www.bob.example"]
#   issuer_cn(cert)       -> the common name of the CA that issued it, e.g. "Trusty CA"
#   issued_on(cert)       -> the start of the validity period (a date)
#   CAA_ID                -> the name each CA looks for in CAA records, e.g. CAA_ID["Trusty CA"] == "trusty-ca.example"
#   ALLOWED               -> the CAA names in Bob's record (caa.txt): ["trusty-ca.example"]
#
# A real log is a public server (RFC 6962) with billions of entries; monitors such as crt.sh read it for you.
# Here it is a file with nine certificates from October and November 2026, so the task works offline.
from cryptography import x509
from cryptography.x509.oid import NameOID

CAA_ID = {"Trusty CA": "trusty-ca.example", "Shady CA": "shady-ca.example", "Green CA": "green-ca.example"}


def load_log(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificates(f.read())


def load_orders(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line != "" and not line.startswith("#"):
                out.append(line)
    return out


def _caa(path):
    out = []
    with open(path) as f:
        for line in f:
            if " issue " in line and not line.startswith(";"):
                out.append(line.split('"')[1])
    return out


ALLOWED = _caa("caa.txt")


def dns_names(cert):
    san = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
    return san.get_values_for_type(x509.DNSName)


def issuer_cn(cert):
    return cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def issued_on(cert):
    # cryptography 42+ has not_valid_before_utc; 41 only has the naive not_valid_before
    if hasattr(cert, "not_valid_before_utc"):
        return cert.not_valid_before_utc.date()
    return cert.not_valid_before.date()
