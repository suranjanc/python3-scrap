#def to take input
strListToConvert=[item for item in str(input('Please provide the string to convert: '))]

#def to convert into hex
def convertToHex(strListToConvert):
    #Using LC
    strToReturn=''.join(str(hex(ord(item))[2:]+' ') for item in strListToConvert)
    return strToReturn

#main
print(convertToHex(strListToConvert))