from alice_key import n, e, d, number_to_bytes, short

message = b"Pay Bob 10 pounds. Alice"

# TODO 1: the message as one number: int.from_bytes(message, "big")
#         (the bytes read as one big-endian number, as in Lecture 3; it must be smaller than n)
m = None

# TODO 2: Alice signs with her private key: s = m^d mod n, in Python pow(m, d, n)
s = None

# TODO 3: Bob checks with Alice's public key: is s^e mod n equal to m?   pow(s, e, n) == m
check = None

# TODO 4: Mallory changes the message to b"Pay Bob 90 pounds. Alice" and keeps s.
#         Bob turns the changed message into a number (as in TODO 1) and checks it with s (as in TODO 3).
changed = b"Pay Bob 90 pounds. Alice"
check_changed = None

# TODO 5: what is inside s? Compute pow(s, e, n) and turn the number back into bytes: number_to_bytes(x)
inside = None

# The printing is ready: each line says "not done yet" until its TODO is done.
if m is None:
    print("not done yet: TODO 1")
else:
    print("m =", short(m), " smaller than n:", m < n)
if s is None:
    print("not done yet: TODO 2")
else:
    print("s =", short(s))
if check is None:
    print("not done yet: TODO 3")
else:
    print("Bob checks the message:        ", check)
if check_changed is None:
    print("not done yet: TODO 4")
else:
    print("Bob checks the changed message:", check_changed)
if inside is None:
    print("not done yet: TODO 5")
else:
    print("s^e mod n as bytes:", inside)
