n=input()
l=list(n)
lenth=len(l)
sum=0
l1=[]
for i in range(0,len(l)):
    l1.append(int(l[i]))
for i in range(0,len(l)):
    sum=sum+(l1[i]**lenth)
if sum==int(n):
    print('YES')
else:
    print('NO')
