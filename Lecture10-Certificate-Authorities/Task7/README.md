# Task 7: did the log only grow?

## The situation

Bob's monitor watches a small Certificate Transparency log. On 10 November it saved the Signed Tree Head (`sth-old.txt`): 4 entries and their root. Entry 2 is a certificate for `bob.example` that Mallory got from "Other CA"; Bob never asked for it. Today the log has 8 entries. Log A is what an honest log shows: the 4 old entries and 4 new ones. Log B is what the log would show if Mallory made it drop entry 2. Both send a new root and a consistency proof: one hash that should turn the old root into the new one. Who is honest?

![Left: the tree that Bob's monitor saved on 10 November, 4 entries, root 0e166364; entry 2 is Mallory's certificate for bob.example. Right: log A today, 8 entries, root acbf332a; log B today, 8 entries without entry 2, root a16e803c. Question for both: old root + proof hash = new root?](figure.svg)

## Goal

Find the certificate Bob did not ask for, and catch the log that removed it.

## Ready for you

- `log.txt`, `sth-a.txt`, `proof-a.txt` (log A), `log-b.txt`, `sth-b.txt`, `proof-b.txt` (log B), `sth-old.txt`: example data made for this task.
- `merkle_ready.py` (a black box), the Merkle tree of Lecture 6 with the extra first byte of RFC 6962: `node_hash(left, right)` is the parent of two nodes, `tree_root(entries)` the root of a whole tree, `short(h)` the first 8 hex digits of a hash.
- In `check_log.py` everything is loaded: `entries_a`, `root_a`, `proof_a`, the same for `b`, and `old_root`. An entry is `bytes`; `.decode()` turns it into text.

The old log had 4 entries, a full half of the new tree of 8. So the new root must be `node_hash(old_root, proof)`, where `proof` is the root of the right half. (For other sizes a consistency proof has a few more hashes.)

## Steps

Write your code in place of the `TODO` comments in `check_log.py`. Under each `TODO` there is a line `print("not done yet: TODO n")`: replace it with your code.

1. Be Bob's monitor: in a loop over log A print every entry that contains `"| bob.example |"` and not `"| Trusty Issuing CA 1 |"` (`"x" in line` is like `strstr(line, "x") != NULL` in C).
2. Print whether `tree_root(entries_a)` equals `root_a`.
3. Print whether `node_hash(old_root, proof_a)` equals `root_a`.
4. Do steps 2 and 3 for log B.

## Expected output

Predict first: which of the two checks does log B pass?

<details>
<summary>Check your answer</summary>

```
saved root: 0e166364  log A: acbf332a  log B: a16e803c
1. not mine: 2 | 2026-11-09 | Other CA | bob.example | serial 7a:03:e6:d1:58:bc:22:94
2. root of the 8 entries of log A: True
3. log A only grew: True
4. root of the 8 entries of log B: True
   log B only grew: False
```

Log B is a correct Merkle tree of its own 8 entries, so a look at today's root alone shows nothing wrong. But it does not grow out of the root that Bob's monitor saved. No hash can repair that: to get `root_b` from `old_root`, the log would need a second preimage of SHA-256. A log signs every tree head, so the two signed roots together are proof that it cheated.

</details>

## Run

```
python3 check_log.py
```

Run it inside the `Task7` folder. About 8 minutes. Python 3, no other library, no internet.
