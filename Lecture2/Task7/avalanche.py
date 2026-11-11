import random

from chacha import block

random.seed(1)
TRIALS = 200

for rounds in [1, 2, 3, 4, 5, 6, 8, 12, 20]:
    total = 0
    for _ in range(TRIALS):
        key = random.randbytes(32)
        nonce = random.randbytes(12)
        counter = random.getrandbits(32)
        out1 = block(key, counter, nonce, rounds)
        out2 = block(key, counter ^ 1, nonce, rounds)   # the same, one bit of the counter changed
        # TODO: count how many of the 512 bits differ between out1 and out2
        #       and add that number to total
        #       hint: int.from_bytes(out1, "big") turns 64 bytes into one number,
        #             bin(x).count("1") counts the 1 bits of x
    print(f"{rounds:2} rounds: {total / TRIALS:6.1f} of 512 bits changed")
