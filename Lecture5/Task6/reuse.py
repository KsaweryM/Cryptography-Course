from p256 import G, n, mul, h, sign, verify

# The console maker's PUBLIC key Q = d G. The private key d is secret.
Q = (
    0x8acf5b62eb99b27b9ed061a20d57b38634b0421252f438ed66c26ccfba9cbaf,
    0x6172d6f5b85cfa7d02e36c0f2552a2de1a587d0e037f5df31d0f33f92b5e85ac,
)

# Two signed updates. Look at r: it is the same in both, so the same k was used twice.
m1 = b'Game update 3.55, signed by the console maker'
r1, s1 = 0xa35b8338f3ace0c230b273701262dbae06143b79d770415e032162274ae1c4eb, 0xca379bba0dd209d5592b81a95fe6990033fa6bec9c85fc34762dd1fd35df9c51
m2 = b'System menu 3.55, signed by the console maker'
r2, s2 = 0xa35b8338f3ace0c230b273701262dbae06143b79d770415e032162274ae1c4eb, 0x2ea3793df38a52652c7ff32dca3388c225b7315cae9eb66342e504498fc21b7f

print("both signatures valid:", verify(m1, r1, s1, Q) and verify(m2, r2, s2, Q))
print("same r:", r1 == r2)

# s = k^-1 (h(m) + r d) mod n.  With the same k and r in both signatures:
# TODO 1: k = (h(m1) - h(m2)) * (inverse of (s1 - s2)) mod n
# TODO 2: d = (s1 * k - h(m1)) * (inverse of r1) mod n
# TODO 3: check that mul(d, G) == Q, then sign your own message with d:
#         sign(b"My homebrew game", d, some new k) and verify it with Q
