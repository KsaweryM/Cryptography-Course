# Task 8: the same k twice

## The situation

Alice Games makes a game console. The console runs a program only if it carries a valid ECDSA signature (curve P-256, SHA-256) made with Alice Games' private key `d`; the console knows only the public key `Q = d x G`. But the signing program of Alice Games uses the same `k` every time. Mallory has two signed games and wants to run her own program on every console.

![A console that knows only Q. game_1.txt with the signature r = a7ef2367...e3800979, s1 = b109701c...737ab4af and game_2.txt with r = a7ef2367...e3800979, s2 = 76b7f5c7...34c86b4b: the same r, so the same k. Mallory computes k = ?, then d = ?, signs mallory_game.txt: console accepts?](figure.svg)

## Goal

Recover the private key `d` from the two signatures, check it against `Q`, and sign Mallory's program so that the console accepts it.

## Ready for you

- `ecdsa_ready.py`: `q` (the order of G; all ECDSA numbers are mod q), `hash_number(data)` (z: SHA-256 as a number), `public_key(d)` (the point d x G as a pair `(x, y)`), `sign(d, data)` (a new signature `(r, s)`) and `verify(Q, data, r, s)`.
- `recover_key.py`: the three files as bytes, `Q`, and the two signatures `(r1, s1)` and `(r2, s2)`.
- `pow(x, -1, q)`: the inverse of x mod q (Lecture 3). Dividing by x mod q means multiplying by `pow(x, -1, q)`.

The two formulas of ECDSA you need (slides "Inside ECDSA" and "The same k twice"): `r` is the x of k x G, and `s = (z + r d) / k mod q`.

## Steps

Write your code in place of the `None` after each `TODO` in `recover_key.py`:

1. `same_r`: before any attack, look at the two signatures: is `r1 == r2`? Equal `r` means the same `k`.
2. `z1`, `z2`: the hashes of `game_1` and `game_2` as numbers.
3. `k`: subtract the two equations for `s`; `r d` disappears. Solve for `k`, mod `q`.
4. `d`: put `k` into the equation of the first signature and solve for `d`, mod `q`.
5. `d_matches`: is `public_key(d) == Q`?
6. `mallory_valid`: sign `mallory_game` with `d` (`r, s = sign(d, mallory_game)`) and check it with `verify(Q, ...)`.

<details>
<summary>Hint for steps 3 and 4</summary>

k = (z1 - z2) / (s1 - s2) mod q, and d = (s1 k - z1) / r1 mod q. Write each division as a multiplication by `pow(..., -1, q)` and end with `% q`.

</details>

## Expected output

<details>
<summary>Check your answer</summary>

```
signature of game 1 valid: True
signature of game 2 valid: True
r1 == r2: True
z1 = 0xca3b4660cf2082827b96167343c32b9ea99a7fba27515b3dc9c1d234b3cefd2
z2 = 0xab62eabbe775ef323b410fd4fef32b791aeaf80f9a13bcaef0555a2e71036a46
k  = 0xccfc9b5a4810d39278af4285a63e384b21ceca0ae4346ae10a22902e518abbc0
d  = 0xdb8c7cb15301165917fb456dbe9f471410044244de069f55e3c64f2aa1189f1c
public_key(d) == Q: True
the console accepts Mallory's program: True
```

The same `r` in both signatures shows that `k` repeated. Two equations with the same unknown `k` give `k`, and then `d`. This is what happened to the Sony PlayStation 3 in 2010.

</details>

## Run

```
python3 recover_key.py
```

About 12 minutes. Python 3 and the library `cryptography` (used by `ecdsa_ready.py` for `sign` and `verify`).

Want to see it move? The [signatures simulator, step 5](https://ksawerym.github.io/Cryptography-simulators/signatures/#5) signs twice on the small curve of Lecture 5 with four ways of choosing k (random, repeated, k + 1, from the key and the message) and shows what Mallory can compute from each. Open it after the task.
