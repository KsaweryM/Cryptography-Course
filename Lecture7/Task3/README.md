# Task 3: two contracts, one fingerprint

## The situation

Mallory sells her bike to Alice. The notary Carol keeps only a **fingerprint** of every contract: the first 32 bits of its SHA-256. Mallory wants two contracts with the same fingerprint: a fair one (100 pounds), which Alice will accept and Carol will register, and an unfair one (1000 pounds), which Mallory will show later. She cannot change the words, but she can put one or two spaces in every gap between words: nobody notices, and every variant has a different fingerprint.

![Left: the FAIR contract with the price 100 pounds, 2^16 variants. Right: the UNFAIR contract with 1000 pounds, up to 2^24 variants. Every gap between words: one space or two. Both go into "fingerprint: first 32 bits of SHA-256", which must give the same 32 bits = ?. Carol keeps only these 32 bits. Mallory asks: fair number = ?, unfair number = ?](figure.svg)

## Goal

Find a fair variant and an unfair variant with the same fingerprint, and see how few digests it takes.

## Ready for you

- `contracts.py`: `FAIR` and `UNFAIR` (the lines of the two contracts), `variant(lines, number)` (the contract as bytes; bit k of `number` says if gap k gets two spaces), `fingerprint(data)` (the first 32 bits of SHA-256 as a whole number), `FAIR_BITS = 16`, `UNFAIR_BITS = 24`.
- `two_contracts.py`: the start and the printing at the end.
- `table = {}` is a Python dictionary, a hash table as in C: `table[key] = value` stores, `key in table` checks in one step, `table[key]` reads.

## Steps

Write your code in `two_contracts.py`, in place of the `TODO` comments:

1. Make the table of the fair variants: for every `number` in `range(2 ** FAIR_BITS)`, store `table[fingerprint(variant(FAIR, number))] = number`.
2. Try the unfair variants one by one, `number` from 0 up: count each try in `unfair_tries`; if `fingerprint(variant(UNFAIR, number))` is a key in `table`, keep `fair_number = table[...]` and `unfair_number = number`, and stop with `break`.
3. Print the fingerprint of both contracts in hex (`f"{fingerprint(a):08x}"`), then the full SHA-256 of both (`hashlib.sha256(a).hexdigest()`).

<details>
<summary>Hint: why the table</summary>

Each unfair variant is compared with all 65 536 fair fingerprints at once, in one dictionary lookup. That is the birthday trick with two piles: about 2^16 + 2^16 digests instead of 2^32.

</details>

## Expected output

The two numbers, both contracts as text, their fingerprints and their full SHA-256.

<details>
<summary>Check your answer</summary>

```
fair variant 37733 and unfair variant 32953, after 32954 unfair tries
Contract
Mallory  sells her  bike to Alice.
The  price  is 100  pounds.
...
fingerprint of fair:   af00d510
fingerprint of unfair: af00d510
SHA-256 of fair:   af00d510b68f47f98949f2c710648b9fa1ee8b60b97ddae51c2ee2e38430c9a3
SHA-256 of unfair: af00d510ed6672af8158c778e4abf9c73acb6f8f221ea6599c4760ce0e26963c
```

65 536 + 32 954 digests, about 98 500, were enough. To match the fingerprint of one **given** contract Mallory would need about 2^32, over 4 billion. The full SHA-256 digests differ: Carol should keep the whole digest.

</details>

## Run

```
python3 two_contracts.py
```

About 10 minutes. Python 3.8 or newer, no extra libraries; the program runs about 1.5 seconds.
