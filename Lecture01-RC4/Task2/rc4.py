# RC4, ready to use.
# For now, treat this file as a black box: you only need keystream(key, n).
# Later in the lecture we open this box and go through every line.


def ksa(key):
    S = list(range(256))
    T = [key[i % len(key)] for i in range(256)]
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
