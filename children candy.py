n=int(input())
s=0
c=1
l1=[]
l=list(map(int,input().split()))
if (l[0]>l[1]):
    l1.append(2)
else:
    l1.append(1)
for i in range(0,n):
    
    if(i>0):
        if(l[i]>l[i-1]):
            c=c+1
            l1.append(c)
        else:
            c=1
            l1.append(c)
for i in range(0,n):
    s=s+l1[i]
print(s)



