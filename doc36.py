x={'key1':1,'key2':3,'key3':2}
y={'key1':1,'key2':2}
for i in x:
    for j in y:
        if i==j and x[i]==y[j]:
            print('key 1 is presented in x and y both')
    