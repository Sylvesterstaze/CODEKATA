b=[]
a=list(input().split())
for i in a:
  i=int(i)
  b.append(i)
c=sum(b)
if c%2==0:
  print("even")
else:
  print("odd")