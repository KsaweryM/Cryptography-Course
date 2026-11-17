import time

# Each line: a prime p, the public g, and the public value A = g^a mod p. The secret a is unknown.
PROBLEMS = [
    (49223, 4, 38043),   # p has 16 bits
    (939167, 4, 532807),   # p has 20 bits
    (10684799, 4, 3257080),   # p has 24 bits
    (187882979, 4, 180535483),   # p has 28 bits
]


def find_exponent(p, g, A):
    # TODO 1: try a = 1, 2, 3, ... : keep value = g^a mod p
    #         (multiply the previous value by g, mod p) until value == A, then return a
    return None


a = None
seconds = 0.0
for i in range(len(PROBLEMS)):
    p = PROBLEMS[i][0]
    g = PROBLEMS[i][1]
    A = PROBLEMS[i][2]
    start = time.perf_counter()
    a = find_exponent(p, g, A)
    seconds = time.perf_counter() - start
    if a is None:
        print(f"{p.bit_length()} bits: not done yet: TODO 1")
    else:
        print(f"{p.bit_length()} bits: a = {a}   {seconds:.3f} s")

# Here a and seconds are from the last problem: p of 28 bits.
# TODO 2: your speed: tries_per_second = a / seconds (you tried a values of a).
#         A real secret a has 256 bits: trying them all is about 2^256 tries (2**256 in Python).
#         How many years would that take at your speed? (one year = 365 * 24 * 3600 seconds)
#         print(f"{tries_per_second:.0f} tries per second, a of 256 bits: about {years:.1e} years")
print("not done yet: TODO 2")
