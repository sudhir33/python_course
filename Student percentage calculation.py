s1,s2,s3,s4,s5=map(int,input().split())
if (s1>=0 and s1<=100) and (s2>=0 and s2<=100) and(s3>=0 and s3<=100) and (s4>=0 and s4<=100) and(s5>=0 and s5<=100):
    print("Valid")
    if s1<35 or s2<35 or s3<35 or s4<35 or s5<35:
        print("fail")
    else:
        print("pass")
        total=s1+s2+s3+s4+s5
        per=(total*100)/500
        print(total,per)
        if per>=85:
            print("A+")
        elif per>=70:
            print("A")
        elif per>=60:
            print("B")
        elif per>=50:
            print("C")
        else:
            print("D")
        
else:
    print("Invalid marks")

"""

67 23 67 56 54



5 subs

min-0  max-100
pass-35

total
per
grade

per>=85   A+
70-84    A

60-69   B

50- 59  C
D










"""
