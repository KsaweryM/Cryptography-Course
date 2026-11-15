# Task 1: decrypt a message

## The situation

A sender wants to give you a short secret message. Before, you met and both got the same 11 random bytes: the **one-time pad**. The sender XORed the message with the pad and sent the result, the ciphertext, where anyone can see it. Without the pad it is noise. With the pad, you can read it.

![The ciphertext row and the pad row, byte under byte. The first column is worked out: A3 XOR EB = 48, ASCII code 72, the letter H. The other 10 letters are question marks.](figure.svg)

## Goal

Print the secret message.

## Ready for you

- `decrypt.py`: two lists of 11 numbers, `ciphertext` and `pad`, already filled in:

```
ciphertext  A3 FA 1B ED D8 14 BE 1A C2 6B 2F
pad         EB 9F 77 81 B7 34 CA 72 A7 19 4A
```

## Steps

Write your code in place of the `TODO` comment in `decrypt.py`:

1. XOR each ciphertext byte with the pad byte at the same position: `ciphertext[i] ^ pad[i]`.
2. Each result is an ASCII code. Turn it into a letter: `chr(72)` gives `H` (like the cast `(char)72` in C).
3. Print the whole message.

```python
plaintext = ""
for i in range(len(ciphertext)):
    # TODO: add one letter to plaintext
print(plaintext)
```

## Expected output

One line: the message, 11 characters, starting with `H`.

<details>
<summary>Check your answer</summary>

```
Hello there
```

</details>

## Run

```
python3 decrypt.py
```

About 5 minutes. Python 3, no extra libraries.
