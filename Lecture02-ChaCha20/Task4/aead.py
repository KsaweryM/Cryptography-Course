# ChaCha20-Poly1305 (RFC 8439) in plain Python, ready to use.
# Treat this file as a black box: you only need two functions.
#   seal(key, nonce, plaintext)  returns the packet: ciphertext + a 16-byte tag
#   open_(key, nonce, packet)    checks the tag and returns the plaintext,
#                                or raises ValueError if the packet was changed
# Both take an optional aad: associated data (a header), not encrypted but protected by the tag.
# (open_ has a "_" at the end because open is already a Python function.)

import hmac

MASK = 0xFFFFFFFF   # keeps 32 bits


# ---------- ChaCha20: the same code as chacha.py ----------

def add32(a, b):
    return (a + b) & MASK


def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def quarter_round(s, a, b, c, d):
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 16)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 12)
    s[a] = add32(s[a], s[b]); s[d] ^= s[a]; s[d] = rotl32(s[d], 8)
    s[c] = add32(s[c], s[d]); s[b] ^= s[c]; s[b] = rotl32(s[b], 7)


def word(data, i):
    return int.from_bytes(data[4 * i:4 * i + 4], "little")


def initial_state(key, counter, nonce):
    s = [0x61707865, 0x3320646E, 0x79622D32, 0x6B206574]
    for i in range(8):
        s.append(word(key, i))
    s.append(counter)
    for i in range(3):
        s.append(word(nonce, i))
    return s


def block(key, counter, nonce):
    start = initial_state(key, counter, nonce)
    s = list(start)
    for r in range(10):
        quarter_round(s, 0, 4, 8, 12)
        quarter_round(s, 1, 5, 9, 13)
        quarter_round(s, 2, 6, 10, 14)
        quarter_round(s, 3, 7, 11, 15)
        quarter_round(s, 0, 5, 10, 15)
        quarter_round(s, 1, 6, 11, 12)
        quarter_round(s, 2, 7, 8, 13)
        quarter_round(s, 3, 4, 9, 14)
    out = b""
    for i in range(16):
        out += add32(s[i], start[i]).to_bytes(4, "little")
    return out


def chacha20(key, nonce, counter, data):
    out = bytearray(len(data))
    for i in range(len(data)):
        if i % 64 == 0:
            ks = block(key, counter + i // 64, nonce)
        out[i] = data[i] ^ ks[i % 64]
    return bytes(out)


# ---------- Poly1305: a 16-byte tag ----------

def poly1305(key, msg):
    r = int.from_bytes(key[0:16], "little") & 0x0FFFFFFC0FFFFFFC0FFFFFFC0FFFFFFF
    s = int.from_bytes(key[16:32], "little")
    p = (1 << 130) - 5
    acc = 0
    for i in range(0, len(msg), 16):
        n = int.from_bytes(msg[i:i + 16] + b"\x01", "little")
        acc = (acc + n) * r % p
    return ((acc + s) & ((1 << 128) - 1)).to_bytes(16, "little")


def pad16(x):
    # zero bytes up to a multiple of 16
    return bytes((16 - len(x) % 16) % 16)


def make_tag(key, nonce, ciphertext, aad):
    one_time_key = block(key, 0, nonce)[0:32]        # block 0 gives the Poly1305 key
    mac_data = (aad + pad16(aad) + ciphertext + pad16(ciphertext)
                + len(aad).to_bytes(8, "little") + len(ciphertext).to_bytes(8, "little"))
    return poly1305(one_time_key, mac_data)


def seal(key, nonce, plaintext, aad=b""):
    ciphertext = chacha20(key, nonce, 1, plaintext)  # the data starts at block 1
    return ciphertext + make_tag(key, nonce, ciphertext, aad)


def open_(key, nonce, packet, aad=b""):
    ciphertext = packet[:-16]
    tag = packet[-16:]
    # compare_digest takes the same time wherever the tags differ (a plain != stops at the first
    # different byte, and the time could tell Mallory how many bytes of her tag are right)
    if not hmac.compare_digest(make_tag(key, nonce, ciphertext, aad), tag):
        raise ValueError("bad tag: message rejected")
    return chacha20(key, nonce, 1, ciphertext)
