# Checks behind the numbers on the slides

Not for students. These scripts reproduce the measurements shown on the slides.

- `bias_10M.c`: slide "Solution: the second byte". 10 000 000 random 16-byte keys, how often the first three
  keystream bytes are 0. `gcc -O2 bias_10M.c -o bias && ./bias` (about 5 s).
- `recover_byte.py`: slide "Try it: recover a byte". 100 000 keys, secret second byte 0x61, the most common
  values of the second ciphertext byte. `python3 recover_byte.py` (seed 2026, about 4 s).
