#def for inputs
def getString():
    strToBeConverted=input('Provide the string for which you need a mirror: ')
    return strToBeConverted

#def for mirroring
def calcMirror(strToBeConverted):
    mirrorStr=''.join(chr(ord('z') - (ord(item)-ord('a'))) for item in strToBeConverted)
    return mirrorStr

#main
print(calcMirror(getString()))
