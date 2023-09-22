def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
    return a


a,b=map(int,input().split())
res=gcd(a,b)
print(res)
