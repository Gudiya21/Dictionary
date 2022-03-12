dic={'a':8,'b':23,'c':45,'d':67,'e':55,'f':3}
i=0
a=[]
for b in dic:
    a.append(dic[b])
max=0
min=a[i]
for i in (range(len(a))):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    i+=1
print('minimum is',min)
print('maximum is',max)
