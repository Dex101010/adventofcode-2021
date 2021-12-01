x=[int(x) for x in open("input.txt").readlines()]
print(sum([int(k)<int(v) for k,v in zip(x,x[1:])]))

#part two
q=[x+y+z for x,y,z in zip(x,x[1:],x[2:])]
print(sum([int(k)<int(v) for k,v in zip(q,q[1:])]))
