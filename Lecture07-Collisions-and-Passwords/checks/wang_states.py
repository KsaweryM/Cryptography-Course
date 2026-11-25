# Lecture 7: the state of MD5 after each block of Wang's pair (slide "Wang's collision: two blocks").
# Run from Lecture07-Collisions-and-Passwords/: python3 checks/wang_states.py
import struct, math, hashlib
S=[7,12,17,22]*4+[5,9,14,20]*4+[4,11,16,23]*4+[6,10,15,21]*4
K=[int(abs(math.sin(i+1))*2**32)&0xffffffff for i in range(64)]
def comp(st,blk):
    X=struct.unpack('<16I',blk); a,b,c,d=st
    for i in range(64):
        if i<16: f=(b&c)|(~b&d); g=i
        elif i<32: f=(d&b)|(~d&c); g=(5*i+1)%16
        elif i<48: f=b^c^d; g=(3*i+5)%16
        else: f=c^(b|~d); g=(7*i)%16
        f&=0xffffffff; t=d; d=c; c=b
        x=(a+f+K[i]+X[g])&0xffffffff
        b=(b+(((x<<S[i])|(x>>(32-S[i])))&0xffffffff))&0xffffffff; a=t
    return [(st[0]+a)&0xffffffff,(st[1]+b)&0xffffffff,(st[2]+c)&0xffffffff,(st[3]+d)&0xffffffff]
h=lambda st: struct.pack('<4I',*st).hex()
A=open('Task4/md5_a.bin','rb').read()
B=open('Task4/md5_b.bin','rb').read()
IV=[0x67452301,0xefcdab89,0x98badcfe,0x10325476]
for M in (A,B):
    s1=comp(IV,M[:64]); s2=comp(s1,M[64:128]); print(h(IV), h(s1), h(s2))
a1=comp(IV,A[:64]);b1=comp(IV,B[:64])
print('xor words after block1', [hex(x^y) for x,y in zip(a1,b1)])
print('diff bytes block1', [i for i in range(64) if A[i]!=B[i]], 'block2', [i for i in range(64,128) if A[i]!=B[i]])
print(hashlib.md5(A).hexdigest())
