d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
a=[]
for i in range(len(d)):
    for j in d[i]:
        a.append(d[i][j])
print(a)
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
