a={'v':[1,4,6,10],'v1':[1,4,12],'v11':[1,3,8]}
dic={}
for i in a.keys():
    b=[]
    for j in a[i]:
        if j%2==0:
            b.append(j)
        dic[i]=b
print(i,dic,end="")