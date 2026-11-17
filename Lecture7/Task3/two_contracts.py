# Task 3: two contracts, one fingerprint.
# The notary Carol keeps only a 32-bit fingerprint of every contract she sees.
# Mallory wants a fair and an unfair contract with the same fingerprint.
import hashlib
from contracts import FAIR, UNFAIR, FAIR_BITS, UNFAIR_BITS, variant, fingerprint

# TODO 1: make a table of the fair variants: for number in range(2 ** FAIR_BITS):
#         table[fingerprint(variant(FAIR, number))] = number
table = {}

# TODO 2: try the unfair variants one by one: for number in range(2 ** UNFAIR_BITS):
#         if fingerprint(variant(UNFAIR, number)) is a key in table, stop (break):
#         keep fair_number = table[...] and unfair_number = number, and count the unfair tries
fair_number = None
unfair_number = None
unfair_tries = 0

if fair_number is None:
    print("not done yet: TODO 1 and 2")
else:
    a = variant(FAIR, fair_number)
    b = variant(UNFAIR, unfair_number)
    print(f"fair variant {fair_number} and unfair variant {unfair_number}, after {unfair_tries} unfair tries")
    print(a.decode())
    print(b.decode())
    # TODO 3: print the fingerprint of a and of b (in hex: f"{fingerprint(a):08x}"),
    #         then the full SHA-256 of a and of b (hashlib.sha256(a).hexdigest())
    print("not done yet: TODO 3")
