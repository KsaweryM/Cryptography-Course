# Task 7: use bcrypt

## The situation

Bob's web shop now stores passwords with **bcrypt**, a slow password hash. When Alice makes an account with the password `blue tulip 42`, the server stores one line of text such as `$2b$04$` + 22 characters of salt + 31 characters of hash. At every login it checks what Alice typed against that line.

![Alice's password "blue tulip 42", a new random salt and cost = 4 go into bcrypt. Out come two texts, first and second, both starting with $2b$04$ followed by question marks: the same text twice? Below: Bob's server at login, check_password("blue tulip 42", first) = ? and check_password("blue tulip 43", first) = ?](figure.svg)

## Goal

Hash a password twice, check a right and a wrong password, and take the bcrypt text apart.

## Ready for you

- `bcrypt_ready.py` (you do not need to read it): `hash_password(password, cost)` makes a new random salt and returns the bcrypt text; `check_password(password, stored)` returns `True` or `False`. It is bcrypt in pure Python, checked against the published test vectors; it is about 100 times slower than the C code real servers use, so we use cost 4 (about 0.2 s per hash).
- `text.split("$")` cuts a text at every `$`, like `strtok` in C, and returns the pieces as a list.

Before you run it, predict: the same password, hashed twice: the same text or not?

## Steps

Write your code in `use_bcrypt.py`, in place of the `TODO` comments:

1. `first = hash_password(PASSWORD, COST)`, then `second` the same way. Print both.
2. Print `check_password(PASSWORD, first)` and `check_password("blue tulip 43", first)`.
3. `parts = first.split("$")` gives `["", "2b", "04", "<53 characters>"]`. Print the version `parts[1]`, the cost `parts[2]`, the salt `parts[3][:22]` and the hash `parts[3][22:]`.

## Expected output

The salts are random, so your texts differ from these; the structure is the same.

<details>
<summary>Check your answer</summary>

```
first:  $2b$04$qTQy5IYfH6s9WD0einJAI.iMA463eVVKCsWryysiMUUWkdOZYiKCS
second: $2b$04$tLH6T1rHhyp8lbuhZMdyYepQnMFPGBM2obSypF8panNMwUN8jxygG
right password: True
wrong password: False
version: 2b
cost:    04
salt:    qTQy5IYfH6s9WD0einJAI.
hash:    iMA463eVVKCsWryysiMUUWkdOZYiKCS
```

Two different texts for one password, because bcrypt makes a new salt every time. `check_password` still works, because it reads the salt and the cost from the stored text.

</details>

## Run

```
python3 use_bcrypt.py
```

About 7 minutes. Python 3.8 or newer, no extra libraries; the program runs about 1 second.
