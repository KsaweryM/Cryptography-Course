# Task 6: k used twice

## The situation

ElGamal is safe only if k is new for every message. One sender got this wrong: two ciphertexts for Bob were made with **the same k**, so their C1 is the same. You do not have Bob's private key. But you know the first message: it was printed on a public receipt. Each C2 is its message times the same hidden mask y^k mod p.

![Two ElGamal ciphertexts for Bob, from reuse.py. First: C1 = 26838989395851..., C2 = 17820659653148..., and its message is known from a public receipt: "Payment approved: 250 EUR, order 1187." Second: C1 = 26838989395851..., C2 = 19065383106845..., and its message is unknown. The two C1 are the same: the sender used the same k twice. Bob's private key x is not in the file: you do not have it.](figure.svg)

## Goal

Recover the second message, without Bob's private key.

## Ready for you

- `reuse.py`: `P` (2048 bits) and `G = 2`.
- `reuse.py`: `C1` (the same in both), `C2_first` and `C2_second`, and the known first message `first`.
- `reuse.py`: `text_to_number(text)` and `number_to_text(number)` turn text into a number and back.

## Steps

Write your code in place of the `TODO` comments in `reuse.py`. `pow(n, -1, P)` gives the inverse of `n` mod `P`.

1. The hidden mask y^k: `C2_first = M_first * y^k mod P`, so `y^k = C2_first * (inverse of M_first) mod P`. `M_first` is `text_to_number(first)`.
2. The second message: `M_second = C2_second * (inverse of y^k) mod P`.
3. Print it as text: `print("second message:", number_to_text(M_second))`.

## Expected output

One line: the second message, readable text.

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
