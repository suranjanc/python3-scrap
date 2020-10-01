def solution(i):
    startNos=i
    primeNos='2357111317192329...'
    if startNos in range(10001):
    #if (startNos>=0 and startNos<=10000):
        chosenStr=primeNos[startNos:startNos+5]
        return chosenStr
    else:
        return 'Invalid minion!'


