# Ready module for Task 3: the two contracts and their variants. You do not need to change this file.
#
#   FAIR, UNFAIR           the lines of the two contracts (they differ only in the price)
#   variant(lines, number) the contract as bytes, with one or two spaces between words:
#                          bit k of number (k = 0, 1, 2, ...) says if the k-th gap gets two spaces.
#                          A reader does not notice the extra spaces, but the bytes (and the hash) change.
#   FAIR_BITS = 16         Mallory makes 2^16 fair variants: numbers 0 to 65535
#   UNFAIR_BITS = 24       and up to 2^24 unfair ones
#   fingerprint(data)      the notary's fingerprint: the first 32 bits of SHA-256(data), as a whole number
import hashlib

FAIR = ["Contract",
        "Mallory sells her bike to Alice.",
        "The price is 100 pounds.",
        "Alice pays on 1 March.",
        "Mallory gives the bike to Alice on the same day.",
        "Signed: Alice, Mallory"]
UNFAIR = ["Contract",
          "Mallory sells her bike to Alice.",
          "The price is 1000 pounds.",
          "Alice pays on 1 March.",
          "Mallory gives the bike to Alice on the same day.",
          "Signed: Alice, Mallory"]
FAIR_BITS = 16
UNFAIR_BITS = 24


def variant(lines, number):
    out = ""
    k = 0   # the number of the gap between two words
    for li in range(len(lines)):
        words = lines[li].split(" ")
        for wi in range(len(words)):
            out = out + words[wi]
            if wi < len(words) - 1:
                if (number >> k) & 1 == 1:
                    out = out + "  "
                else:
                    out = out + " "
                k = k + 1
        out = out + "\n"
    return out.encode()


def fingerprint(data):
    full = hashlib.sha256(data).digest()
    return int.from_bytes(full, "big") >> (256 - 32)
