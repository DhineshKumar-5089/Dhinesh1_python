c={"Sql","Wd","Python"}
d={"Sql","Wd","Java"}
e=c&d
print(e)
e=c|d
print(e)
e=c-d
print(e)
e=c^d
print(e)

#for clearing a duplicate value in a list.
a=[1,2,1,5,2,8]
print(set(a))

a=[1,2,1,5,2,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)        