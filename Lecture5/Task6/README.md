# Task 6: the same k twice

`p256.py` is ready: ECDSA on the curve P-256. `reuse.py` holds a console maker's public key and two signed updates
that use the same k (their r is the same). Fill in the `TODO`s:

1. Compute k from the two signatures.
2. Compute the private key d.
3. Check d against the public key, then sign your own "game" so that the console would accept it.

## Run

```
python3 reuse.py
```

Python 3.8 or newer, no extra libraries.
