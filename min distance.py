n=input()
list1=list(map(int,input().split()))
a,b=map(int,input().split())
c=abs(list1[a-1]-list1[b-1])
print(c)
