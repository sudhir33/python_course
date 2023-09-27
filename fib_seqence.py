"""
fib seq

10
        b
0 1 1 2 3 5
      a   c


a=b
b=c
c=a+b
"""
def fib_seq(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,b,end=" ")
        
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        


n=int(input())
fib_seq(n)


















