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

    