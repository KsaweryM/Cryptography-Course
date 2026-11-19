# Task 8: what the cost costs.
# Part 1: how the time of one bcrypt grows with the cost.
# Part 2: Mallory stole Dave's bcrypt text (cost 4) and tries the 20 most common passwords.
import hashlib
import time
from bcrypt_ready import hash_password, check_password


def load_lines(path):
    """Ready: the lines of a text file without the ones that start with #."""
    out = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if line != "" and not line.startswith("#"):
                out.append(line)
    return out


# TODO 1: for cost in 4, 5, 6, 7: measure one hash_password("test password", cost)
#         (start = time.perf_counter() before, seconds = time.perf_counter() - start after)
#         and print(f"cost {cost}: {seconds:.2f} s")
print("not done yet: TODO 1")

stored = load_lines("stolen_bcrypt.txt")[0]
guesses = load_lines("top20.txt")
print("stolen:", stored)

# TODO 2: try the guesses in order with check_password(guess, stored). Count the tries.
#         When one matches, print f"found after {tries} tries: {guess}" and stop (break).
#         Measure the whole loop and print f"bcrypt cost 4: {tries / seconds:.1f} guesses per second"
print("not done yet: TODO 2")

# TODO 3: for comparison, measure SHA-256 on the same guesses: compute
#         hashlib.sha256(guesses[i].encode()).hexdigest() for all 20 guesses, 10000 times over (200000 hashes),
#         and print f"SHA-256: {200000 / seconds:.0f} guesses per second"
print("not done yet: TODO 3")
