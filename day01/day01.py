a=lambda b:sum([k<v for k,v in zip(b,b[1:])])

x=[int(l) for l in open("input.txt").readlines()]

z=[p+q+r for p,q,r in zip(x,x[1:],x[2:])]
print(a(x),a(z))
