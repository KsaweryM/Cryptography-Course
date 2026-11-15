"""Ready parts of Task 7: Bob's server that asks every client for a certificate. Do not change this file.

The server is bob.example on 127.0.0.1. Its own certificate comes from the Trusty CA.
It accepts only clients whose certificate was issued by "Bob Staff CA", Bob's private CA for his staff,
and greets the client by the name in the certificate.
"""
import os
import socket
import ssl
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
CERTS = os.path.join(HERE, "certs")

SERVER_ROOT = os.path.join(CERTS, "server_root.pem")       # the root the client trusts for the server
ALICE = (os.path.join(CERTS, "alice.pem"), os.path.join(CERTS, "alice.key"))
MALLORY = (os.path.join(CERTS, "mallory.pem"), os.path.join(CERTS, "mallory.key"))


def _serve(listener, context):
    while True:
        conn, _ = listener.accept()
        try:
            tls = context.wrap_socket(conn, server_side=True)
            subject = tls.getpeercert()["subject"]
            name = "?"
            for i in range(len(subject)):
                if subject[i][0][0] == "commonName":
                    name = subject[i][0][1]
            tls.sendall(("hello, %s: you are logged in" % name).encode())
            tls.close()
        except (ssl.SSLError, OSError):
            conn.close()


def start_server():
    """Starts Bob's server in the background. Returns its port on 127.0.0.1."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(os.path.join(CERTS, "server.pem"), os.path.join(CERTS, "server.key"))
    context.verify_mode = ssl.CERT_REQUIRED                           # ask for a client certificate
    context.load_verify_locations(os.path.join(CERTS, "staff_ca.pem"))  # trust only Bob Staff CA for clients
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen()
    threading.Thread(target=_serve, args=(listener, context), daemon=True).start()
    return listener.getsockname()[1]
