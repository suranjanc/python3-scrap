#this sorts a list of integers

#input ints separated by ','
listToSort= [int(item) for item in input('Enter the numbers that you: ').strip().split(',')]
print(listToSort)
sortedlist=listToSort.copy()
sortedlist.sort()
print(sortedlist)