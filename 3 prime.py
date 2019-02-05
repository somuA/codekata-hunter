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
list=[]
l3=[]
for i in range(2,n):
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           list.append(i)
z=len(list)
for i in range(0,z):
    if (list[i]%10==3):
        l3.append(list[i])
print (sum(l3))

