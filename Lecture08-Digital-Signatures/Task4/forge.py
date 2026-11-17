from bank_ready import n, e, amount_1, sig_1, amount_2, sig_2, short

# Alice's bank takes an order as one number, the amount in pounds, signed with textbook RSA:
# the signature s is valid for the amount m when s^e mod n == m.
# Mallory has two orders that Alice signed for her: 20 pounds and 50 pounds. She does not have d.
print("order 1:", amount_1, "pounds, signature", short(sig_1))
print("order 2:", amount_2, "pounds, signature", short(sig_2))

# TODO 1: check both orders as the bank does: pow(sig_1, e, n) == amount_1, and the same for order 2
check_1 = None
check_2 = None

# TODO 2: Mallory multiplies the two signatures: forged = sig_1 * sig_2 % n.
#         The bank checks forged as a signature on the amount amount_1 * amount_2.
forged = None
check_forged = None

# TODO 3: Mallory picks any number as a signature, e.g. any_sig = 123456789, and computes the amount
#         it signs: any_amount = pow(any_sig, e, n). The bank checks any_sig on any_amount.
any_sig = None
any_amount = None
check_any = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if check_1 is None or check_2 is None:
    print("not done yet: TODO 1")
else:
    print("the bank checks order 1:", check_1, " order 2:", check_2)
if forged is None or check_forged is None:
    print("not done yet: TODO 2")
else:
    print("forged signature:", short(forged))
    print("the bank checks it on", amount_1 * amount_2, "pounds:", check_forged)
if any_sig is None or any_amount is None or check_any is None:
    print("not done yet: TODO 3")
else:
    print("any signature:", any_sig, " signs the amount", short(any_amount))
    print("the bank checks it:", check_any)
