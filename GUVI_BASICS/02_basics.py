num=int(input())
count=0
for a in range(2,num):
    if num%a==0:
        count+=1
if count>=1:
    print("yes")
else:
    print("no")