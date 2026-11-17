"""Textbook RSA in plain Python. Ready to use: you do not need to read it."""
import random


def is_probable_prime(n, rounds=40):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(bits):
    while True:
        c = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(c):
            return c


def generate_keys(bits=2048, e=65537):
    """Returns (public_key, private_key) = ((e, n), (d, n))."""
    while True:
        p, q = random_prime(bits // 2), random_prime(bits // 2)
        phi = (p - 1) * (q - 1)
        if p != q and phi % e != 0:
            n = p * q
            return (e, n), (pow(e, -1, phi), n)


def text_to_number(text):
    return int.from_bytes(text.encode(), "big")


def number_to_text(number):
    return number.to_bytes((number.bit_length() + 7) // 8, "big").decode(errors="replace")


def encrypt(message, public_key):
    """Encrypts a short text with the public key (e, n). Returns a number."""
    e, n = public_key
    m = text_to_number(message)
    assert m < n, "message too long for this key"
    return pow(m, e, n)


def decrypt(ciphertext, private_key):
    """Decrypts a number with the private key (d, n). Returns the text."""
    d, n = private_key
    return number_to_text(pow(ciphertext, d, n))
