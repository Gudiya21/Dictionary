dic={'c1':[10,20,30],'c2':[20,30,40],'c3':[12,34]}
for i in dic:
    for j in dic[i]:
        dic[i].clear()
print(dic)
