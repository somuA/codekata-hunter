a=input()
b=input()
l=list(a.split(b))
l1=l[0]
l2=list(l1)
if len(a)==len(l2):
    print(-1)
else:
    print(len(l2))
