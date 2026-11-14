# RC4 (from Lecture 1), ready to use.
#   ksa(key)    returns the table S after the key schedule
#   prga(S, n)  returns n bytes of keystream


def ksa(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def prga(S, n):
    i = 0
    j = 0
    out = bytearray(n)
    for k in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out[k] = S[(S[i] + S[j]) % 256]
    return bytes(out)


def keystream(key, n):
    return prga(ksa(key), n)
