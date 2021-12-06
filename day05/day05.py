from collections import defaultdict
import time
start_time = time.time()

with open("input.txt","r") as f:
    input = f.readlines()
input=[[list(map(int,j.split(",")))for j in i[:-1].split(" -> ")] for i in input]


def get_points_between(a,b):
    ret=[]
    if a[0]==b[0]:
        for y in range(min(a[1],b[1]),max(a[1],b[1])+1):
            ret.append((a[0],y))
    elif a[1]==b[1]:
        for x in range(min(a[0],b[0]),max(a[0],b[0])+1):
            ret.append((x,a[1]))
    else:
        pass
    return ret

points=defaultdict(int)
count = 0
for pair in input:
    for point in get_points_between(pair[0],pair[1]):
        points[point]+=1
        if points[point]==2:
            count+=1
print(count)
print("--- %s seconds ---" % (time.time() - start_time))
