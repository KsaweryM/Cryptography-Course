from network import P, run, key_from_secret, decrypt


class Mallory:
    """Mallory sits on the cable. This time she has no secret m of her own."""

    def __init__(self):
        self.key = None   # the key Mallory reads with (TODO 2)

    def change_A(self, A):
        # Alice sends A to Bob.
        # TODO 1: send 1 to Bob instead of A
        return A

    def change_B(self, B):
        # Bob sends B to Alice.
        # TODO 1: send 1 to Alice instead of B
        return B

    def change_message(self, data):
        # Alice sends an encrypted message to Bob.
        # TODO 2: Alice's secret is 1^a and Bob's is 1^b. Make the key from that secret,
        #         self.key = key_from_secret(...), read the message: print("Mallory reads:", decrypt(self.key, data)),
        #         and pass the data on unchanged
        return data


def accept_all(value):
    """No check: Alice and Bob take every value they receive."""
    return True


def check_public(value):
    # TODO 3: return True only if 1 < value < P - 1, else False
    return True


print("Without the check:")
mallory = Mallory()
run(mallory, accept_all)
if mallory.key is None:
    print("not done yet: TODO 1 and 2")

print("With the check:")
run(Mallory(), check_public)
if check_public(1):
    print("not done yet: TODO 3")
