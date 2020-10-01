[-1, 3, 5, 0, 1]

import json

def solution(i):
    startNos=i
    primeNos='2357111317192329...'
    if (startNos>=0 and startNos<=10000):
        #file open to store/check past IDs
        fileRHandler=open(__file__, 'r')
        linesInFile=fileRHandler.read().split('\n')
        pastIndexes=json.loads(linesInFile[0]) 
        fileRHandler.close()

        if startNos not in pastIndexes:
            chosenStr=primeNos[startNos:startNos+5]
            pastIndexes.append(startNos)
            #file open to write updated IDs
            fileWHandler=open(__file__,'w')
            fileWHandler.write('\n'.join([str(pastIndexes)]+linesInFile[1:]))
            fileWHandler.close()
            return(chosenStr)
        else:
            return 'That minion ID is already taken!'
    else:
        return 'Invalid minion!'


