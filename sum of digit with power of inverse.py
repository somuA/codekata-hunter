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
q=1
if(r>1):

    for i in range(0,r-1):
        if (i<r):
            sum=sum+digits[i]**(q+1)
            q=q+1
    sum=sum+digits[-1]**1
else:
    sum=digits[0]**2



print (sum)

