# a="MISSISSIPPI"
# b=list(a)
# i=0
# dic={}
# while i<len(b):
#     count=0
#     dic2={}
#     j=0
#     while j<len(b):
#         if b[i]==b[j]:
#             count+=1
#         j+=1
#     dic.update({b[i]:count})
#     i+=1
# print(dic)

a="MISSISSIPPI"
b=list(a)
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)