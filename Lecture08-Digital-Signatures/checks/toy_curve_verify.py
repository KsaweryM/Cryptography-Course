# The toy curve y^2 = x^3 + 2x + 2 mod 17 of Lecture 5, G = (5, 1), q = 19: the points of the slides "Why verify works: on our curve".
p=17; a=2
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    if P[0]==Q[0] and (P[1]+Q[1])%p==0: return None
    if P==Q: l=(3*P[0]*P[0]+a)*pow(2*P[1],-1,p)%p
    else: l=(Q[1]-P[1])*pow(Q[0]-P[0],-1,p)%p
    x=(l*l-P[0]-Q[0])%p; return (x,(l*(P[0]-x)-P[1])%p)
def mul(k,P):
    R=None
    for i in range(k): R=add(R,P)
    return R
G=(5,1)
for k in [1,2,7,10,14,15,19]: print(k, mul(k,G))
Q=mul(7,G); print("2Q",mul(2,Q), "15G+2Q", add(mul(15,G),mul(2,Q)))
print("13G", mul(13,G), "u1 for z=6:", 6*3%19, "18G+14G", add(mul(18,G),mul(14,G)))
