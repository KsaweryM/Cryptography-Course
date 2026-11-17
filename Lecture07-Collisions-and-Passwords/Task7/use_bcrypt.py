# Task 7: use bcrypt.
# Bob runs a web shop. When Alice makes an account, his server stores the bcrypt text of her password.
from bcrypt_ready import hash_password, check_password

PASSWORD = "blue tulip 42"
COST = 4

# TODO 1: make the bcrypt text of PASSWORD twice: first = hash_password(PASSWORD, COST), then second.
#         Print both.
first = None
second = None
print("not done yet: TODO 1")

# TODO 2: Alice logs in. Check the right password and a wrong one against first:
#         check_password(PASSWORD, first) and check_password("blue tulip 43", first). Print both.
print("not done yet: TODO 2")

# TODO 3: take first apart. It looks like $2b$04$ + 22 characters of salt + 31 characters of hash.
#         parts = first.split("$") gives ["", "2b", "04", "<53 characters>"]: print the version parts[1],
#         the cost parts[2], the salt parts[3][:22] and the hash parts[3][22:].
print("not done yet: TODO 3")
