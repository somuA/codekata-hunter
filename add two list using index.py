a=input()
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
n3=[]
for i in range(0,int(a)):
    n3.append(n1[i]+n2[i])
print(*n3,sep=' ')
