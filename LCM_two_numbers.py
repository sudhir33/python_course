def find_lcm(a,b):
    t=2
    lcm=1
    while True:
        if a%t==0 and b%t==0: #14%2==0 and 16%2==0
            a=a//t #14
            b=b//t #16
            lcm=lcm*t #lcm=2
        else:
            t+=1
        if a<t or b<t:
            return lcm*a*b

        
a,b=map(int,input().split())
lcm=find_lcm(a,b)
print(lcm)
