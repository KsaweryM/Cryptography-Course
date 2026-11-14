# WEP problem 2: the key itself leaks.
# For each secret key byte, every weak packet casts one vote (mostly wrong, but
# the right value wins). We recover the whole Wi-Fi key, byte by byte.
from wep import capture, SECRET
from fms import fms_guess

packets = capture()
print("captured", len(packets), "packets with weak IVs\n")

recovered = []
for A in range(len(SECRET)):
    votes = [0] * 256
    for packet in packets:
        iv = packet[:3]
        if iv[0] == A + 3 and iv[1] == 255:
            first_keystream_byte = packet[3] ^ 0xAA     # plaintext starts with 0xAA
            guess = fms_guess(iv, first_keystream_byte, recovered)
            votes[guess] += 1

    ranked = sorted(range(256), key=lambda v: votes[v], reverse=True)
    winner = ranked[0]
    recovered.append(winner)
    print(f"K[{A}]: top guesses  "
          f"{winner:02X} ({votes[ranked[0]]} votes), "
          f"{ranked[1]:02X} ({votes[ranked[1]]}), "
          f"{ranked[2]:02X} ({votes[ranked[2]]})")

print()
print("recovered key:", bytes(recovered).hex(" "))
print("real key:     ", SECRET.hex(" "))
print("match:", bytes(recovered) == SECRET)
