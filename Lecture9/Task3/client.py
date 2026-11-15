# Task 3: what verify=False lets in.
# Four servers say they are shop.alice.example. A client must find the real one.
import ssl
from servers import start_servers, fetch, PORTS

start_servers()

# TODO 1: the broken client, which is what verify=False does:
#         broken = ssl.create_default_context()
#         broken.check_hostname = False
#         broken.verify_mode = ssl.CERT_NONE

# TODO 2: for every port in PORTS: print the port and fetch(broken, port).

# TODO 3: the correct client: it trusts only Trusty CA and checks the name.
#         good = ssl.create_default_context(cafile="certs/trusty-ca.pem")

# TODO 4: for every port: try fetch(good, port) and print the answer;
#         except ssl.SSLCertVerificationError as e: print "refused:" and e.verify_message.
