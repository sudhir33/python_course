
def collatz_seq(num):
    #write ur code here
    s=0     # big =22  num=34
    while True:
        s+=num
        if num==1:#
            break
        if num%2==0:#  
            num=num//2
        else:
            num=num*3+1# 34  
            
    return s
        
    
num=int(input())
res=collatz_seq(num)
print(res)













