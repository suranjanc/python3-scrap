def checkPrime(nos):
    listOfNos=[]
    for i in range(nos):
        if (nos % (i + 1)) == 0:
            listOfNos.append(i+1)
    if len(listOfNos) == 2:
        print ("Its prime")
    else: 
        print ("its not!")

checkPrime(7)