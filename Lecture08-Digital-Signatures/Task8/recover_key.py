from ecdsa_ready import q, hash_number, public_key, sign, verify


def read_file(path):
    # like fopen(path, "rb") + fread in C: the whole file as bytes
    with open(path, "rb") as f:
        return f.read()


game_1 = read_file("game_1.txt")
game_2 = read_file("game_2.txt")
mallory_game = read_file("mallory_game.txt")

# The console's public key Q = d x G (a point of P-256). The console runs a program only if its signature is valid.
Q = (0x751cb625edb017e30f726d15af4c8746ea1019aafc3ffe8e2a864c0618c58751,
     0x4ae88355355a7f35bd5ae3e337d95649ee141518b87155fae1d8b5e8f9bc685d)
# Alice Games signed both games with ECDSA (P-256, SHA-256). A signature is two numbers (r, s).
r1 = 0xa7ef236729f03041193e3458499fcfb674235d72f7748a605db39ab6e3800979
s1 = 0xb109701cf6d28b0f4d6ecd084441eaba1c9372ea874571df5f65acd6737ab4af
r2 = 0xa7ef236729f03041193e3458499fcfb674235d72f7748a605db39ab6e3800979
s2 = 0x76b7f5c783dd939a8bedcd94ffd88b45c83c1e3ede500b29949e984234c86b4b

print("signature of game 1 valid:", verify(Q, game_1, r1, s1))
print("signature of game 2 valid:", verify(Q, game_2, r2, s2))

# TODO 1: before any attack, look: do the two signatures share the same r (so the same k)? same_r = True or False
same_r = None

# TODO 2: the hashes as numbers: z1 = hash_number(game_1), z2 = hash_number(game_2)
z1 = None
z2 = None

# TODO 3: k from the two equations for s1 and s2 (README, step 3), mod q.
#         Dividing mod q is multiplying by the inverse: pow(x, -1, q), as in Lecture 3.
k = None

# TODO 4: d from the equation of the first signature and k (README, step 4), mod q.
d = None

# TODO 5: is d really the private key? Compare public_key(d) with Q.
d_matches = None

# TODO 6: Mallory signs her own program with d: (r, s) = sign(d, mallory_game). The console checks it with Q.
mallory_valid = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if same_r is None:
    print("not done yet: TODO 1")
else:
    print("r1 == r2:", same_r)
if z1 is None or z2 is None:
    print("not done yet: TODO 2")
else:
    print("z1 =", hex(z1))
    print("z2 =", hex(z2))
if k is None:
    print("not done yet: TODO 3")
else:
    print("k  =", hex(k))
if d is None:
    print("not done yet: TODO 4")
else:
    print("d  =", hex(d))
if d_matches is None:
    print("not done yet: TODO 5")
else:
    print("public_key(d) == Q:", d_matches)
if mallory_valid is None:
    print("not done yet: TODO 6")
else:
    print("the console accepts Mallory's program:", mallory_valid)
