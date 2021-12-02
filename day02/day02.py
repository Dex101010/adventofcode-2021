s=lambda l,v:sum([[q,0][k!=v]for (k,q) in l])
f=[(i[0],int(i[-2])) for i in open("input.txt")]
y,a=0,0
for (k,q) in f:
    y,a=[(y+q*a,a),(y,a+q*[1,-1][k=="u"])][k!="f"]
print((s(f,"d")-s(f,"u"))*s(f,"f"),s(f,"f")*y)
