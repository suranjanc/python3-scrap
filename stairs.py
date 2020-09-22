#seek input for height of stairs
def seekInput():
    heightOfStairs=int(input('Provide the height of the stairs: '))
    return heightOfStairs 

#def to build stairs
def buildStairs(heightOfStairs):
    if heightOfStairs > 0:
        for i in range(heightOfStairs):
            print(' '*(heightOfStairs-i) + '#'*(i+1))
    else:
        heightOfStairs=abs(heightOfStairs)
        for i in range(heightOfStairs):
            print('#'*(i+1) + ' '*(heightOfStairs-i))

#main
buildStairs(seekInput())
