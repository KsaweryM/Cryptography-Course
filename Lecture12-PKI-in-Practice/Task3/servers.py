# Ready helper for Task 3: four TLS servers on this computer (127.0.0.1). Treat it as a black box.
#
#   start_servers()        starts the four servers in the background (threads)
#   PORTS                  their port numbers: 8443, 8444, 8445, 8446
#   fetch(context, port)   connects to 127.0.0.1:port with the ssl.SSLContext you give,
#                          asks for the page of shop.bob.example and returns the answer (str).
#                          If the certificate check fails, it raises ssl.SSLCertVerificationError.
#
# Every server says it is shop.bob.example. Only the first one really is:
#   8443  the real shop: a certificate for shop.bob.example from Trusty CA
#   8444  Mallory: a self-signed certificate that says shop.bob.example
#   8445  Mallory: a real Trusty CA certificate, but for her own name mallory.example
#   8446  an old copy of the shop: a certificate from Trusty CA that expired on 2025-08-20
import socket
import ssl
import threading
import time

HOST = "shop.bob.example"
PORTS = [8443, 8444, 8445, 8446]
_FILES = ["certs/shop", "certs/mallory-selfsigned", "certs/mallory-own-name", "certs/shop-expired"]
_ANSWERS = ["[the real shop] Welcome to Bob's shop. Please log in.",
            "[Mallory, self-signed] Welcome to Bob's shop. Please log in.",
            "[Mallory, her own name] Welcome to Bob's shop. Please log in.",
            "[an expired copy] Welcome to Bob's shop. Please log in."]


def _serve(port, files, answer):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(files + ".pem", files + ".key")
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(5)
    while True:
        conn, _ = srv.accept()
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                tls.recv(100)
                tls.sendall(answer.encode())
        except (ssl.SSLError, OSError):
            pass        # the client refused our certificate


def start_servers():
    for i in range(len(PORTS)):
        t = threading.Thread(target=_serve, args=(PORTS[i], _FILES[i], _ANSWERS[i]), daemon=True)
        t.start()
    time.sleep(0.3)


def fetch(context, port):
    with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
        with context.wrap_socket(raw, server_hostname=HOST) as tls:
            tls.sendall(b"GET / HTTP/1.0\r\nHost: " + HOST.encode() + b"\r\n\r\n")
            return tls.recv(200).decode()
