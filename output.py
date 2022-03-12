# a={(1,2):1,(2,3):2}
# print(a[1,2])
# output is 1


# a={'a':1,'b':2,'c':3}
# print(a['a','b'])
# output is key error 


# fruit={}
# def addone(i):
#     if i in fruit:
#         fruit[i]+=1
#     else:
#         fruit[i]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone("Apple")
# print(len(fruit))
# print(fruit)
# output is:
# 3
# {'Apple':2,'banana':1,'apple':1}


# student={}
# age={}
# details={}
# student['name']='bikki'
# age['student age']=14
# details['student']=student
# details['age']=age
# print(len(details['student']))
# OUTPUT IS 1


# mydict={}
# mydict[(1,2,4)]=8
# mydict[(4,2,1)]=10
# mydict[(1,2)]=12
# sum=0
# for i in mydict:
#     sum+=mydict[i]
# print(sum)
# print(mydict)
# OUTPUT IS:
# {(1,2,4):8,(4,2,1):10,(1,2):12}



# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jams']=4
# crates['box']=box
# crates['jars']=jars  
# print(len(crates[box]))
# OUTPUT IS
# Typeerror:unhashable type:'dict'


# rec={'Name':'Python','Age':20,'Addr':'NJ','Country':'USA'}
# id1=id(rec)
# del rec
# rec={'Name':'Python','Age':20,'Addr':'NJ','Country':'USA'}
# id2=id(rec)
# print(id1==id2)
# OUTPUT IS:
# True