a=[{'v':'s001'},{'v':'s002'},{'v1':'s001'},{'v1':'s005'},{'v11':'s005'},{'v':'s009'},{'v11':'s009'}]
b=[]
for i in range(len(a)):
    for j in (a[i]):
        b.append(a[i][j])
print(b)

