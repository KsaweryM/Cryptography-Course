# Example 2: the WEP key leaks

WEP's RC4 key is `IV + secret key`, and the IV is public. For some "weak" IVs of
the form `(A+3, 255, X)`, the first keystream byte gives away the next secret key
byte about 5% of the time (Fluhrer, Mantin, Shamir, 2001). One packet says almost
nothing; thousands of packets vote, and the right byte wins.

`attack.py` works on packets captured in `wep.py` (offline, fixed seed). For each
key byte it:

1. takes every packet with a weak IV for that position,
2. computes the first keystream byte (first ciphertext byte XOR 0xAA),
3. calls the ready `fms_guess` (in `fms.py`) and counts the votes,
4. keeps the most common value, then moves to the next byte.

At the end it prints the recovered key next to the real one.

## Run

```
python3 attack.py
```

No network, no real device: everything is simulated. Python 3, no extra libraries.
