x=open("input.txt","r").readlines()
print(sum([int(k)<int(v) for k,v in zip(x,x[1:])]))
