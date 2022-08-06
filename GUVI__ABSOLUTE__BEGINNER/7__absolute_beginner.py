a=int(input())
if a > 0 and a <= 12:
    if a == 2:
        print("28")
    elif a%2==0: 
        print("30")
    else:
        print("31")    
else:
    print("Error")