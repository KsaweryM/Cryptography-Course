# Bob. Treat this file as a black box: the task is to solve it without reading the key.

_KEY = b'hidden server key'


def _keystream(n):
    S = [0] * 256
    for i in range(256):
        S[i] = i
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
    z = _keystream(len(ciphertext))
    plaintext = bytearray(len(ciphertext))
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ z[i]
    digits = len(plaintext) == 8
    for i in range(len(plaintext)):
        if plaintext[i] < 0x30 or plaintext[i] > 0x39:
            digits = False
    if digits:
        print(f"Invoice accepted: {int(plaintext)} PLN")
    else:
        print("Rejected: the message is not 8 digits")
