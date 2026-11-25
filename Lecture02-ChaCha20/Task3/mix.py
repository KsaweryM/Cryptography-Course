# Task 3: which one mixes faster, Salsa20 or ChaCha20?
# salsa.py and chacha.py are ready: quarter_round(s, a, b, c, d), rounds(s, n), initial_state(key, counter, nonce).
import salsa
import chacha


def changed_bits(x, y):
    # how many bits differ between two 32-bit words: the 1 bits of x XOR y
    # (bin(v) is the text "0b1011..."; .count("1") counts its ones, like __builtin_popcount in C)
    return bin(x ^ y).count("1")


words = [0x11111111, 0x01020304, 0x9B8D6F43, 0x01234567]   # a, b, c, d: the input of RFC 8439, 2.1.1
key = bytes(range(32))                                        # 00 01 02 ... 1F

one_salsa = None     # bits changed (of 128) by one Salsa20 quarter round when bit 0 of a flips
one_chacha = None    # the same for ChaCha20
avg_salsa = None     # the average over all 128 input bits
avg_chacha = None
table = None         # table[n] = [Salsa20, ChaCha20]: bits changed (of 512) after n rounds, n = 1 to 4

# Predict first: one quarter round does 12 small steps in both ciphers. Which one spreads a 1-bit change further?

# TODO 1: one quarter round. x = list(words), y = list(words) with y[0] ^= 1 (bit 0 of a flipped).
#         salsa.quarter_round(x, 0, 1, 2, 3) and the same for y, then one_salsa = the sum of
#         changed_bits(x[k], y[k]) for k = 0 to 3. Then the same with chacha.quarter_round: one_chacha.

# TODO 2: the same for each of the 128 input bits: for i in range(128), flip bit i % 32 of word i // 32
#         (y[i // 32] ^= 1 << (i % 32)). avg_salsa = the total / 128, the same for avg_chacha.

# TODO 3: the whole table. key2 = bytearray(key), key2[0] ^= 1: two keys that differ in one bit.
#         table = {} (a dictionary: table[n] = ... works like an array indexed by n).
#         For n = 1 to 4: s1 = salsa.initial_state(key, 0, bytes(8)), s2 = the same with key2,
#         salsa.rounds(s1, n), salsa.rounds(s2, n), count the changed bits over all 16 words.
#         The same with chacha.initial_state(key, 0, bytes(12)) and chacha.rounds. table[n] = [salsa bits, chacha bits]

# The printing is ready: each line says "not done yet" until its TODO is done.
if one_salsa is None or one_chacha is None:
    print("not done yet: TODO 1")
else:
    print("one quarter round, bit 0 of a flipped (of 128 bits):")
    print("  Salsa20: ", one_salsa)
    print("  ChaCha20:", one_chacha)
if avg_salsa is None or avg_chacha is None:
    print("not done yet: TODO 2")
else:
    print(f"average over all 128 input bits: Salsa20 {avg_salsa:.1f}, ChaCha20 {avg_chacha:.1f}")
if table is None:
    print("not done yet: TODO 3")
else:
    print("whole table, one key bit flipped (of 512 bits; random would be about 256):")
    print("  rounds  Salsa20  ChaCha20")
    for n in range(1, 5):
        print(f"  {n:6}  {table[n][0]:7}  {table[n][1]:8}")
