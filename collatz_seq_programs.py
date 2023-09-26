def collatz_seq(num):
    #write ur code here
    while True:
        print(num,end=" ")
        if num==1:#
            break
        if num%2==0:#  
            num=num//2
        else:
            num=num*3+1# 34  
            
    
        
    
num=int(input())
collatz_seq(num)

