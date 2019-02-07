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
b=[]

digits = [int(x) for x in str(n)]
r=len(digits)
for i in range(0,r):
    su=1
    for j in range(1,digits[i]):
        su=su+(j+1)
    b.append(su)
print(sum(b))
