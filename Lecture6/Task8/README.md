# Task 8: logins with a hash chain

## The situation

Alice logs in to Bob's server with one-time passwords made from a hash chain. Her phone keeps a secret seed x0. When she signed up, the phone computed x1 = H(x0), x2 = H(x1), ..., x100 and gave the server only x100. To log in, the phone sends the value one step down the chain (first x99, then x98, ...). The server checks that H(what arrived) equals what it stored, and if so, it stores the new value. Eve listens to the network, and Mallory sends logins of her own. Five logins arrived: which ones does the server accept?

![Alice in indigo with an amber seed x0 and a chain of brown values x0, x1, x2, ..., x99, x100 linked by arrows H. Bob's server in teal stores x100. Below, five login values arrive one after another, each with "OK or REJECTED = ?". Eve in pink listens on the network.](figure.svg)

## Goal

Build the chain from the seed, then play the server: accept or reject each login and update what it stores.

## Ready for you

- `chain_login.py`: `ALICE_SEED` (16 bytes), `SERVER_STORED` (x100, 32 bytes), `LOGINS` (five values in hex), and `H(x)`, the SHA-256 of x as 32 bytes.

## Steps

1. Alice's phone: `x = ALICE_SEED`, then 100 times `x = H(x)`. The program compares the result with the server's value.
2. The server: start with `stored = SERVER_STORED`. For each login, numbered from 1: `value = bytes.fromhex(login)` (hex digits to bytes); if `H(value) == stored`, print `login n: OK` and set `stored = value`; otherwise print `login n: REJECTED`.

Then look at the five values: which rejected login is something Eve heard before, and which is made up?

## Expected output

The chain from the seed matches the server's x100, then one line per login.

<details>
<summary>Check your answer</summary>

```
x100 from the seed: 48e65d057174a2b686556baa3467311b14d7a1348d1a55693b7ff3243afddce1
the same as on the server: True
login 1: OK
login 2: OK
login 3: REJECTED
login 4: REJECTED
login 5: OK
```

Logins 1, 2 and 5 are x99, x98 and x97. Login 3 is x98 again: Eve heard login 2 and replayed it, but the server already moved on to x98, and H(x98) is not x98. Login 4 is Mallory's made-up value. To log in, Eve would need x97 from x98, that is, a preimage of SHA-256. Login 5 is accepted even though login 4 was rejected: the server keeps waiting for x97.

</details>

## Run

```
python3 chain_login.py
```

About 9 minutes. Python 3.8 or newer, no extra libraries.
