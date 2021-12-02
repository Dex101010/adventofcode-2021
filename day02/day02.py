h,y,d,a=[0]*4
for (k,q) in [(i[0],int(i[-2])) for i in open("input.txt")]:
    h,y,d,a={"u":(h,y,d-q,a-q),"d":(h,y,d+q,a+q),"f":(h+q,y+q*a,d,a)}[k]
print(h*d,y*h)


#h is horizontal distance
#d is depth used in p1
#y is the depth for p2
#a is the aim for p2
