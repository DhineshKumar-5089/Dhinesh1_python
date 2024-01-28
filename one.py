'''a=int(input("Enter a value:"))
for a in range(1,11,1)
if (a % 2)==0:
    print("{0} is even".format(a))
else:
    print("{0} is odd".format(a))'''

'''for i  in range(1,6):
    print()
    print("loop begins")
    print("Outer Loop",i)
    for j in range(1,6):
        print("inner loops",j)'''

'''for i in range(1,11):
    print(i * "*")'''

'''def print_left_angled_triangle(n):
 n=int(input("enter the n value:"))
 print(n)
for i in range(1, 5+1):
        print('* ' * i)

for i in range(5, 0 - 1):
        spaces = ' ' * (5 - i)
        stars = '*' * i
        print(spaces + stars)

for i in range(1,5,1):
    for j in range(1,5,1):
        print(i-j,end=" ")
        print()
for i in range(1,6,1):
    for  j in range(6,i,-1):
        print("* ",end=" ")
    print()

for i in range(1,5,1):
    for j in range(1,i+1):
        print("* ",end=" ")
    print()'''

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")
        print()
print()