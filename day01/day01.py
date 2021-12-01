with open("input.txt","r") as r:
    print(sum([mylist[i+1]>mylist[i] for i,v in enumerate(r.readlines()[:-1])]))
