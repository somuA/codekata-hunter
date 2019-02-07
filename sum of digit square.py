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
sum=0
digits = [int(x) for x in str(n)]
r=len(digits)
for i in range(0,r):
    sum=sum+digits[i]**2
print (sum)

