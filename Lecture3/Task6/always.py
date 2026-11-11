# The small example: p = 17, q = 11
n, e, d = 187, 7, 23

# Predict first: does every P from 0 to 186 come back after encrypting and decrypting?
# What about P = 17 or P = 22, which share a factor with n?

wrong = []
# TODO: for every P in range(n): encrypt with pow(P, e, n), decrypt with pow(C, d, n)
#       and add P to the list wrong if the result is not P.

print("checked:", n, "values")
print("wrong:  ", wrong)
print("P = 17 ->", pow(17, e, n), "->", pow(pow(17, e, n), d, n))
