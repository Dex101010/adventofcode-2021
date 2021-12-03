f=[l[:-1]for l in open("input.txt")]
ret=""
for j in range(len(f[0])-1): 
    foo=[x[j] for x in f]
    mydict={x:foo.count(x) for x in set(foo)}
    ret+=[x for x in mydict if mydict[x]==max(mydict.values())][0]
print(int(ret,2)*int("".join([["1","0"][int(i)]for i in ret]),2))

def myfunction(alist,v):
    reverse=[0,1]if v==0 else [1,0]
    for i in range(len(alist[0])):
        mysum=sum([int(x[i]) for x in alist])
        mostCommonBit=int(mysum>=(len(alist)-mysum))
        temp=[]
        for item in alist:
            if reverse[int(item[i])==mostCommonBit]:
                temp.append(item)
        if len(temp)==1:
            return temp[0]
        alist=temp

life=myfunction(f,1)
oxy=myfunction(f,0)
print(int(life,2)*int(oxy,2))
