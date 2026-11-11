import time

from rc4 import keystream

known = b"Hello"
c1 = bytes.fromhex("F3CA21A4C01000B3D35238B2E470F5AC374F84DA0B64AEAF56F4FA38762E10AE5DF1D800E582179D32AC")  # key: 1 byte
c2 = bytes.fromhex("C20CC3AE782BDDF07248FDEB9506A8A04A8FC587EB9189B9001AC1CEB3A73B78D15529F7FD1F63ADFDB65286437A654CEE")  # key: 2 bytes


def crack(ciphertext, n):
    # TODO 1: try every key of n bytes. Return a list of
    #         all keys whose keystream turns the start
    #         of the ciphertext into known.
    # Hint: for k in range(256 ** n):
    #           key = k.to_bytes(n, "big")
    return []


for ciphertext, n in [(c1, 1), (c2, 2)]:
    start = time.time()
    keys = crack(ciphertext, n)
    print(f"{n} byte(s): keys {[key.hex() for key in keys]}, {time.time() - start:.2f} s")
    # TODO 2: decrypt the whole ciphertext with the key you found and print it

# TODO 3: from the two times above, estimate (do not run it!)
#         how long the same search would take for a key of 5 bytes, and of 16 bytes.
