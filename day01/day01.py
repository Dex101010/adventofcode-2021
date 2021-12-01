a=lambda b:sum([k<v for k,v in zip(b,b[1:])])
x=map(int,open("input.txt").readlines())
z=map(sum,zip(x,x[1:],x[2:]))
print(a(list(x)),a(list(z)))
