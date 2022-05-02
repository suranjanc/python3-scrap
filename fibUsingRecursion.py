listOfFib=[]

# use recursion to add items to a list
def createFib(nos):
    if nos==0:
        return listOfFib 
    else:
        listOfFib.append(nos)

print(createFib(100))