a=int(input())
b=list(map(int,input().split()))
c=1
l1=[]
for i in range(0,len(b)):
    c=c*b[i]
for i in range(0,len(b)):
    l1.append(c//b[i])
print(*l1,sep=' ')
