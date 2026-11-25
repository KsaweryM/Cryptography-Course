# Lecture 7: tail, loop and collision of x -> first 16 bits of SHA-256(x as 2 bytes) (slides on rho and Floyd).
import hashlib
def f(x,bits=16):
    nb=(bits+7)//8
    d=hashlib.sha256(x.to_bytes(nb,'big')).digest()
    return int.from_bytes(d[:nb],'big')>>(8*nb-bits)
def path(x0,bits=16):
    seen={};x=x0;i=0
    while x not in seen: seen[x]=i; x=f(x,bits); i+=1
    mu=seen[x]; lam=i-mu; return mu,lam
def floyd(x0,bits=16):
    t=f(x0,bits); h=f(f(x0,bits),bits); steps=1
    while t!=h: t=f(t,bits); h=f(f(h,bits),bits); steps+=1
    meet=steps
    t=x0; pt=ph=None; k=0
    while t!=h: pt,ph=t,h; t=f(t,bits); h=f(h,bits); k+=1
    return meet,k,pt,ph,t
for x0 in [0,1,2,0x2026]:
    mu,lam=path(x0); r=floyd(x0)
    print(hex(x0),'mu',mu,'lam',lam,'meet after',r[0],'second phase',r[1],'a',r[2] is not None and hex(r[2]),'b',r[3] is not None and hex(r[3]),'f',hex(r[4]))
import math; print('sqrt(pi N/2)', math.sqrt(math.pi*65536/2), 1.18*256)
# average over many starts
import random; random.seed(1); tot=[]
for _ in range(2000):
    mu,lam=path(random.randrange(65536)); tot.append(mu+lam)
tot.sort(); print('median mu+lam', tot[1000], 'mean', sum(tot)/len(tot))
