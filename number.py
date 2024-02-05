import math
print(math.sqrt(144))
print(math.pow(2,7))
print(math.exp(0))
print(math.ceil(3.2))
print(math.floor(6.9))
print(math.fabs(-4.6))
print(max(3,2,45,65,67,98))
print(min(3,2,45,65,67,98))

#To create a count of a number using loop.

a=6745
count=0
while a!=0:
    a=a//10
    count+=1
print(count)

#using string method.

b=90909
c=str(b)
print(len(c))

#To find the value using list method indexing.
a=[1,2,3,4,[5,4,2],6,7,8]
print(a[4][1])

