a=lambda b,c:sum([k<v for k,v in zip(b,b[c:])])
x=list(map(int,open("input.txt").readlines()))
print(a(x,1),a(x,3))

#deobfuscated below
def calculate_function(list,offset):
    sum=0
    for left,right in zip(list,list[offset:]):
        if left<right:
            sum+=1
    return sum

with open("input.txt") as f:
    listOfValues=[]
    for line in f.readlines():
        listOfValues.append(int(line))
print(calculate_function(listOfValues,1),calculate_function(listOfValues,3))
