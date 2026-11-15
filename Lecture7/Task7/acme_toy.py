# A toy ACME certificate authority and a tiny web server for Task 7. Treat it as a black box.
#
# Simplified: real ACME (RFC 8555) sends every request to the CA over HTTPS as JSON signed with the
# account key (JWS). Here the requests are plain Python calls. The http-01 challenge itself is real:
# the CA downloads http://<domain>/.well-known/acme-challenge/<token> and compares the text with
# the key authorization  token + "." + thumbprint(account key).
#
#   thumbprint(account_key)    the JWK thumbprint of the public account key (RFC 7638), base64url
#   start_web_server(folder)   serves the files of `folder` on 127.0.0.1 (a free port); returns the port
#   ca = ToyCA(dns)            a CA "Toy ACME CA R1"; dns says which port answers for which domain
#   order = ca.new_order(domain, account_key)    order.token is the token of the http-01 challenge
#   ca.validate(order)         downloads the challenge file and returns "valid" or "invalid"
#   ca.finalize(order, csr)    a 90-day certificate for a valid order (None otherwise)

import base64
import datetime
import functools
import hashlib
import http.server
import os
import secrets
import threading
import urllib.request

from cert_ready import make_cert, new_key, dns_names_of


def _b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def thumbprint(account_key):
    numbers = account_key.public_key().public_numbers()
    x = _b64url(numbers.x.to_bytes(32, "big"))
    y = _b64url(numbers.y.to_bytes(32, "big"))
    jwk = '{"crv":"P-256","kty":"EC","x":"' + x + '","y":"' + y + '"}'   # RFC 7638: sorted, no spaces
    return _b64url(hashlib.sha256(jwk.encode()).digest())


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if len(args) >= 2:
            print("   [web server] GET", self.path, "->", args[1])

    def log_error(self, fmt, *args):
        pass


def start_web_server(folder):
    os.makedirs(folder, exist_ok=True)
    handler = functools.partial(_Quiet, directory=folder)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server.server_address[1]


class Order:
    def __init__(self, domain, account_key):
        self.domain = domain
        self.account_key = account_key
        self.token = secrets.token_urlsafe(32)
        self.status = "pending"


class ToyCA:
    def __init__(self, dns):
        self.dns = dns
        self.root_key = new_key()
        self.root = make_cert("Toy ACME Root", self.root_key, None, None, ca=True, path_len=0, days=3650)
        self.key = new_key()
        self.cert = make_cert("Toy ACME CA R1", self.key, self.root, self.root_key, ca=True,
                              path_len=0, days=1825)

    def new_order(self, domain, account_key):
        return Order(domain, account_key)

    def validate(self, order):
        if order.domain not in self.dns:
            order.status = "invalid"
            return "invalid: no web server answers for " + order.domain
        url = ("http://127.0.0.1:" + str(self.dns[order.domain]) +
               "/.well-known/acme-challenge/" + order.token)
        print("   [CA] downloads http://" + order.domain + "/.well-known/acme-challenge/" + order.token)
        expected = order.token + "." + thumbprint(order.account_key)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            got = opener.open(url, timeout=5).read().decode().rstrip()
        except Exception as e:
            order.status = "invalid"
            return "invalid: " + str(e) + " (an invalid order stays invalid: ask for a new one)"
        if got != expected:
            order.status = "invalid"
            return "invalid: the file says " + repr(got)
        order.status = "valid"
        return "valid"

    def finalize(self, order, csr):
        if order.status != "valid":
            print("   [CA] refuses: the order is", order.status)
            return None
        if not csr.is_signature_valid:
            print("   [CA] refuses: the signature of the CSR is wrong")
            return None
        if dns_names_of(csr) != [order.domain]:
            print("   [CA] refuses: the CSR asks for", dns_names_of(csr), "not", [order.domain])
            return None
        return make_cert(order.domain, None, self.cert, self.key, ca=False, days=90,
                         dns_names=[order.domain], public_key=csr.public_key())
