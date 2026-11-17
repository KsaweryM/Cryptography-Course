# Task 5: the leaked table without salt

## The situation

Bob's small web shop stored, for each user, `SHA-256(password)` in hex. The table has leaked: Mallory has `leaked_users.txt` with 12 users. She cannot reverse SHA-256, but she can guess: she has a list of 3 529 common passwords (`wordlist.txt`, made up for this course in the style of real lists).

![Left: the leaked table, user and stored SHA-256(password): alice e48443929f57ec4c..., bob 9cdb4a45f1bba581..., carol e4ad93ca07acb8d9..., dave e4ad93ca07acb8d9..., erin 48486e1514e84234..., frank 65e84be33532fb78..., ... 12 users. Right: Mallory with wordlist.txt (123456, password, 123456789, ..., 3 529 guesses) going into SHA-256, compared with every user. Cracked: ? of 12. A note: TODO 1 first, the server's login check, alice types monkey123 and monkey124.](figure.svg)

## Goal

Write the server's login check, then crack as many users as you can, and count the SHA-256 computations.

## Ready for you

- `crack_unsalted.py`: `load_users(path)` returns two lists of the same length, `names[i]` and `digests[i]` (like two parallel arrays in C); `load_words(path)` returns the list of guesses.
- `hashlib.sha256(text.encode()).hexdigest()`: `text.encode()` turns the Python text into bytes (UTF-8), as the server did.

Before you run it, predict: how many of the 12 users fall, and how many SHA-256 computations does it take?

## Steps

Write your code in `crack_unsalted.py`, in place of the `TODO` comments:

1. `check_login(user, typed)`: find the index of `user` in `names` with an index loop, then return whether `hashlib.sha256(typed.encode()).hexdigest()` equals `digests[index]`.
2. The dictionary attack: for every word, compute its digest **once** (add 1 to `hashes`), then compare it with the digest of every user. On a match, print `f"{names[u]}: {word}"` and add 1 to `cracked`.
3. Print the summary line given in the comment.
4. Print every pair of users with the same digest (two index loops, the inner one from `u + 1`).

## Expected output

<details>
<summary>Check your answer</summary>

```
12 users, 3529 guesses in the list
alice types monkey123: True
alice types monkey124: False
ivan: 123456
frank: qwerty
carol: iloveyou
dave: iloveyou
grace: dragon2024
alice: monkey123
oscar: football!
judy: Summer2025
bob: Liverpool1
cracked 9 of 12 users with 3529 SHA-256 computations
same digest: carol and dave
```

One computation per guess, however many users there are. erin, heidi and peggy survive only because their passwords are not in the list.

</details>

## Run

```
python3 crack_unsalted.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries; the program runs in a fraction of a second.
