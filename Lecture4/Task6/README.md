# Task 6: k used twice

`reuse.py` holds two ElGamal ciphertexts for Bartek that were made with the same k, so their C1 is the same.
You know the first message. Fill in the `TODO`s and recover the second message without Bartek's private key:

1. The hidden mask y^k: C2_first = M_first · y^k mod P, so y^k = C2_first · (inverse of M_first) mod P.
2. The second message: M_second = C2_second · (inverse of y^k) mod P.
3. Print it as text: `number_to_text(M_second)`.

## Run

```
python3 reuse.py
```

Python 3.8 or newer, no extra libraries.
