a={"id":1,"name":"Dhinesh"}
print(a["name"])
a["id"]=21
print(a)
b={"age":21,"course":"python"}
a.update(b)
print(a)
print(a.itemS())
print(a.pop("id"))
print(a)
print(a.popitem())
print(a)
print(a.clear())
print(a)
del a["name"]
print(a)