import time

from schemes import NAMES, load_keys, sign, verify, public_key_size

message = b"Release 4.2 of the Notes app. Alice"
ROUNDS = 200

for i in range(len(NAMES)):
    name = NAMES[i]
    private_key, public_key = load_keys(name)

    # TODO 1: the sizes: public_key_size(name, public_key), and len(...) of one signature sign(name, private_key, message)
    key_size = None
    signature_size = None

    # TODO 2: sign the same message twice (sig_a and sig_b). Are the two signatures equal (==)?
    #         Do both pass verify(name, public_key, message, sig)?
    same = None
    both_valid = None

    # TODO 3: the time of one sign and one verify, in milliseconds. time.perf_counter() gives seconds
    #         (like clock_gettime in C): read it, run sign ROUNDS times in a for loop, read it again,
    #         and divide the difference by ROUNDS; multiply by 1000 for ms. Then the same for verify.
    sign_ms = None
    verify_ms = None

    # The printing is ready: each line says "not done yet" until its TODO is done.
    print(name)
    if key_size is None or signature_size is None:
        print("  not done yet: TODO 1")
    else:
        print("  public key:", key_size, "bytes, signature:", signature_size, "bytes")
    if same is None or both_valid is None:
        print("  not done yet: TODO 2")
    else:
        print("  signed twice, the same signature:", same, " both valid:", both_valid)
    if sign_ms is None or verify_ms is None:
        print("  not done yet: TODO 3")
    else:
        print("  sign: %.3f ms   verify: %.3f ms" % (sign_ms, verify_ms))
