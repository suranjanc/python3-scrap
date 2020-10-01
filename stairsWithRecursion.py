#def to get input
heightOfStairs=int(input('Provide the height of the staircase: '))

#def to build stairs using recursion
def buildStairs(heightOfStairs):
    while heightOfStairs>0:
        buildStairs(heightOfStairs-1)
    


#main