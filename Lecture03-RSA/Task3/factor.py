import time

NUMBERS = [
    3215484683,  # 32 bits
    731738952551,  # 40 bits
    175092413211607,  # 48 bits
    32013612409104631,  # 55 bits
]


def smallest_factor(n):
    # TODO: try the divisors 2, 3, 5, 7, 9, ... (2, then odd numbers)
    #       until one divides n (n % f == 0), and return it.
    #       You only need to try f while f * f <= n. Why?
    return None


for n in NUMBERS:
    start = time.perf_counter()
    f = smallest_factor(n)
    seconds = time.perf_counter() - start
    if f is None:
        print(f"{n.bit_length()} bits: not done yet")
    else:
        print(f"{n.bit_length()} bits: {n} = {f} x {n // f}   {seconds:.3f} s")
