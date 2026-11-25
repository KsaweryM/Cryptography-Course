import secrets

from network import P, G, run, key_from_secret, encrypt, decrypt


class Mallory:
    """Mallory sits on the cable. Every value sent between Alice and Bob passes through her."""

    def __init__(self):
        self.m = secrets.randbits(256)       # Mallory's own secret
        self.g_m = pow(G, self.m, P)         # and her public value g^m (g_m: "g to the m")
        self.key_alice = None                # the key Mallory shares with Alice (TODO 1)
        self.key_bob = None                  # the key Mallory shares with Bob (TODO 2)

    def change_A(self, A):
        # Alice sends A to Bob.
        # TODO 1: compute the secret Mallory will share with Alice, A^m mod P,
        #         keep the key: self.key_alice = key_from_secret(...)
        #         and send Mallory's own value to Bob instead of A
        return A

    def change_B(self, B):
        # Bob sends B to Alice.
        # TODO 2: the same for Bob: self.key_bob, and send g_m to Alice instead of B
        return B

    def change_message(self, data):
        # Alice sends an encrypted message to Bob.
        # TODO 3: decrypt it with the key shared with Alice and print it: print("Mallory reads:", text),
        #         then encrypt it again with the key shared with Bob and pass it on
        return data


mallory = Mallory()
run(mallory)
if mallory.key_alice is None:
    print("not done yet: TODO 1 to 3")
