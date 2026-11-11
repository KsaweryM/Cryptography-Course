import secrets

from network import P, G, run, key_from_secret, encrypt, decrypt


class Mallory:
    """Mallory sits on the cable. Every value sent between Ania and Bartek passes through her."""

    def __init__(self):
        self.m = secrets.randbits(256)       # Mallory's own secret
        self.M = pow(G, self.m, P)           # and her public value

    def change_A(self, A):
        # Ania sends A to Bartek.
        # TODO 1: compute the secret Mallory will share with Ania, A^m mod P,
        #         keep the key: self.key_ania = key_from_secret(...)
        #         and send Mallory's own value to Bartek instead of A
        return A

    def change_B(self, B):
        # Bartek sends B to Ania.
        # TODO 2: the same for Bartek: self.key_bartek, and send M to Ania instead of B
        return B

    def change_message(self, data):
        # Ania sends an encrypted message to Bartek.
        # TODO 3: decrypt it with the key shared with Ania and print it,
        #         then encrypt it again with the key shared with Bartek and pass it on
        return data


run(Mallory())
