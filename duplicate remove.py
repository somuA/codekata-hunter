a=list(input().split())
b=list(input().split())
li=[]
for i in range(0,len(b)):
    if int(a[1])!=int(b[i]):
        li.append(int(b[i]))
if len(li)!=0:
    print(*li,sep=' ')
else:
    print('empty')
