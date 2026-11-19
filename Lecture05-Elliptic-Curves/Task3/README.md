# Task 3: all points from G

## The situation

The small curve from the slides is y^2 = x^3 + 2x + 2 mod 17, with the point G = (5, 1). On the slides you doubled G and got 2G = (6, 3); in Task 2 you added G + 2G on paper. Now Python does the arithmetic: write the point addition once, then add G again and again and watch where it goes. Sooner or later you reach O, the point at infinity.

![The curve y^2 = x^3 + 2x + 2 mod 17 as a 17 by 17 grid of grey dots with the points of the curve in dark ink. G = (5, 1), 2G = (6, 3) and 3G = (10, 6) are marked in violet, joined by arrows labelled +G; a dashed arrow goes on to "4G = ?". Next to it, the cases of add(P, Q): P is O gives Q, Q is O gives P, Q = -P gives O, all three ready; P = Q with the slope (3x1^2 + a) / (2y1), P not equal to Q with the slope (y2 - y1) / (x2 - x1), then x3 and y3 from s, marked TODO. Below: print G, 2G, 3G, ... until O, how many points? TODO.](figure.svg)

## Goal

Finish the point addition, then list G, 2G, 3G, ... until you reach O. How many points do you get?

## Ready for you

- `ec_toy.py`: the curve (`a`, `b`, `p`), the point `G` and `O = None`, the point at infinity.
- In `add(P, Q)`: the cases P + O, O + Q and P + (-P) = O. A point is a tuple `(x, y)`: `P[0]` is x, `P[1]` is y.

## Steps

Write your code in place of the `TODO` comments in `ec_toy.py`. Each `print("not done yet: ...")` line is there only so that the unchanged file says what is missing: delete it when you do its TODO (with TODO 3 also the line `add(G, G)` above it: it only calls `add()` once so that the unchanged file reports TODO 1 and 2 too).

1. The slope `s`. For doubling (`P == Q`): `s = (3 * x1 * x1 + a) / (2 * y1) mod p`; otherwise `s = (y2 - y1) / (x2 - x1) mod p`.
   - Python has no `/` modulo p: "`/ v mod p`" means "`* pow(v, -1, p)`", the modular inverse (Python 3.8 or newer). Then `% p`.
   - Write the square as `x1 * x1`. In Python `^` is XOR, as in C, not a power.
2. `x3 = s * s - x1 - x2 mod p` and `y3 = s * (x1 - x3) - y1 mod p`, then `return (x3, y3)`.
   - Python's `%` never gives a negative result: `-7 % 17` is `10`, not `-7` as in C.
3. Print G, 2G, 3G, ...: start with `k = 1` and `R = G`. While `R is not O`: `print(f"{k}G = {R}")`, then `R = add(R, G)` and `k = k + 1`. After the loop, print the last line, the point at infinity: `print(f"{k}G = O")`.
   - `f"{k}G = {R}"` is like `printf("%dG = (%d, %d)\n", k, x, y)` in C: the values in `{}` are put into the text.

## Expected output

One line per point, in exactly this format: `1G = (5, 1)`, `2G = (6, 3)`, `3G = (10, 6)` (the values from the slides and Task 2), and so on; the last line is `<k>G = O`, the point at infinity. Count the lines before O.

<details>
<summary>Check your answer</summary>

```
1G = (5, 1)
2G = (6, 3)
3G = (10, 6)
4G = (3, 1)
5G = (9, 16)
6G = (16, 13)
7G = (0, 6)
8G = (13, 7)
9G = (7, 6)
10G = (7, 11)
11G = (13, 10)
12G = (0, 11)
13G = (16, 4)
14G = (9, 1)
15G = (3, 16)
16G = (10, 11)
17G = (6, 14)
18G = (5, 16)
19G = O
```

18 different points, then O: G visits every dot of the curve. 18G = (5, 16) is -G, so 19G = G + (-G) = O.

</details>

## Run

```
python3 ec_toy.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries.

Want to see it move? In the [elliptic-curves simulator, step 4](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#4.3), "Multiples of G" adds G step by step, and [step 5](https://ksawerym.github.io/Cryptography-simulators/elliptic-curves/#5) shows one addition number by number.
