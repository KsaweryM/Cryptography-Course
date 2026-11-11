from chacha20_ready import chacha20

key = bytes.fromhex("c0ffee00" * 8)              # 32 bytes
nonce = bytes.fromhex("0000004a0000000000000007")   # 12 bytes
ciphertext = bytes.fromhex(
    "36323fcd0cbf7202049805976e0d4afda0a2bc36"
    "3f02eea05b49125427ad01f9709e3275ef98d8"
)

# TODO: decrypt the ciphertext with
#       chacha20(key, nonce, counter, data).
#       The message was encrypted starting with counter 1.
#       Print the plaintext as text: plaintext.decode()
