a=input()
l=list(a)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(*l2,sep='')
