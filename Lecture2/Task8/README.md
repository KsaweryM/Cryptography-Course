# Task 8: why add the initial state?

`invert.py` holds one output block of a broken ChaCha20: 20 rounds, but without adding the initial state
at the end. `sub32` and `rotr32` are ready, and so is the loop that undoes the 20 rounds.

Fill in the `TODO`: write `inverse_quarter_round`, which undoes one quarter round. Then the program prints
rows 1 to 3 of the initial state: the constants and the secret key.

## Run

```
python3 invert.py
```

Python 3, no extra libraries.
