#get the input values into a list
prisonList=[int(item) for item in str(input('Enter the list: ')).strip().split(',')]

#func to calc prisoners released
def relPrisoners(prisonList):
    countRelPrisoners=0
    for index in range(len(prisonList)):
        if prisonList[index]==1:
            countRelPrisoners=countRelPrisoners+1
            #print('test for 1, & index is: ', index)
            prisonList=toggleList(prisonList)
    print('Total numbers of prisoners released: ', countRelPrisoners)


#def to toggle list
def toggleList(listToToggle):
    toggledList=[1 if item==0 else 0 for item in listToToggle]
    return toggledList

#main
relPrisoners(prisonList)