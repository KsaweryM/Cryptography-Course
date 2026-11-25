"""The parts of SHA-256 (FIPS 180-4, section 6.2) in plain Python. Ready to use: you do not need to read it.

IV                    the starting state: 8 words of 32 bits
pad(message)          the message with its padding: 0x80, zero bytes, the length in bits (8 bytes)
compress(state, blk)  the compression function: the state (8 words) and one 64-byte block in, a new state out
state_to_bytes(state) the 8 words as 32 bytes: the digest when this is the last state
sha256(message)       the whole SHA-256 of a message (bytes in, 32 bytes out), the same as hashlib.sha256

In Lecture 7 (Task 8) this file is the fair partner of bcrypt_ready.py: both are plain Python, so their
speeds can be compared. hashlib.sha256 is C code and more than 100 times faster than this file.
"""

IV = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

M32 = 0xFFFFFFFF


def _rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & M32


def pad(message):
    length_bits = len(message) * 8
    out = bytearray(message)
    out.append(0x80)
    while len(out) % 64 != 56:
        out.append(0)
    out += length_bits.to_bytes(8, "big")
    return bytes(out)


def compress(state, block):
    if len(state) != 8 or len(block) != 64:
        raise ValueError("compress needs a state of 8 words and a block of 64 bytes")
    w = [0] * 64
    for t in range(16):
        w[t] = int.from_bytes(block[4 * t:4 * t + 4], "big")
    for t in range(16, 64):
        s0 = _rotr(w[t - 15], 7) ^ _rotr(w[t - 15], 18) ^ (w[t - 15] >> 3)
        s1 = _rotr(w[t - 2], 17) ^ _rotr(w[t - 2], 19) ^ (w[t - 2] >> 10)
        w[t] = (w[t - 16] + s0 + w[t - 7] + s1) & M32
    a, b, c, d, e, f, g, h = state
    for t in range(64):
        S1 = _rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)
        ch = (e & f) ^ (~e & g)
        t1 = (h + S1 + ch + K[t] + w[t]) & M32
        S0 = _rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        t2 = (S0 + maj) & M32
        h = g
        g = f
        f = e
        e = (d + t1) & M32
        d = c
        c = b
        b = a
        a = (t1 + t2) & M32
    new = [a, b, c, d, e, f, g, h]
    for i in range(8):
        new[i] = (new[i] + state[i]) & M32
    return new


def state_to_bytes(state):
    out = bytearray()
    for i in range(8):
        out += state[i].to_bytes(4, "big")
    return bytes(out)


def sha256(message):
    padded = pad(message)
    state = list(IV)
    for off in range(0, len(padded), 64):
        state = compress(state, padded[off:off + 64])
    return state_to_bytes(state)
