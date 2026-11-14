# A tiny simulation of WEP, so the attack below runs offline, with no real network.
# WEP builds the RC4 key by gluing a public 3-byte IV in front of the secret key.
# You never see SECRET in the attack: the attacker only gets the packets.
import random
from rc4 import keystream


def xor(a, b):
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return bytes(out)


def wep_encrypt(iv, secret, plaintext):
    ks = keystream(iv + secret, len(plaintext))
    return iv + xor(plaintext, ks)          # a packet = IV, then the ciphertext


SECRET = bytes([0x1F, 0x8A, 0x3C, 0x77, 0xD2])   # the Wi-Fi key, hidden from the attacker
SNAP = bytes([0xAA, 0xAA, 0x03, 0x00])           # every data packet starts with this header


def capture(seed=1, n=6000):
    """Return a list of captured packets, the index of one packet whose
    plaintext we happen to know, and that known plaintext."""
    rng = random.Random(seed)
    packets = []

    # A status packet the printer broadcasts in the clear language everybody knows.
    known_iv = bytes([0x9C, 0x03, 0x7E])
    known_plaintext = SNAP + b"status: the printer is online and ready"
    packets.append(wep_encrypt(known_iv, SECRET, known_plaintext))

    # Somewhere later, the router happens to pick the SAME IV again (3 bytes repeat fast).
    secret_message = SNAP + b"the door code is 2580"
    reuse_at = rng.randrange(1000, n)

    for k in range(1, n):
        if k == reuse_at:
            packets.append(wep_encrypt(known_iv, SECRET, secret_message))
        else:
            iv = bytes([rng.randrange(256), rng.randrange(256), rng.randrange(256)])
            while iv == known_iv:
                iv = bytes([rng.randrange(256), rng.randrange(256), rng.randrange(256)])
            msg = SNAP + b"routine traffic " + bytes([rng.randrange(65, 91)])
            packets.append(wep_encrypt(iv, SECRET, msg))

    return packets, 0, known_plaintext
