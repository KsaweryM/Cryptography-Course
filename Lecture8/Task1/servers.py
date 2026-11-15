"""Six TLS servers on this computer (127.0.0.1) for Task 1. Ready: you do not need to change it.

Each server pretends to be bob.example and sends its own certificate file from certs/:
    good             the leaf of bob.example and the intermediate, both from the Trusty CA
    expired          the same, but the leaf ended on 1 October 2026
    wrong_name       a good certificate, but for carol.example
    unknown_ca       a certificate for bob.example from "Mallory Root CA"
    self_signed      a certificate for bob.example signed with its own key
    no_intermediate  the good leaf, but the server forgot to send the intermediate
"""
import os
import socket
import ssl
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
CERTS = os.path.join(HERE, "certs")

# the trust store of this task: only the Trusty Root CA
ROOT_CA = os.path.join(CERTS, "root.pem")

NAMES = ["good", "expired", "wrong_name", "unknown_ca", "self_signed", "no_intermediate"]


def _serve(listener, context):
    while True:
        conn, _ = listener.accept()
        try:
            tls = context.wrap_socket(conn, server_side=True)
            tls.sendall(b"hello from the server\n")
            tls.close()
        except (ssl.SSLError, OSError):
            conn.close()      # the client rejected our certificate


def start_servers():
    """Starts the six servers. Returns a list of (name, port)."""
    servers = []
    for i in range(len(NAMES)):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(os.path.join(CERTS, NAMES[i] + ".pem"), os.path.join(CERTS, NAMES[i] + ".key"))
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))       # any free port
        listener.listen()
        threading.Thread(target=_serve, args=(listener, context), daemon=True).start()
        servers.append((NAMES[i], listener.getsockname()[1]))
    return servers
