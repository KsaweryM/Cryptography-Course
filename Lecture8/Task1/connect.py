"""Task 1: connect to six servers that all claim to be bob.example. Which ones does Python trust?"""
import socket
import ssl

from servers import start_servers, ROOT_CA

servers = start_servers()     # a list of (name, port), all on 127.0.0.1

# TODO 1: make a TLS client context that trusts only our root CA:
#         context = ssl.create_default_context(cafile=ROOT_CA)
context = None

for i in range(len(servers)):
    label = servers[i][0]
    port = servers[i][1]
    sock = socket.create_connection(("127.0.0.1", port))
    # TODO 2: start TLS on sock and check the certificate for the name "bob.example":
    #         tls = context.wrap_socket(sock, server_hostname="bob.example")
    #         if it works, print the name of the server, "OK" and tls.version(), then tls.close()
    # TODO 3: if the certificate is rejected, wrap_socket raises ssl.SSLCertVerificationError.
    #         Catch it and print the name of the server and e.verify_message, then sock.close()
    print("%-16s TODO" % label)
    sock.close()
