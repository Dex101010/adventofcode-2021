from collections import defaultdict
input=[[list(map(int,j.split(",")))for j in i[:-1].split(" -> ")] for i in open("input.txt")]
points=defaultdict(int)
for (a,b),(c,d) in input:
    x,y=a,b
    points[(x,y)]+=1
    while x!=c or y!=d:
        if b!=d:y+=[1,-1][b>d]
        if a!=c:x+=[1,-1][a>c]
        points[(x,y)]+=1
print(len([1 for point in points if points[point]>1]))
