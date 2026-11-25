# Task 11: a key from a password

## The situation

Alice's diary app encrypts every diary with ChaCha20 (lecture 2). The key is not stored anywhere: the app makes it from the password each time, with **PBKDF2**, a slow hash with a salt, 10 000 iterations. Mallory copied Bob's diary file from his laptop, but not his password. There is no server to stop her guesses: the file is all she needs.

![Top: Alice's password "violet kettle 1987" and the salt from the file go into PBKDF2 (10 000 iterations); out comes a 32-byte key; ChaCha20 with diary_alice.bin gives "Dear diary, ?". Bottom: Mallory feeds the words of wordlist.txt one by one into PBKDF2 and ChaCha20 with diary_bob.bin: starts with "Dear diary,"? password: ?, after ? tries](figure.svg)

## Goal

Make a key from a password, then crack an encrypted file with a dictionary attack, and see what the iteration count changes.

## Ready for you

- `chacha.py` (the same file as in lecture 2, you do not need to read it): `chacha20(key, nonce, counter, data)` encrypts and decrypts.
- `password_key.py`: `read_diary(path)` returns the salt, the iterations, the nonce and the ciphertext of a diary file; `load_lines(path)` reads `wordlist.txt` (the same list as in Task 5).
- `hashlib.pbkdf2_hmac("sha256", password_bytes, salt, iterations, 32)` returns a 32-byte key. `"text".encode()` gives the bytes of a text, like a `char` array in C.
- A diary file: salt (16 bytes), iterations (4 bytes), nonce (12 bytes), ciphertext.

Before you run it, predict: Mallory has no server to slow her down. What does slow her down?

## Steps

Write your code in `password_key.py`, in place of the `TODO` comments:

1. Read `diary_alice.bin`, make the key from `"violet kettle 1987"` with the salt and the iterations of the file, decrypt with counter 1 and print the iterations and the text.
2. Read `diary_bob.bin` and measure one key derivation with its salt and iterations; print it in milliseconds.
3. Try the words of `wordlist.txt` in order: make the key, decrypt only the first 11 bytes, and compare them with `b"Dear diary,"`. On a match print the word, the number of tries and the whole diary, then `break`. Print the time of the whole attack.
4. Print how long the same attack would take with 600 000 iterations (the OWASP advice for PBKDF2-HMAC-SHA256): the time grows in proportion to the iterations.

## Expected output

<details>
<summary>Check your answer</summary>

```
iterations: 10000
Dear diary, today I moved my savings to the new bank. The PIN is in the blue notebook.

one key: 7.0 ms
found after 902 tries: Cookie12
Dear diary, Mallory asked again about the bike. I said no.

attack: 6.6 s
with 600000 iterations: about 7 minutes
```

(Intel i5-8265U, Python 3.12; your times will differ.) A password from a list falls even behind PBKDF2: the iterations only multiply the work, as the cost of bcrypt does. Against a strong, random password the same multiplication makes the attack hopeless. A known start of the file ("Dear diary,") is enough to recognise the right key.

</details>

## Run

```
python3 password_key.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries; the program runs about 10 seconds.
