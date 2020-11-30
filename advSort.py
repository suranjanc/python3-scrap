#Get list
nosList=[int(item) for item in input('Enter the list of numbers to sort: ').strip().split(',')]
sortedNosList=nosList.copy()
sortedNosList.sort()

#approach - sort a list, once sorted, create a new list for the item and keep adding items to that list
def sortList(passedList):
    sortedList=[]
    for i in range(len(nosList)):
        if not any(passedList[i] in sublist for sublist in sortedList):
            sortedList.append([passedList[i]])
        else:
            #indexToInsert= sortedList.index([passedList[i]])
            indexToInsert=searchSubList(sortedList,passedList[i])
            sortedList[indexToInsert].append(passedList[i])
    return sortedList

def searchSubList(listToSearch, itemToSearch):
    indexFound=0
    #any(indexFound=listToSearch.index(sublist) for  sublist in listToSearch if (item in sublist) == itemToSearch)
    for sublist in listToSearch:
        for item in sublist:
            if item == itemToSearch:
                indexFound=listToSearch.index(sublist)                    
    return indexFound

#main
print(sortList(sortedNosList))         
