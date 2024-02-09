numheads=int(input("the number of heads: "))
numlegs=int(input("the number of legs: "))
def solve(numheads,numlegs):
    print("The num of chickens: ",numheads-(numlegs-numheads*2)//2,'\n',"The num of rabbits",(numlegs-numheads*2)//2)
solve(numlegs,numheads)