a=lambda l,v:sum([[q,0][k!=v]for (k,q) in l])
f=[(i[0],int(i[-2])) for i in open("input.txt")]
y,d=0,0
for (k,q) in f:
    y,d=[(y+q*d,d),(y,d+q*[1,-1][k=="u"])][k!="f"]
print((a(f,"d")-a(f,"u"))*a(f,"f"),a(f,"f")*y)
