a=int(input("how many want!:"))
b={}
for i in range(a):
    c=input("emter your key")
    d=int(input("enter your value"))
    b.update({c:d})
print(b)