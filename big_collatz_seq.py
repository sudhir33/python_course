
def collatz_seq(num):
    #write ur code here
    big=num     # big =22  num=34
    while True:
        if num>big:#   34>22
            big=num#    big=34
        if num==1:#
            break
        if num%2==0:#  
            num=num//2
        else:
            num=num*3+1# 34  
            
    return big
        
    
num=int(input())
res=collatz_seq(num)
print(res)













