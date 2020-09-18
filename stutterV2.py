#input the string 
inputStr=input('Enter the string : ')

#func to create stutter string
def createStutter(inputStr):
    stutterString = (inputStr[0:2]+".. ")*2 + inputStr
    return stutterString

#main
print(createStutter(inputStr))