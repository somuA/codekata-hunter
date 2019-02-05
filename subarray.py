#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      somu
#
# Created:     05-02-2019
# Copyright:   (c) somu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
n, m = map(int, input().split())
a=[]
b=[]
count=0
for i in range(0,n):
    z=input()
    a.append(z)
for i in range(0,m):
    z=input()
    b.append(z)
for i in range(0,n):
    for j in range(0,m):
        if (a[i]==b[j]):
            count=count+1
if (count==m):
    print ("YES")
else:
    print ("NO")
if __name__ == '__main__':
    main()
