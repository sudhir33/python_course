def RP_mul(a,b):# 24  16
    res=0
    while a:#0
        if a%2==1:# 
            res=res+b# res=128+256=384
            
        a=a//2#0
        b=b*2#512
        
    return res#384


a,b=map(int,input().split())
res=RP_mul(a,b)
print(res)
