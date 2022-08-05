a=float(input())
def findArea(r):
    if r<0:
        print("error") 
    else:
        PI = 3.1415
        c= PI * 2 *r 
        print(round(c, 2))
findArea(a)