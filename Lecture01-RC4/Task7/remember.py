import random

from rc4 import ksa

N = 10_000
ksa_hits = 0
shuffle_hits = 0

for _ in range(N):
    key = random.randbytes(16)   # random is fine for a measurement (never for real keys)
    # TODO 1: S = ksa(key). Add 1 to ksa_hits if S[0] == key[0].

    # TODO 2: S = a fair random shuffle of the numbers 0 to 255.
    #         Add 1 to shuffle_hits if S[0] == key[0].
    # Hint: random.shuffle(S) shuffles the list S in place.
    pass

if ksa_hits == 0:
    print("not done yet: TODO 1")
elif shuffle_hits == 0:
    print("not done yet: TODO 2")
else:
    print(f"KSA:     {100 * ksa_hits / N:.2f}%")
    print(f"shuffle: {100 * shuffle_hits / N:.2f}%")
