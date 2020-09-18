#input nos using list comprehension
nosList=[int(item) for item in (input("Please enter the numbers : ").strip().split(','))]

#create func for finding unique nos
def findUniqueNos(listOfNos):
    uniqueSet=set(listOfNos)
    uniqueListOfNos=list(uniqueSet) 
    return(uniqueListOfNos)

#Main, call func
print(findUniqueNos(nosList))