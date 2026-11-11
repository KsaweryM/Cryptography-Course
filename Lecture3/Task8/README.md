# Task 8: which one is genuine?

Two money orders arrived, each with an RSA signature. `verify.py` holds the bank's public key.
Fill in the `TODO` in `verify`: a signature S is genuine if S^e mod n equals the message as a number.
Which order really comes from the bank?

## Run

```
python3 verify.py
```

Python 3, no extra libraries.
