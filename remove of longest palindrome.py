from itertools import combinations
x =input()
perms = []
for i in range(1, len(x)+1):
    for c in combinations(x, i):
        perms.append("".join(c))
l1=[]
l3=[]

for i in range(0,len(perms)):
    l1.append(perms[i])
for i in range(0,len(perms)):
    l2=[]
    a=l1[i]
    l2=list(a)
    if(l2 == l2[::-1]):
        l3.append(a)

print (len(x)-len(l3[-1]))
