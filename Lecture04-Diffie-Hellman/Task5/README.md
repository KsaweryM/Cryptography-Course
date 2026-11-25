# Task 5: Mallory sends 1

## The situation

Alice and Bob do a Diffie-Hellman exchange again, and Alice sends Bob one encrypted message. You are Mallory on the cable, as in Task 4, but this time you have no secret of your own and you do no exchange at all: you just replace both public values with the number 1. Then you read Alice's message. In the second run, Alice and Bob check every value they receive, and the attack should stop.

![Alice on the left, Mallory (you, at a laptop, with no secret of her own: she sends 1) in the middle, Bob on the right. 1: Alice's A goes through change_A(A), then through Bob's check_public (TODO 3), and what Bob gets is unknown; 1: Bob's B goes through change_B(B), then through Alice's check_public (TODO 3). 2: Alice's message, encrypted with her key, goes through change_message(data): Mallory reads it with the key from which secret? Bob decrypts it and prints it. Ready in network.py, not to be changed: key_from_secret(secret), decrypt(key, data), and run(mallory, check), in which Alice and Bob pass every value they receive to check. The program runs twice: first with no check, then with your check_public.](figure.svg)

## Goal

Read Alice's message without any secret of your own, then stop the attack with one comparison.

## Ready for you

- `network.py` (do not change it): `P`, `G`, Alice, Bob and `run(mallory, check)`. It is the network of Task 4, with one difference: Bob calls `check(A)` on the value he receives, Alice calls `check(B)`, and each of them stops the exchange when `check` returns `False`.
- `network.py`: `key_from_secret(secret)` turns a Diffie-Hellman secret into a 32-byte key, and `decrypt(key, data)` gives the text.
- `send_one.py`: the class `Mallory`, the function `accept_all` (no check at all), and the program that runs the exchange twice, first with `accept_all`, then with your `check_public`.

## Steps

Write your code in place of the `TODO` comments in `send_one.py`.

1. `change_A` and `change_B`: return `1` instead of `A` and instead of `B`.
2. `change_message(self, data)`: Alice now computes 1^a mod P and Bob computes 1^b mod P. What number is that, whatever a and b are? Make the key from it, `self.key = key_from_secret(...)`, print the message, `print("Mallory reads:", decrypt(self.key, data))`, and return `data` unchanged. Predict first: does Mallory have to encrypt the message again for Bob, as in Task 4?
3. `check_public(value)`: return `True` only if `1 < value < P - 1`. In C this is `return 1 < value && value < P - 1;`; Python also allows the chained form `1 < value < P - 1`.

<details>
<summary>Hint for step 2</summary>

1 times 1 times 1 ... is still 1, so both secrets are 1, and both keys are `key_from_secret(1)`. Alice and Bob have the same key, so Mallory passes the message on as it is.

</details>

## Expected output

Without your code, the program prints what Bob reads in both runs, and `not done yet: TODO 1 and 2` and `not done yet: TODO 3`.

<details>
<summary>Check your answer</summary>

```
Without the check:
Mallory reads: The new Wi-Fi password is Blue-Heron-58.
Bob reads: The new Wi-Fi password is Blue-Heron-58.
With the check:
Bob rejects A = 1 and stops.
```

Alice and Bob both had the key from the secret 1, so they could even compare their keys and see nothing wrong. Mallory needed no computation at all. With the check, Bob refuses A = 1 before he computes anything.

</details>

## Run

```
python3 send_one.py
```

About 8 minutes. Python 3, no extra libraries.

Want more? Return `P - 1` instead of `1`. (P - 1)^a mod P is 1 when a is even and P - 1 when a is odd, so Mallory has two keys to try, and half of the time Alice and Bob end up with different keys. `check_public` refuses P - 1 too.

Want to see it on small numbers? [Mallory in the middle](https://ksawerym.github.io/Cryptography-simulators/diffie-hellman/#3) has the switch "Mallory sends: 1" and the check "1 < value < p - 1".
