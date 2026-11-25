# Task 7: did the log only grow?
#   sth-old.txt   the Signed Tree Head that Bob's monitor saved on 10 November (4 entries)
#   log.txt, sth-a.txt, proof-a.txt     what the log shows today to Bob: 8 entries, the root, the consistency proof
#   log-b.txt, sth-b.txt, proof-b.txt   what it would show after Mallory made it drop entry 2
# merkle_ready.py is ready: node_hash, tree_root, load_log, load_sth, load_hash, short.
# Under each TODO there is a line print("not done yet: TODO n"): replace it with your code.
from merkle_ready import node_hash, tree_root, load_log, load_sth, load_hash, short

old_size, old_root = load_sth("sth-old.txt")
entries_a = load_log("log.txt")
size_a, root_a = load_sth("sth-a.txt")
proof_a = load_hash("proof-a.txt")
entries_b = load_log("log-b.txt")
size_b, root_b = load_sth("sth-b.txt")
proof_b = load_hash("proof-b.txt")
print("saved root:", short(old_root), " log A:", short(root_a), " log B:", short(root_b))

# TODO 1: be Bob's monitor: print every entry of log A for bob.example that does not come from "Trusty Issuing CA 1"
print("not done yet: TODO 1")

# TODO 2: is the root of log A really the root of its 8 entries? Print tree_root(entries_a) == root_a
print("not done yet: TODO 2")

# TODO 3: the consistency proof of log A: print whether node_hash(old_root, proof_a) equals root_a
print("not done yet: TODO 3")

# TODO 4: the same two checks for log B
print("not done yet: TODO 4")
