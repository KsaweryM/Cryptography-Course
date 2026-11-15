import random

from rc4 import rc4


def xor(a, b):
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return bytes(out)


# Ready: the attacker's test for check d). You only call it.
# The attacker sees only the two packets. Does a simple trick give him m1 XOR m2?
def attacker_learns_xor(p1, p2, m1, m2):
    target = xor(m1, m2)
    n1 = p1[0:3]
    n2 = p2[0:3]
    for skip in range(4):                 # the ciphertext may start right after n, or later
        c1 = p1[3 + skip:]
        c2 = p2[3 + skip:]
        if len(c1) < len(target):
            continue
        both = xor(c1, c2)
        if both[0:len(target)] == target:
            return True
        removed = []                      # the same, with the public values XOR-ed away
        for i in range(len(target)):
            removed.append(both[i] ^ n1[i % 3] ^ n2[i % 3])
        if bytes(removed) == target:
            return True
    return False


key = b"our secret"
m1 = b"Meet at noon."
m2 = b"Bring the map"

# Step 1: the same key for two messages
# TODO 1: c1 = rc4(key, m1) and c2 = rc4(key, m2), then print:
#         xor(c1, c2) == xor(m1, m2)
#         rc4(key, m1) == rc4(key, m1)      # the same message, sent twice
#         When is this dangerous?

# Step 2: a public value, new for every message
# Step 1 showed: one key gives one keystream.
# Goal: keep ONE secret key, but get a different keystream for every message.


def encrypt(key, m):
    # TODO 2: encrypt one message with its own RC4 key.
    #   a) Make a new 3-byte value: n = random.randbytes(3)
    #      It does not have to be secret: it travels in the open.
    #   b) The RC4 key for this message is n + key
    #      (n glued in front of the secret key): c = rc4(n + key, m)
    #   c) Return the packet that is sent: n + c (first n, then the ciphertext c).
    pass


def decrypt(key, packet):
    # TODO 3: undo encrypt.
    #   a) n = the first 3 bytes of the packet, c = the rest.
    #   b) The RC4 key is again n + key: give back rc4(n + key, c).
    pass


# TODO 4: check, print four lines:
#   a) p1 = encrypt(key, m1) and p2 = encrypt(key, m2);
#      xor of the ciphertext parts (packet[3:]) == xor(m1, m2)   should be False
#   b) encrypt(key, m1) twice: are the two packets different?    should be True
#   c) decrypt(key, p1)                                          b'Meet at noon.'
#   d) attacker_learns_xor(p1, p2, m1, m2)                       should be False
#      (a ready test: the attacker sees only the packets)
# Hints: b"ab" + b"cd" == b"abcd", so n + key is n glued in front of key.
#        packet[0:3] = the first 3 bytes, packet[3:] = the rest.
