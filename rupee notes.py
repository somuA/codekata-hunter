n=int(input())
c=0
c=c+(n//1000)
t1=n%1000
c=c+(t1//500)
t2=t1%500
c=c+(t2//100)
t3=t2%100
c=c+(t3//50)
t4=t3%50
c=c+(t4//10)
t5=t4%10
c=c+(t5//1)
print(c)
