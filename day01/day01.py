a=lambda b,c:sum([k<v for k,v in zip(b,b[c:])])
x=list(map(int,open("input.txt").readlines()))
print(a(x,1),a(x,3))

#more verbose but readable version below

#the same function is used for part 1 and two as a+b+c<b+c+d is equivalent to a<d
#for the first problem, offset is 1, meaning neighbours are compared, whereas for the second it is 3
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
