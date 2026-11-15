# Task 5: ElGamal on a curve

## The situation

Bob has a key pair on the small curve y^2 = x^3 + 2x + 2 mod 17: the private number d = 7 and the public point Q = 7G = (0, 6). Alice wants to send him a message that is already a point of the curve, M = (13, 10). She picks a random k = 4 and sends two points, C1 = kG and C2 = M + kQ. Only Bob, who knows d, can take kQ off again: d C1 = d k G = k Q, so M = C2 - d C1.

![The curve mod 17 as a grid of dots, with G = (5, 1) and Q = (0, 6) in violet and M = (13, 10) in dark ink. Alice has the message M = (13, 10) and a random k = 4; Bob has the private d = 7 and the public Q = 7G = (0, 6), which goes to Alice. Alice's box encrypt(M, Q, k): C1 = kG, C2 = M + kQ, marked TODO 1, sends "C1 = ?, C2 = ?" in brown to Bob's box decrypt(C1, C2, d): M = C2 - dC1, marked TODO 2, which gives "decrypted = ?". Ready: add(P, Q), mul(k, P), neg(P), the point -P.](figure.svg)

## Goal

Write ElGamal encryption and decryption with points, and check that Bob gets M back.

## Ready for you

- `ec_elgamal.py`:
  - `add(P, Q)`: P + Q on the curve. `O = None` is the point at infinity.
  - `mul(k, P)`: k P = P + P + ... + P (k times).
  - `neg(P)`: -P, the point with the opposite y. Subtracting a point is adding its negative.
  - `G = (5, 1)`, Bob's `d = 7` and `Q = mul(d, G)`, and the message `M = (13, 10)`.
- At the end the file calls `encrypt(M, Q, 4)`, prints the ciphertext and then the result of `decrypt`.

## Steps

Write your code in place of the `TODO` comments in `ec_elgamal.py`:

1. `encrypt(M, Q, k)`: `C1 = kG` and `C2 = M + kQ`. Return both: `return C1, C2` returns a tuple, like a small struct of two points in C.
2. `decrypt(C1, C2, d)`: `S = d C1`, then `M = C2 - S`, that is `add(C2, neg(S))`. Return M.

## Expected output

Three lines: Bob's public key Q = (0, 6), the ciphertext (two points), and the decrypted point, which must be M = (13, 10) again.

<details>
<summary>Check your answer</summary>

```
Q = (0, 6)
ciphertext (C1, C2): ((3, 1), (5, 1))
decrypted: (13, 10)
```

The same numbers as on the slide "The example on our curve".

</details>

## Run

```
python3 ec_elgamal.py
```

About 7 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? In the [elliptic-curves simulator, step 1](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#1), the tab "ElGamal: encrypt a point" does the same on this curve: change M, k and d.
