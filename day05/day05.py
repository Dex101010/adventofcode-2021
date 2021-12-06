t=[[map(int,j.split(","))for j in i[:-1].split(" -> ")] for i in open("input.txt")]
q={}
f = lambda l,x,y,c,d: l+[(x,y)] if x==c and y==d else f(l+[(x,y)],[[x+1,x-1][x>c],x][x==c],[[y+1,y-1][y>d],y][y==d],c,d)
for i in sum(map(lambda x:f([],*x[0],*x[1]),t),[]):
    q[i]=q[i]+1 if i in q else 1
print(len([1 for p in q if q[p]>1]))
