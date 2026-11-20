"""Makes the keys and ciphertexts of Tasks 7 and 8 of Lecture 3 (and the small keys of the RSA simulator, step 6).

Fixed seeds, so a new run gives the same numbers. If you change a seed, fix the task files, the READMEs,
the figures (task-figures/task7.tex, task8.tex) and the slides "Task 7/8: what we saw".
Run: python3 checks/make_task_keys.py
"""
import random


def is_probable_prime(n, rng):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(40):
        a = rng.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(bits, rng):
    while True:
        x = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(x, rng):
            return x


def make_key(rng, bits=2048, e=65537, p=None):
    while True:
        if p is None:
            pp = random_prime(bits // 2, rng)
        else:
            pp = p
        q = random_prime(bits // 2, rng)
        n = pp * q
        phi = (pp - 1) * (q - 1)
        if pp != q and n.bit_length() == bits and phi % e != 0:
            return pp, q, n, pow(e, -1, phi)


def show(name, x):
    print(name, "=", x)


rng = random.Random(20261119)
# Task 7: the bank's key; Alice transfers 100
p, q, n, d = make_key(rng)
amount = 100
show("T7_n", n); show("T7_d", d); show("T7_C", pow(amount, 65537, n))

# Task 8: two routers with a weak random generator: the same p
rng = random.Random(20261120)
p, q1, n1, d1 = make_key(rng)
_, q2, n2, d2 = make_key(rng, p=p)
msg = b"router 1 admin password: blue-otter-42"
show("T8_n1", n1); show("T8_n2", n2)
show("T8_C", pow(int.from_bytes(msg, "big"), 65537, n1))
show("T8_p", p)
