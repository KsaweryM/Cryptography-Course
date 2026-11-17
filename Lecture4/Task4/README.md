# Task 4: be Mallory

## The situation

Alice and Bob do a Diffie-Hellman exchange and then Alice sends Bob one encrypted message. Nobody checks who is on the other side. You are Mallory, sitting on the cable: every value between them passes through you, and you may send on whatever you want. Alice should end up sharing a key with you, Bob should end up sharing another key with you, and both should think that everything is fine.

![Alice on the left, Mallory (you, at a laptop) in the middle, Bob on the right. Mallory has her own secret m and public value g^m mod p (self.g_m). Three things pass through Mallory, each through a function with a TODO: 1. Alice's A goes through change_A(A), and what reaches Bob is unknown; 2. Bob's B goes through change_B(B) on its way to Alice; 3. Alice's message, encrypted with her key, goes through change_message(data), and Bob decrypts and prints what he gets. Ready in network.py, not to be changed: key_from_secret(secret) turns a Diffie-Hellman secret into a 32-byte key; encrypt(key, text) and decrypt(key, data).](figure.svg)

## Goal

Read Alice's message, and pass it on so that Bob notices nothing.

## Ready for you

- `network.py` (do not change it): `P`, `G`, Alice, Bob and the network, `run(mallory)`, which calls your three functions in the order of the figure.
- `network.py`: `key_from_secret(secret)` turns a Diffie-Hellman secret into a 32-byte key (with SHA-256), `encrypt(key, text)` gives bytes, `decrypt(key, data)` gives text.
- The cipher in `network.py` is a simple stream cipher: it XORs the bytes of the text with a keystream made from the key by SHA-256, and the same XOR again gives the text back.
- `mitm.py`: the class `Mallory` with her secret m (`self.m`) and her public value g^m mod p (`self.g_m`; the name is read "g to the m", because Python names cannot contain `^`). `self.g_m` is what she sends instead of A and B.

## Steps

Write your code in place of the `TODO` comments in `mitm.py`. `self` is like a pointer to a struct in C: `self.key_alice = ...` stores a field that the other functions can read.

1. `change_A(self, A)`: Alice sends `A` to Bob. Compute the secret Mallory will share with Alice, `A^m mod P` (`pow(A, self.m, P)`), keep the key, `self.key_alice = key_from_secret(...)`, and return Mallory's own value `self.g_m` instead of `A`. Why A^m: Alice takes `self.g_m` for Bob's B and computes (g^m)^a = g^(am); Mallory knows m, so she gets the same g^(am) as A^m = (g^a)^m.
2. `change_B(self, B)`: the same for Bob: keep `self.key_bob`, and return `self.g_m` instead of `B`.
3. `change_message(self, data)`: decrypt the message with the key shared with Alice and print it, `print("Mallory reads:", text)`, then encrypt it again with the key shared with Bob and return it.

## Expected output

Without your code, the program prints only what Bob reads. With it, two lines: first what Mallory reads, then what Bob reads. Both are the same text, so Bob has no reason to suspect anything.

<details>
<summary>Check your answer</summary>

```
Mallory reads: My new card PIN is 7314. Please keep it secret.
Bob reads: My new card PIN is 7314. Please keep it secret.
```

</details>

## Run

```
python3 mitm.py
```

About 10 minutes. Python 3, no extra libraries.

Want to see it step by step? [Mallory in the middle](https://ksawerym.github.io/Cryptography-simulators/diffie-hellman/#3) shows the same attack on small numbers.
