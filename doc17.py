from optparse import Values


key={}
key[5]=10
key[3]=8
key[6]=77
key[4]=23
key[2]=9
key[1]=43
# print("sorting on the basis of keys")
for i in sorted(key):
    print({i:key[i]},end=" ")