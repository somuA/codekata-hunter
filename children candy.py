n=int(input())
s=0
l1=[]
c=1
l1.append(c)
l=list(map(int,input().split()))
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


