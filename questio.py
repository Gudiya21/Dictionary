# dic={'a':8,'b':23,'c':45,'d':67,'e':55}
# i=0
# a=[]
# for b in dic:
#     a.append(dic[b])
# max=0
# min=a[i]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
#     i+=1
# print('minimum is',min)
# print('maximum is',max)



# a=[{'v':'s001'},{'v':'s002'},{'v1':'s001'},{'v1':'s005'},{'v11':'s005'},{'v':'s009'},{'v11':'s009'}]
# b=[]
# for i in range(len(a)):
#     for j in (a[i]):
#         b.append(a[i][j])
# print(b)



# a=[{'id':1,'success':'True','name':'lary'},
# {'id':2,'success':'false','name':'rabi'},
# {'id':3,'success':'true','name':'alex'}]
# sum=0
# for i in range(len(a)):
#     for j in (a[i]):
#         if 'id'==j:
#             sum+=a[i][j]
# print(sum)



# a={1:10,2:20,3:30,4:40,5:50,6:60}
# count=0
# for i,j in a.items():
#     count+=1
#     print(count,j,i)



# dict={'alex':{'class':'v','roll_id':2},'puja':{'class':'v','roll_id':3}}
# for i in dict:
#     print(i)
#     for j in dict[i]:
#         print(j,':',dict[i][j])




# dict={'x':[11,12,13,14,15,16,17,18,19],
# 'y':[21,22,23,24,25,26,27,28,29],
# 'z':[31,32,33,34,35,36,37,38,39]}
# b=[]
# for i in dict:
#     b.append(dict[i])
# print(b)
# j=0
# while j<len(b):
#     k=0
#     while k<len(b[j]):
#         if b[j][k]%5==0:
#             print(b[j][k])
#         k+=1
#     j+=1




# dic={'c1':[10,20,30],'c2':[20,30,40],'c3':[12,34]}
# for i in dic:
#     for j in dic[i]:
#         dic[i].clear()
# print(dic)



# sub={'physics':80,'math':90,'chemistry':86}
# for i in sub.keys():
#     print(i)





# dict={1:['Jean Castro'],2:['Lula Powell'],3:['Brian Howell'],4:['Lyne Foster'],5:['Zachary Simon']}
# b={}
# l=[]
# for i in dict:
#     for j in dict[i]:
#         b.update({i:j})
# l.append(b)
# print(l)


# dic={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165,'Piera Cox':190}
# dic.pop('Kierra Gentry')
# print(dic)



# dic={'a':2,'b':3,'c':7,'d':6}
# dic2={'e':6,'f':9,'g':4,'h':8}
# a={}
# for i in dic:
#     for j in dic2:
#         a[i]=dic[i]
#         a[j]=dic2[j]
# print(a)




# a={'v':[1,4,6,10],'v1':[1,4,12],'v11':[1,3,8]}
# dic={}
# for i in a.keys():
#     b=[]
#     for j in a[i]:
#         if j%2==0:
#             b.append(j)
#         dic[i]=b
# print(i,dic,end="")



# a={'v':[1,3,6],'v1':[1,5],'v11':[2,7,9]}
# b={}
# for i in a:
#     l=[]
#     for j in a[i]:
#         if j%2==0:
#             l.append(j)
#         b[i]=l
# print(i,b,end="")



# a={'a':5,'b':14,'c':32,'d':35,'e':24,'f':100,'g':57,'h':8,'i':100}
# l=[]
# for i in a:
#     if a[i]==100:
#         l.append(i)
# print(l)



# a={'a':5,'b':14,'c':32,'d':35,'e':24,'f':100,'g':57,'h':8,'i':100}
# b=[]
# for i in a:
#     if a[i]>30:
#         b.append(i)
# print(b)



# a={'x':{'a':10,'b':20,'c':45},'y':{'d':20,'e':50,'f':20}}
# sum=0
# for i in a:
#     for j in a[i]:
#         sum+=a[i][j]
# print(sum)

















