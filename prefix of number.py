n=int(input())
list1=list(input().split())
test=input()
c=0
b=len(test)
for i in range(0,len(list1)):
    str1=list1[i]
    if str1[0:b]==test:
        c=c+1
print(c)
