import time

# Each line: a prime p, the public g, and the public value A = g^a mod p. The secret a is unknown.
PROBLEMS = [
    (49223, 4, 38043),   # p has 16 bits
    (939167, 4, 532807),   # p has 20 bits
    (10684799, 4, 3257080),   # p has 24 bits
    (187882979, 4, 180535483),   # p has 28 bits
]


def find_exponent(p, g, A):
    # TODO: try a = 1, 2, 3, ... : keep value = g^a mod p
    #       (multiply the previous value by g, mod p) until value == A, then return a
    return None


for p, g, A in PROBLEMS:
    start = time.perf_counter()
    a = find_exponent(p, g, A)
    seconds = time.perf_counter() - start
    print(f"{p.bit_length()} bits: a = {a}   {seconds:.3f} s")
