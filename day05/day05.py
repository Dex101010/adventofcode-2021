from collections import defaultdict
input=[[map(int,j.split(","))for j in i[:-1].split(" -> ")] for i in open("input.txt")]
points=defaultdict(int)

my_func = lambda l,x,y,c,d: l+[(x,y)] if x==c and y==d else my_func(l+[(x,y)],[[x+1,x-1][x>c],x][x==c],[[y+1,y-1][y>d],y][y==d],c,d)
ret=[my_func([],*a,*b) for a,b in input]
for item in ret:
    for thing in item:
        points[thing]+=1
print(len([1 for point in points if points[point]>1]))
