# WEP problem 1: a repeated IV repeats the keystream.
# The attacker knows one packet's plaintext, finds another packet with the
# same IV, and reads it, without ever knowing the key.
from wep import capture, xor

packets, known_index, known_plaintext = capture()
print("captured", len(packets), "packets")

known_packet = packets[known_index]
known_iv = known_packet[:3]
print("known packet has IV", known_iv.hex(" "), "and known plaintext:")
print("   ", known_plaintext[4:].decode())

# Step 1: find another packet that used the same IV.
victim = None
for k in range(len(packets)):
    if k != known_index and packets[k][:3] == known_iv:
        victim = packets[k]
        print("found a second packet with the same IV: packet", k)
        break

# Step 2: the known pair gives us the keystream (ciphertext XOR plaintext).
known_ciphertext = known_packet[3:]
keystream_bytes = xor(known_ciphertext, known_plaintext)

# Step 3: XOR the keystream onto the other packet to read it.
victim_ciphertext = victim[3:]
n = min(len(victim_ciphertext), len(keystream_bytes))
recovered = xor(victim_ciphertext[:n], keystream_bytes[:n])
print("decrypted the second packet:")
print("   ", recovered[4:].decode())
