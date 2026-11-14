# The same offline WEP simulation as example 1, but the captured packets all use
# "weak IVs" of the form (A+3, 255, X). Those IVs let the attack below guess one
# secret key byte at a time. SECRET is never used by the attack.
import random
from rc4 import keystream


def xor(a, b):
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return bytes(out)


def wep_encrypt(iv, secret, plaintext):
    ks = keystream(iv + secret, len(plaintext))
    return iv + xor(plaintext, ks)


SECRET = bytes([0x1F, 0x8A, 0x3C, 0x77, 0xD2])   # the Wi-Fi key, hidden from the attacker
SNAP0 = 0xAA                                     # the first plaintext byte of every packet


def capture(seed=2, per_byte=3000):
    """Return captured packets that use weak IVs (A+3, 255, X) for every key
    byte position A."""
    rng = random.Random(seed)
    packets = []
    for A in range(len(SECRET)):
        for _ in range(per_byte):
            x = rng.randrange(256)
            iv = bytes([A + 3, 255, x])
            plain = [SNAP0]
            for _ in range(8):
                plain.append(rng.randrange(256))
            packets.append(wep_encrypt(iv, SECRET, bytes(plain)))
    rng.shuffle(packets)
    return packets
