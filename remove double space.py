n=list(input().split(' '))
for i in n:
    if i=='':
        n.remove(i)
print(*n,sep=" ")
