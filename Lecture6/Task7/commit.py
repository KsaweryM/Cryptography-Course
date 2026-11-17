import hashlib

# Monday: before the match Coventry City against Leeds United, three people publish a commitment
# to their prediction of the final score. The predictions look like b"2:1" (home goals, a colon, away goals).
ALICE_COMMIT = "1e01d9f76e145d12a694bf020769c418a32301f6512a5333c374bba3b9669e0f"
MALLORY_COMMIT = "ab08e2164852d59236526ba3151f62c0aadb0e1a4e6a69bee5c85bedbcf92c9c"
CAROL_COMMIT = "59a5a0c7c39734d9c3359438fe114555c618f012aea84f3e4933246f7795575d"          # Carol hashed only her prediction, without a random r

# Saturday, after the match (it ended 2:1): Alice and Mallory reveal r and their prediction.
ALICE_R = bytes.fromhex("5f1c9a07d2e84b36a1c0f7e92d4b8e13")
ALICE_SAYS = b"2:1"
MALLORY_R = bytes.fromhex("c3e8017b9a4d22f6085e1db7a9c4f350")
MALLORY_SAYS = b"2:1"


def commit(r, prediction):
    """A commitment: the SHA-256 of r followed by the prediction, as 64 hex digits."""
    # TODO 1: return hashlib.sha256(r + prediction).hexdigest()      (r + prediction joins the two byte strings)
    return None


def check(commitment, r, prediction):
    """True when (r, prediction) is what was committed to."""
    # TODO 2: compute the commitment again from r and prediction, and compare it with the published one (==)
    return None


# TODO 3: Bob guesses Carol's prediction from CAROL_COMMIT alone: try every score home:away with home and away
#         from 0 to 9 (two nested for loops), make the bytes with (str(home) + ":" + str(away)).encode(),
#         and stop when hashlib.sha256(guess).hexdigest() == CAROL_COMMIT. Count the tries.
carol_guess = None
tries = 0

# The printing is ready.
if commit(b"r", b"1:0") is None:
    print("not done yet: TODO 1")
else:
    print("commit(r, 1:0) with r = b'r':", commit(b"r", b"1:0"))
if check(ALICE_COMMIT, ALICE_R, ALICE_SAYS) is None:
    print("not done yet: TODO 2")
else:
    print("Alice says 2:1, matches her commitment:", check(ALICE_COMMIT, ALICE_R, ALICE_SAYS))
    print("Mallory says 2:1, matches her commitment:", check(MALLORY_COMMIT, MALLORY_R, MALLORY_SAYS))
if carol_guess is None:
    print("not done yet: TODO 3")
else:
    print("Carol predicted", carol_guess.decode(), "(found after", tries, "tries)")
