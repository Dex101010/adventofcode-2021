with open("input.txt","r") as r:
    mylist=[int(x.rstrip("\n")) for x in r.readlines()]  
    print(sum([mylist[i+1]>mylist[i] for i in range(len(mylist[:-1]))]))
