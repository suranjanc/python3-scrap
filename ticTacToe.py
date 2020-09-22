tttList=[
  ["O", "O", "X"],
  ["O", "X",  "O"],
  ["X", "X",  "X"]
]

def tttWinner(tttList):
    countX=0
    countO=0
    victory=0
    for rows in range(len(tttList)):
        for cols in range(len(tttList)):
            if  tttList[rows][cols]=='X':
                countX+=1
            else:
                countO+=1
            if countX==3 or countO == 3:
                    break
        if countX==3 or countO == 3:
            victory+=1
            break
        else:
            countO=0
            countX=0
    if victory==1:
        [print('The victor is: O') if countO==3 else print('The victor is: X')]
    else:
        print('No winners here')

tttWinner(tttList)