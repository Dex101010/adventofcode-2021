a=lambda l,v:sum([int(i[-2]) if i[0]==v else 0 for i in l])
f=open("input.txt").readlines()
print((a(f,"d")-a(f,"u"))*a(f,"f"))

x,y,d = 0,0,0
for l in f:
    b=int(l[-2])
    x,y,d=[(x+b,y+b*d,d),(x,y,d+b*[1,-1][l[0]=="u"])][l[0]!="f"]
print(x*y)
