a={'a':5,'b':14,'c':32,'d':35,'e':24,'f':100,'g':57,'h':8,'i':100}
l=[]
for i in a:
    if a[i]==100:
        l.append(i)
print(l)