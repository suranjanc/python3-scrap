#Get list
nosList=[int(item) for item in input('Enter the list of numbers to sort: ').strip().split(',')]
sortedNosList=nosList.copy()
sortedNosList.sort()

#approach - sort a list, once sorted, create a new list for the item and keep adding items to that list
def sortList(listToBeSorted):
    sortedList=[]
    for i in range(len(nosList)):
        if not any(listToBeSorted[i] in sublist for sublist in sortedList):
            sortedList.append([listToBeSorted[i]])
        else:
            #indexToInsert= sortedList.index([listToBeSorted[i]])
            indexToInsert=searchSubList(sortedList,listToBeSorted[i])
            sortedList[indexToInsert].append(listToBeSorted[i])
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
