# RC4, ready to use: keystream(key, n) returns n bytes of keystream. You do not need to read this file.


def ksa(key):
    S = [0] * 256
    T = [0] * 256
    for i in range(256):
        S[i] = i
        T[i] = key[i % len(key)]
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def prga(S, n):
    i = j = 0
    out = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        out.append(S[t])
    return bytes(out)


def keystream(key, n):
    """Return n bytes of RC4 keystream for the given key (bytes)."""
    return prga(ksa(key), n)
