# Task 7: commitments

## The situation

On Monday, before the match Coventry City against Leeds United, Alice, Mallory and Carol each want to prove later that they predicted the final score, without telling anybody now. Each publishes a **commitment**: Alice and Mallory publish SHA-256(r ‖ prediction), where r is 16 secret random bytes; Carol publishes only SHA-256(prediction). The match ends 2:1. On Saturday Alice and Mallory reveal r and their prediction, and both say "2:1". Bob checks them. Then he wonders whether he could have read Carol's prediction already on Monday.

![Monday: Alice in indigo, Mallory in pink and Carol each publish a brown commitment; Alice's and Mallory's are made from an amber secret r and a violet prediction, Carol's only from a prediction. Saturday: Alice and Mallory reveal r and "2:1". Bob in teal recomputes and asks "match? ?" for each. Bob also tries all scores 0:0 to 9:9 against Carol's commitment: "Carol predicted ?".](figure.svg)

## Goal

Make and check commitments with a hash, catch the one who changed her prediction, and see why the random r is needed.

## Ready for you

- `commit.py`: the three published commitments, the revealed values of Alice and Mallory, and the printing. Each part says `not done yet: TODO n` until its TODO is done.

## Steps

1. In `commit(r, prediction)`: return `hashlib.sha256(r + prediction).hexdigest()`. `r + prediction` joins the two byte strings.
2. In `check(commitment, r, prediction)`: compute the commitment again from `r` and `prediction` and compare it with the published `commitment` (`==` on two strings compares them character by character, like `strcmp(a, b) == 0`).
3. Carol's commitment has no r. Try every score `home:away` with `home` and `away` from 0 to 9 (two nested `for` loops), as bytes `(str(home) + ":" + str(away)).encode()`, until `hashlib.sha256(guess).hexdigest() == CAROL_COMMIT`. Count the tries.

## Expected output

Alice passes, Mallory fails, and Carol's prediction is found in fewer than 100 tries.

<details>
<summary>Check your answer</summary>

```
commit(r, 1:0) with r = b'r': 544c617b43e09262d154e248e68fd39f0648df05360f04587bad2f8f59ab4f52
Alice says 2:1, matches her commitment: True
Mallory says 2:1, matches her commitment: False
Carol predicted 3:1 (found after 32 tries)
```

Mallory committed to a different score on Monday and now claims 2:1: to pass, she would need another input with the same digest, a second preimage. Carol's prediction is one of only 100 scores, so Bob just hashes all of them: preimage resistance protects nothing when the input can be guessed. The 16 random bytes of r make the input impossible to guess (2^128 possibilities).

</details>

## Run

```
python3 commit.py
```

About 9 minutes. Python 3.8 or newer, no extra libraries.
