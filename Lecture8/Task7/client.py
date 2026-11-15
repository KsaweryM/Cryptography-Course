"""Task 7: log in to Bob's server with a client certificate (mutual TLS)."""
import socket
import ssl

from mtls_ready import ALICE, MALLORY, SERVER_ROOT, start_server

port = start_server()

# (who connects, the certificate and key files, or None for no certificate)
CLIENTS = [("Alice", ALICE), ("no certificate", None), ("Mallory", MALLORY)]


def log_in(cert_and_key):
    """Connects to bob.example on 127.0.0.1 and returns what the server says, or why it failed."""
    # TODO 1: a client context that trusts the root of the server: ssl.create_default_context(cafile=SERVER_ROOT)
    # TODO 2: if cert_and_key is not None, give the context our certificate and private key:
    #         context.load_cert_chain(cert_and_key[0], cert_and_key[1])
    # TODO 3: connect with socket.create_connection(("127.0.0.1", port)), then
    #         tls = context.wrap_socket(sock, server_hostname="bob.example") and read the answer: tls.recv(100).
    #         Return the answer as text (.decode()). In TLS 1.3 a rejected client often learns it only
    #         when it reads, so put both calls inside try, and on ssl.SSLError return "rejected: " + e.reason
    return "TODO"


for i in range(len(CLIENTS)):
    print("%-15s %s" % (CLIENTS[i][0], log_in(CLIENTS[i][1])))
