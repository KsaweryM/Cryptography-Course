# Example 1: one repeated IV breaks WEP

WEP builds the RC4 key as `IV + secret key`. The IV is only 3 bytes and is sent
in the open, so after a few thousand packets the same IV comes back (the birthday
effect). Two packets with the same IV share the same keystream.

`attack.py` works on packets captured in `wep.py` (a small offline simulation; the
secret key is never used by the attack). It:

1. takes one packet whose plaintext is known (a printer status message),
2. finds another packet that used the same IV,
3. recovers the keystream from the known pair and reads the second packet.

## Run

```
python3 attack.py
```

No network, no real device: everything is simulated from a fixed seed, so you get
the same result every time. Python 3, no extra libraries.
