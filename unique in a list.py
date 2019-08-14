a=input()
n1=list(map(int,input().split()))
n2=[]
n3=[]
for i in n1:
    if i not in n2:
        n2.append(i)
    else:
        n3.append(i)
for i in n2:
    if i not in n3:
        print(i)
