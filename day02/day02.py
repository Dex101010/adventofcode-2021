f=[(i[0],int(i[-2])) for i in open("input.txt")]
h,y,d,a=[0]*4
for (k,q) in f:
    h,y,d,a=[(h+q,y+q*a,d,a),[(h,y,d+q,a+q),(h,y,d-q,a-q)][k=="u"]][k!="f"]
print(h*d,y*h)
