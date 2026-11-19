"""X25519 (RFC 7748) and HKDF-SHA256 (RFC 5869) in plain Python. Ready to use: you do not need to read it."""
import hashlib
import hmac
P = 2**255 - 19
A24 = 121665


def _decode_scalar(k):
    k = bytearray(k)
    k[0] &= 248
    k[31] &= 127
    k[31] |= 64
    return int.from_bytes(k, "little")


def _decode_u(u):
    u = bytearray(u)
    u[31] &= 127
    return int.from_bytes(u, "little")


def x25519(scalar, u_bytes):
    k = _decode_scalar(scalar)
    u = _decode_u(u_bytes)
    x1, x2, z2, x3, z3, swap = u, 1, 0, u, 1, 0
    for t in reversed(range(255)):
        kt = (k >> t) & 1
        swap ^= kt
        if swap:
            x2, x3, z2, z3 = x3, x2, z3, z2
        swap = kt
        a = (x2 + z2) % P; aa = a * a % P
        b = (x2 - z2) % P; bb = b * b % P
        e = (aa - bb) % P
        c = (x3 + z3) % P; d = (x3 - z3) % P
        da = d * a % P; cb = c * b % P
        x3 = (da + cb) ** 2 % P
        z3 = x1 * (da - cb) ** 2 % P
        x2 = aa * bb % P
        z2 = e * (aa + A24 * e) % P
    if swap:
        x2, x3, z2, z3 = x3, x2, z3, z2
    return (x2 * pow(z2, P - 2, P) % P).to_bytes(32, "little")


BASE_POINT = (9).to_bytes(32, "little")


def public_key(private):
    return x25519(private, BASE_POINT)


def hkdf(secret, info, length=32, salt=b""):
    """Derives a key of the given length from a shared secret (HKDF with SHA-256)."""
    prk = hmac.new(salt or bytes(32), secret, hashlib.sha256).digest()
    okm, block, i = b"", b"", 1
    while len(okm) < length:
        block = hmac.new(prk, block + info + bytes([i]), hashlib.sha256).digest()
        okm += block
        i += 1
    return okm[:length]
