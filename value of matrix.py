a=int(input())
l1=[]
e=0
for i in range(0,a):
    s=list(map(int,input().split()))
    e=e+sum(s)
c=(e/a**2)
print('%.6f' %c)
