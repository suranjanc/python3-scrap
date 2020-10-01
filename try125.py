list1=[[1,2],[3,4],[5,6]]
list1[0].append(7)
print(list1)
searchItem=5

#indexloc=[item1 for (item1, item2) in list1].index(1)
def searchForIndex(ListToSearch):
    indexToInsert=0
    for subList in ListToSearch:
        for item in subList:
            if item==searchItem:
                indexToInsert=list1.index(subList)
    return indexToInsert     


print(searchForIndex(list1))

list1[2].append(20)
print(list1)