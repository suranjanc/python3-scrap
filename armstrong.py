#find the 1st 100 armstong numbers

def findArmstrong(nos):
    nosList=list(map(int, str(nos)))
    armstrongCalc=0
    for i in nosList:
        armstrongCalc=armstrongCalc+i**len(nosList)
    if armstrongCalc == int(nos):
        return True
    else: 
        return False

def checkIfArmstrong():
    inputNos=input("Enter the number to check: ")
    if (findArmstrong(inputNos)):
        print("True")
    else:
        print("False")

def listOfArmstrongs():
    checkUptoNos=int(input('Check for Armstrong upto which nos: '))
    listOfArmstrong=[]
    for i in range(1, checkUptoNos+1):
        if(findArmstrong(i)):
            listOfArmstrong.append(i)
    print(*listOfArmstrong, sep=', ')

listOfArmstrongs()




