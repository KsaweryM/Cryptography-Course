import time

from rc4 import keystream

known = b"Hello"
c1 = bytes.fromhex("F3CA21A4C01000B3D35238B2E470F5AC374F84DA0B64AEAF56F4FA38762E10AE5DF1D800E582179D32AC")  # key: 1 byte
c2 = bytes.fromhex("C20CC3AE782BDDF07248FDEB9506A8A04A8FC587EB9189B9001AC1CEB3A73B78D15529F7FD1F63ADFDB65286437A654CEE")  # key: 2 bytes


def crack(ciphertext, n):
    keys = []
    # TODO 1: try every key of n bytes. Add to keys every key whose
    #         keystream turns the first 5 bytes of the ciphertext into known.
    # Hint: for k in range(256 ** n):
    #           key = k.to_bytes(n, "big")
    return keys


ciphertexts = [c1, c2]
key_lengths = [1, 2]
for t in range(2):
    n = key_lengths[t]
    start = time.time()
    keys = crack(ciphertexts[t], n)
    seconds = time.time() - start
    if len(keys) == 0:
        print("not done yet: TODO 1")
        continue
    found = ""
    for k in range(len(keys)):
        found = found + keys[k].hex() + " "
    print(f"{n} byte(s): keys {found}, {seconds:.2f} s")
    # TODO 2: decrypt the whole ciphertext with keys[0] and print it.
    #         Replace the line below.
    print("not done yet: TODO 2")

# TODO 3: from the two times above, estimate (do not run it!)
#         how long the same search would take for a key of 5 bytes, and of 16 bytes.
#         Replace the line below with a print of your two estimates.
print("not done yet: TODO 3")
