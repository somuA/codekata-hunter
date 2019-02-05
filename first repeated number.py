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
c=0
a= list(map(int, input().split()))
for i in range(0,n):
    for j in range(1,n):
        if(c==0):
            if(a[i]==a[j]):
                print (a[i])
                c=1



