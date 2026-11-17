# Task 6: k used twice

## The situation

ElGamal is safe only if k is new for every message. One sender got this wrong: two ciphertexts for Bob were made with **the same k**, so their C1 is the same. You do not have Bob's private key. But you know the first message: it was printed on a public receipt.

![Two ElGamal ciphertexts for Bob, from reuse.py. First: C1 = 26838989395851..., C2 = 17820659653148..., and its message is known from a public receipt: "Payment approved: 250 EUR, order 1187." Second: C1 = 26838989395851..., C2 = 19065383106845..., and its message is unknown. The two C1 are the same: the sender used the same k twice. Bob's private key x is not in the file: you do not have it.](figure.svg)

## Goal

Recover the second message, without Bob's private key.

## Ready for you

- `reuse.py`: `P` (2048 bits) and `G = 2`.
- `reuse.py`: `C1` (the same in both), `C2_first` and `C2_second`, and the known first message `first`.
- `reuse.py`: `text_to_number(text)` and `number_to_text(number)` turn text into a number and back.

## Steps

Write your code in place of the `TODO` comments in `reuse.py`. `pow(n, -1, P)` gives the inverse of `n` mod `P`, and `text_to_number(first)` gives the first message as a number, `M_first`.

1. What is the same in both C2? Get it from the known message.
2. Use it to get the second message, `M_second`, from `C2_second`. The code at the end prints it as text.

<details>
<summary>Hint</summary>

Both C2 hide their message with the same mask y^k mod p. `C2_first = M_first * y^k mod P`, so `y^k = C2_first * (inverse of M_first) mod P`. Then `M_second = C2_second * (inverse of y^k) mod P`.

</details>

## Expected output

Without your code the program prints `not done yet: TODO 1 and 2`. With it: one line, the second message, readable text.

<details>
<summary>Check your answer</summary>

```
second message: New door code for the server room: 4096.
```

Bob's private key was never needed. One known message and a repeated k are enough.

</details>

## Run

```
python3 reuse.py
```

About 7 minutes. Python 3.8 or newer (for `pow(n, -1, P)`), no extra libraries.
