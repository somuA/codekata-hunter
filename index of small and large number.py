a=int(input())
b=list(input().split())
for i in range(0,len(b)):
    b[i]=int(b[i])
c=[]
d=[]
for i in range(0,len(b)):
    c.append(b[i])
b.sort()
z=b[0]
x=b[-1]
for i in range(0,len(b)):
    if z==c[i]:
        d.append(i+1)
        break
for i in range(0,len(b)):
    if x==c[i]:
        d.append(i+1)
        break
        
print(*d)
