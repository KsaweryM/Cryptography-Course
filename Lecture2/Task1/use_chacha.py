# Task 1: use ChaCha20.
# chacha.py is ready: chacha20(key, nonce, counter, data). The data is from RFC 8439, section 2.4.2.
from chacha import chacha20

key   = bytes(range(32))
nonce = bytes.fromhex("000000000000004a00000000")
ciphertext = bytes.fromhex(
    "6e2e359a2568f98041ba0728dd0d6981e97e7aec1d4360c2"
    "0a27afccfd9fae0bf91b65c5524733ab8f593dabcd62b357"
    "1639d624e65152ab8f530c359f0861d807ca0dbf500d6a61"
    "56a38e088a22b65e52bc514d16ccf806818ce91ab7793736"
    "5af90bbf74a35be6b40b8eedf2785e42874d"
)

# TODO 1: decrypt the ciphertext with counter 1

# TODO 2: print the message
