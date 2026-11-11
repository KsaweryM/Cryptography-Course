# Task 4: be Mallory

`network.py` simulates Ania and Bartek doing a Diffie-Hellman exchange and then sending one encrypted message.
Every value goes through Mallory, who sits on the cable. Do not change `network.py`.

Fill in the three `TODO`s in `mitm.py`:

1. Replace Ania's A with Mallory's own value, and keep the key Mallory now shares with Ania.
2. Do the same with Bartek's B.
3. Read Ania's message, then pass it on to Bartek so that he notices nothing.

## Run

```
python3 mitm.py
```

Python 3, no extra libraries.
