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
a= list(str(n))
a = list(map(int, a))
s=[]
for i in a:
    s.append(i**2)
e=sum(s)
print(e)