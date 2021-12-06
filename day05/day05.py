from collections import defaultdict
import time
start_time = time.time()
input=[[list(map(int,j.split(",")))for j in i[:-1].split(" -> ")] for i in open("input.txt")]
points=defaultdict(int)
for a,b in input:
    (x,y)=a
    points[(x,y)]+=1
    while not(x==b[0] and y==b[1]):
        y+=0 if a[1]==b[1] else [1,-1][a[1]>b[1]]
        x+=0 if a[0]==b[0] else [1,-1][a[0]>b[0]]
        points[(x,y)]+=1
print(len([1 for point in points if points[point]>1]))
print("--- %s seconds ---" % (time.time() - start_time))
