# The Fluhrer-Mantin-Shamir step, ready to use.
# You do NOT need to understand this function. Given a weak IV, the first
# keystream byte, and the key bytes found so far, it returns ONE guess for the
# next secret key byte. The guess is right only about 5% of the time, which is
# why the attack collects many packets and takes a vote.


def fms_guess(iv, first_keystream_byte, known_key):
    key = list(iv) + list(known_key)
    A = len(key)                      # the RC4 key index we are solving for
    S = list(range(256))
    j = 0
    for i in range(A):                # run the KSA as far as the known bytes reach
        j = (j + S[i] + key[i]) % 256
        S[i], S[j] = S[j], S[i]
    inverse = [0] * 256               # where each value sits in S
    for index in range(256):
        inverse[S[index]] = index
    return (inverse[first_keystream_byte] - j - S[A]) % 256
