def solution(i):
    count=0
    strToReturn='2'
    noToTest=3
    while len(strToReturn)<i+5:
        #print(len(strToReturn))
        if isPrime(noToTest):
            count+=1
            strToReturn+=str(noToTest)
        noToTest+=2
    print(strToReturn)
    return strToReturn[i:i+5]

def isPrime(nos):
    if nos % 2 == 0:
        return False
    x = 3
    while x * x <= nos:
        if nos %x == 0 :
            return False
        x += 2
    return True

print(solution(100))