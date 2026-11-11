"""A simulated network for Task 4. Ready: you do not need to change it."""
import hashlib
import secrets

# The 2048-bit group 14 from RFC 3526: a public prime p and g = 2
P = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74"
    "020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F1437"
    "4FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
    "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF05"
    "98DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB"
    "9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
    "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF695581718"
    "3995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF",
    16,
)
G = 2


def key_from_secret(secret):
    """Turns a Diffie-Hellman secret into a 32-byte key with SHA-256."""
    return hashlib.sha256(secret.to_bytes(256, "big")).digest()


def _stream(key, length):
    out = b""
    counter = 0
    while len(out) < length:
        out += hashlib.sha256(key + counter.to_bytes(8, "big")).digest()
        counter += 1
    return out[:length]


def encrypt(key, text):
    data = text.encode()
    return bytes(x ^ y for x, y in zip(data, _stream(key, len(data))))


def decrypt(key, data):
    return bytes(x ^ y for x, y in zip(data, _stream(key, len(data)))).decode(errors="replace")


class Ania:
    def start(self):
        self.a = secrets.randbits(256)
        return pow(G, self.a, P)

    def finish(self, B):
        self.key = key_from_secret(pow(B, self.a, P))

    def send(self):
        return encrypt(self.key, "My new card PIN is 7314. Please keep it secret.")


class Bartek:
    def receive_A(self, A):
        b = secrets.randbits(256)
        self.key = key_from_secret(pow(A, b, P))
        return pow(G, b, P)

    def receive_message(self, data):
        print("Bartek reads:", decrypt(self.key, data))


def run(mallory):
    ania, bartek = Ania(), Bartek()
    A = ania.start()
    B = bartek.receive_A(mallory.change_A(A))
    ania.finish(mallory.change_B(B))
    message = ania.send()
    bartek.receive_message(mallory.change_message(message))
