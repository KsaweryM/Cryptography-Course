# Task 4: be Mallory

`network.py` simulates Alice and Bob doing a Diffie-Hellman exchange and then sending one encrypted message.
Every value goes through Mallory, who sits on the cable. Do not change `network.py`.

Fill in the three `TODO`s in `mitm.py`:

1. Replace Alice's A with Mallory's own value, and keep the key Mallory now shares with Alice.
2. Do the same with Bob's B.
3. Read Alice's message, then pass it on to Bob so that he notices nothing.

## Run

```
python3 mitm.py
```

Python 3, no extra libraries.
