#inut the nos; assume int
#list1=[]
#inputCount=int(input("How many nos you want to enter :"))

#Input using for
'''for i in range(inputCount):
    #print(i)
    list1.append(int(input("Please enter the numbers :")))'''

#Input using list comprehension
list2=[int(item) for item in (input('Please enter the numbers :').strip().split(','))]
print(list2)


#Find items repeated, and the ones unique
def uniqueKumar(list):
    uniqueList=[]
    for item in list2:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList

print(uniqueKumar(list2))