dic={'Alex':['sub1','sub2','sub3'],'David':['sub1','sub2']}
count=0
for i in dic:
    for j in dic[i]:
        count+=1
print(count)