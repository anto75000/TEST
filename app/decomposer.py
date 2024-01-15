from decomposer import decomposer

def decomposer(n):
    u=n%10
    d=int(n/10)%10
    c=int(n/100)%10
    rep=(c,d,u)
    return rep