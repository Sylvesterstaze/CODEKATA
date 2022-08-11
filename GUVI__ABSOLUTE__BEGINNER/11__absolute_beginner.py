a=int(input())
if a%100==0 and a%400==0:
    print("Y")   
if a%100!=0 and a%4==0:
    print("Y") 
else:
    print("N")