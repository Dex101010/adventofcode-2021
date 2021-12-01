a=lambda b,c:sum([k<v for k,v in zip(b,b[c:])])
x=list(map(int,open("input.txt").readlines()))
print(a(x,1),a(x,3))
