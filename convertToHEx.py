#def to take input
strListToConvert=[item for item in str(input('Please provide the string to convert: '))]
#print(strListToConvert)

#def to convert into hex
def convertToHex(strListToConvert):
    #Using for
    '''strToReturn=''
    for item in strListToConvert:
        strToReturn=strToReturn+ hex(ord(item))'''

    #Using LC
    strToReturn=''.join(str(hex(ord(item))[2:]+' ') for item in strListToConvert)

    return strToReturn

#main
print(convertToHex(strListToConvert))