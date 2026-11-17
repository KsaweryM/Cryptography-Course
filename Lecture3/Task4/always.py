# The small example: p = 17, q = 11
n, e, d = 187, 7, 23

# Predict first: does every P from 0 to 186 come back after encrypting and decrypting?
# What about P = 17 or P = 22, which share a factor with n?

wrong = None
# TODO: wrong = [] (an empty list), then for every P in range(n):
#       encrypt with C = pow(P, e, n), decrypt with pow(C, d, n)
#       and add P to the list with wrong.append(P) if the result is not P.

if wrong is None:
    print("not done yet: TODO")
else:
    print("checked:", n, "values")
    print("wrong:  ", wrong)
