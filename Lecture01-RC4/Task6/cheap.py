ciphertext = bytes.fromhex("F34F841297688A029B0A9108D20A9601"
                           "D14FC503D84E8040DE59C5578413D44E")
known = b"Dear"

numbers = [0, 0, 0, 0]
# TODO 1: find the 4 numbers: numbers[k] = ciphertext[k] ^ known[k] for k = 0, 1, 2, 3

message = ""
# TODO 2: decrypt the whole ciphertext: for every i, XOR ciphertext[i] with numbers[i % 4],
#         turn the result into a character with chr and add it to message

if numbers == [0, 0, 0, 0]:
    print("not done yet: TODO 1")
elif message == "":
    print("not done yet: TODO 2")
else:
    print(message)
