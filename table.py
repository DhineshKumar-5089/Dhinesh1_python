'''a=int(input("Enter a number:"))
i =1
while(i<11):
    print(a,"x",i,"=",a*i)
    i=i+1

a= int(input("enter a factorial number:"))
def factorial(a):
    if a==0:
        return 1
    else:
        return a * factorial(a-1)
print("factorial number",a,"is",factorial(a))'''

a=0
for i in range(1,11,1):
    a=a+i
print(a)
