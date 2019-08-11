n2=input()
a=n2.count('.')
b=n2.count('@')
n=list(n2.split('@'))
n1=n[1].split('.')
if len(n[0])>=3 and n1[1]=='com' and len(n1[0])<6 and b==1 and a==1 :
    print('YES')
else:
    print("NO")
