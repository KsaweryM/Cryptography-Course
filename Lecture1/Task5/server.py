# Party B. Treat this file as a black box: the task is to solve it without reading the key.

_KEY = b'hidden server key'


def _keystream(n):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + _KEY[i % len(_KEY)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(S[(S[i] + S[j]) % 256])
    return out


def receive(ciphertext):
    plaintext = bytes(c ^ z for c, z in zip(ciphertext, _keystream(len(ciphertext))))
    if len(plaintext) == 8 and all(0x30 <= b <= 0x39 for b in plaintext):
        print(f"Invoice accepted: {int(plaintext)} PLN")
    else:
        print("Rejected: the message is not 8 digits")
