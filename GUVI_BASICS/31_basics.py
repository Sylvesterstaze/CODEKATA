a=list(input())
E=[]
O=[]
for i in a:
    i=int(i)
    if i%2==0:
        E.append(i)
    else:
        O.append(i)
E.sort()
O.sort()
print(*E)
print(*O)