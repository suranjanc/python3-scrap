#get the input values into a list
prisonList=[int(item) for item in str(input('Enter the list: ')).strip().split(',')]
#print(prisonList)


#func to calc prisoners released
def relPrisoners(prisonList):
    # maintain listIndex; if list[index]== then release prisoner; add to count; toggle list; recurse until end of list
    countRelPrisoners=0
    #prisonListIndex=0
    #for 
    for index in range(len(prisonList)):
        if prisonList[index]==1:
            countRelPrisoners=countRelPrisoners+1
            print('test for 1, & index is: ', index)
            #prisonListIndex=index
            prisonList=toggleList(prisonList)
            #break
        #else: 
        #    print('test for 1')
    print('Total numbers of prisoners released: ', countRelPrisoners)


#def to toggle list
def toggleList(listToToggle):
    toggledList=[1 if item==0 else 0 for item in listToToggle]
    return toggledList

#main
relPrisoners(prisonList)