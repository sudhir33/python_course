def collatz_seq(num):
    #write ur code here
    c=0
    while True:
        c+=1
        if num==1:#
            break
        if num%2==0:#  
            num=num//2
        else:
            num=num*3+1# 34
    return c
            
    
        
    
num=int(input())
res=collatz_seq(num)
print(res)

