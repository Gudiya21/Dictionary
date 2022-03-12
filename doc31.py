dic={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
a=[]
for b in dic:
    a.append(dic[b])
max=0
for i in (range(len(a))):
    if a[i]>max:
        max=a[i]
max2=0
for j in range(len(a)):
    if a[j]>max2:
        if a[j]<max:
            max2=a[j]
max3=0
for k in range(len(a)):
    if a[k]<max2:
        if a[k]>max3:
            max3=a[k]
print('First maximum is:',max)
print('Second maximum is:',max2)
print('Third maximum is:',max3)

