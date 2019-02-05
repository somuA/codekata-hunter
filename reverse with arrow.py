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

n=int(input())
a=[]
b=[]
a= list(map(int, input().split()))
a.reverse()
for i in range(0,n):
    b.append(a[i])
    b.append("->")
print(''.join(map(str, b)))