a=input()
b=input()
l=[]
for i in range(0,len(b)):
    if ord(a[i])+ord(b[i])-96<=122:
        l.append(ord(a[i])+ord(b[i])-96)
    else:
        l.append(ord(a[i])+ord(b[i])-122)
for i in range(0,len(b)):
    print(chr(l[i]), end='')
