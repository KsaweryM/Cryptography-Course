# Task 6: Mallory's fake points

## The situation

Bob runs a server on the small curve y^2 = x^3 + 2x + 2 mod 17. He keeps one private key d for every connection: whoever sends him a point P gets an answer encrypted with a key made from the shared point d P. Bob's code never checks that P is on his curve. Mallory sends him three points that are on other curves, with another b, where each point has only a few multiples. From Bob's three answers she learns d.

![Mallory, in red, sends three fake points to Bob, in green: (3, 2), (0, 8) and (2, 3), each marked "not on Bob's curve" and "order = ?". Bob holds his private key d, shown as a locked amber box with "d = ?". For each point, Bob computes d P with add() and sends back a short reply, a fingerprint of d P. On Mallory's side: "d mod ? = ?" three times, then "d = ?". Below Bob, a dashed box TODO 4: "check: is P on y^2 = x^3 + 2x + 2?". The grid of the curve mod 17 shows Bob's 18 dots in dark ink and the three fake points as red rings between them.](figure.svg)

## Goal

Recover Bob's private key d with three fake points, then add the one check that stops the attack.

## Ready for you

- `bob_server.py` (you do not need to read it; as Mallory you could not):
  - `bob_reply(P)`: Bob computes S = d P and answers with `key_check(S)`.
  - `key_check(S)`: a short fingerprint of a point (the first 8 bytes of SHA-256). It stands for Bob's encrypted answer: Mallory can make the same fingerprint for any point she guesses.
  - `is_bob_secret(d)`: only to check your answer at the end.
- `fake_points.py`:
  - `add(P, Q)` and `mul(k, P)`, the same as Bob's. `O = None` is the point at infinity; `mul(0, P)` is `O`.
  - `FAKE`: Mallory's three points. `bob_receives(P)`: Bob's front door, it passes P to Bob unless `on_curve(P)` is `False`.
- The printing at the end: each line says `not done yet: TODO n` until its TODO is done. The tests use the example of the slides.

## Steps

Write your code in place of the `return None` after each `TODO` in `fake_points.py`:

1. `order(P)`: start with `R = P` and `n = 1`; while `R is not O`, add P to R and add 1 to n. Return n. This is the loop of Task 3, on another curve: `add` works there too, because it never uses b. Predict first: how many multiples will a fake point have, compared with the 19 of G?
2. `piece(P, n, reply)`: Bob's point d P is one of the n points `mul(0, P)`, `mul(1, P)`, ..., `mul(n - 1, P)`. Loop over j, and when `key_check(mul(j, P)) == reply`, return j: that is d mod n.
3. `combine(pieces)`: `pieces` is a list of pairs `(n, r)`. First multiply all n (the product). Then try every d from 1 to the product and return the first one with `d % n == r` for every pair: two nested `for` loops with an index, as in C.
4. Now you are Bob's programmer. `on_curve(P)`: return `False` for `O`, otherwise whether `(y * y - (x * x * x + a * x + b)) % p == 0`. Run again: Bob refuses every fake point, and still answers a point of his curve.

## Expected output

Until TODO 4 the attack works; after it, Bob refuses the fake points.

<details>
<summary>Check your answer</summary>

After TODO 1 to 3:

```
not done yet: TODO 4 (until then Bob accepts every point)
Mallory sends (3, 2): order 3, Bob's reply 36982eb65d45edb1, d mod 3 = 2
Mallory sends (0, 8): order 4, Bob's reply 870832a6e38931f2, d mod 4 = 1
Mallory sends (2, 3): order 11, Bob's reply f0ef0c371acf7acd, d mod 11 = 6
Bob's private key: d = 17, correct: True
```

After TODO 4:

```
Mallory sends (3, 2): Bob refuses it, not on the curve
Mallory sends (0, 8): Bob refuses it, not on the curve
Mallory sends (2, 3): Bob refuses it, not on the curve
Mallory learned nothing about d
Bob still answers a point of the curve: True
```

Three questions with 3, 4 and 11 possible answers give d mod 3 · 4 · 11 = d mod 132, and Bob's d is smaller than 19, so it is unique. On a curve used in practice d has 256 bits, and Mallory needs more fake points, with small orders whose product has more than 256 bits; each answer still costs her only a few tries. One line of checking stops all of it.

</details>

## Run

```
python3 fake_points.py
```

About 10 minutes. Python 3, no extra libraries.

Want to see it move? The [elliptic-curves simulator, step 6](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#6) shows each fake point going round its small cycle and the candidates for d disappearing, with the numbers of the slides.
