"""Prints the values of Task 9 (the Merkle tree of Alice's release): the root, the levels and Bob's proof.
Run from Lecture06-Hash-Functions: python3 checks/make_task9.py. The files in Task9/release are fixed;
if you change them, copy the new ROOT and PROOF into Task9/merkle.py, the README and the slides."""
import hashlib

NAMES = ["README.txt", "editor.py", "fonts.dat", "icons.dat", "plugins.py", "spell-en.dat", "spell-pl.dat", "LICENSE.txt"]


def H(b):
    return hashlib.sha256(b).digest()


level = []
for n in NAMES:
    level.append(H(open("Task9/release/" + n, "rb").read()))
levels = [level]
while len(level) > 1:
    nxt = []
    for i in range(0, len(level), 2):
        nxt.append(H(level[i] + level[i + 1]))
    level = nxt
    levels.append(level)
for k in range(len(levels)):
    print("level", k, [x.hex()[:8] for x in levels[k]])
print("ROOT =", levels[-1][0].hex())
# the proof of leaf 5 (spell-en.dat): the sibling on every level, and on which side it is
idx = 5
for k in range(3):
    sib = idx ^ 1
    side = "left" if sib < idx else "right"
    print('    ("%s", "%s"),' % (side, levels[k][sib].hex()))
    idx //= 2
m = H(open("Task9/mirror-spell-en.dat", "rb").read())
print("mirror leaf", m.hex()[:8])
