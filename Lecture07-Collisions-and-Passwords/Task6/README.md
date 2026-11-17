# Task 6: the leaked table with salt

## The situation

A better web shop stored, for each user, a random **salt** (16 bytes, different for every user, not secret) and `SHA-256(salt + password)`. Its table has leaked too: `leaked_users.txt` has lines `user:salt:digest`. The users and their passwords are the same as in Task 5, and Mallory has the same `wordlist.txt`.

![The leaked table with three columns: user, salt (public), SHA-256(salt + password). alice a54dca182530bb1d... 27b9f609667f414e..., carol 3460be31201e69fe... d1d5d3c780e63250..., dave 7c2999fdafe59325... 04c4b03e1951548b..., ... the same 12 users as in Task 5. wordlist.txt goes into SHA-256(salt of user u + guess). Cracked: ? of 12, SHA-256 computations: ?. For every user: every guess again, with that user's salt. Compare with Task 5: 3 529 computations.](figure.svg)

## Goal

Crack the salted table and compare the number of SHA-256 computations with Task 5 (3 529).

## Ready for you

- `crack_salted.py`: `load_users(path)` returns three parallel lists `names[i]`, `salts[i]` (bytes) and `digests[i]` (hex text); `load_words(path)`.
- `salts[u] + typed.encode()` joins the salt and the password bytes into one buffer, the salt first.

Before you run it, predict: more or fewer users cracked than in Task 5? More or fewer computations?

## Steps

Write your code in `crack_salted.py`, in place of the `TODO` comments:

1. `check_login(u, typed)`: return whether `hashlib.sha256(salts[u] + typed.encode()).hexdigest()` equals `digests[u]`.
2. The attack, user by user: for every user `u`, go through the words; for each, compute `sha256(salts[u] + word)` (add 1 to `hashes`) and compare with `digests[u]`. On a match print `f"{names[u]}: {word}"`, add 1 to `cracked` and `break` (go to the next user).
3. Print the summary line given in the comment.

## Expected output

<details>
<summary>Check your answer</summary>

```
12 users, 3529 guesses in the list
carol: salt 3460be31201e69fedaa0eee8b9997f5c  digest d1d5d3c780e63250...
dave:  salt 7c2999fdafe593253cd654af4dfad714  digest 04c4b03e1951548b...
alice types monkey123: True
alice: monkey123
bob: Liverpool1
carol: iloveyou
dave: iloveyou
frank: qwerty
grace: dragon2024
ivan: 123456
judy: Summer2025
oscar: football!
cracked 9 of 12 users with 11795 SHA-256 computations
```

The same 9 users fall: salt does not make a weak password strong. But carol's and dave's digests no longer match, and the work grew to 11 795 computations (if nobody fell, 12 × 3 529 = 42 348). With a million users it would be a million times the work of Task 5.

</details>

## Run

```
python3 crack_salted.py
```

About 8 minutes. Python 3.8 or newer, no extra libraries.
