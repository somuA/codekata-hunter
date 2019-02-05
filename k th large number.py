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

n,k=map(int,input().split())
a=[]
a= list(map(int, input().split()))
a.sort()
a.reverse()
print (a[k-1])