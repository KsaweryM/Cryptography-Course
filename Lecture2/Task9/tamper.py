from aead import chacha20, seal, unseal, TagError

key = bytes.fromhex("0badc0de" * 8)
nonce = bytes.fromhex("000000000000000000000001")
message = b"Pay 100 EUR to Anna."

# Without a tag: only ChaCha20, the data starts at counter 1
plain = chacha20(key, nonce, 1, message)
# With a tag: ChaCha20-Poly1305
sealed = seal(key, nonce, message)
print("sealed:", sealed.hex(), f"({len(message)} bytes + 16 bytes of tag)")

# The attacker changes "1" (0x31) into "9" (0x39): XOR 0x08 at position 4.
# TODO 1: make changed_plain: a copy of plain with byte 4 XORed with 0x08
#         hint: b = bytearray(plain); b[4] ^= 0x08; changed_plain = bytes(b)
# TODO 2: make changed_sealed in the same way from sealed
# TODO 3: decrypt changed_plain with chacha20(key, nonce, 1, ...) and print it
# TODO 4: decrypt changed_sealed with unseal(key, nonce, ...) inside
#         try: ... except TagError as e: print("rejected:", e)
