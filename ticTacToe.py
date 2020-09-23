tttList=[
  ["X", "O", "O"],
  ["X", "X", "O"],
  ["O", "O", "E"]
]

def tttWinner(tttList):
    winner=''
    for iterations in ['rowWise','colWise','diagnal1','diagnal2']:   
        countX=countO=0                     
        for rows in range(len(tttList)):
            for cols in range(len(tttList)):
                #which way to eval?
                if iterations=='rowWise':
                    byrows=rows
                    bycols=cols
                elif iterations=='colWise':
                    byrows=cols
                    bycols=rows
                elif iterations=='diagnal1':
                    byrows=bycols=cols
                else: 
                    byrows=2-cols
                    if byrows==2:
                        bycols=0
                    elif byrows==1:
                        bycols=1
                    else: 
                        bycols=0

                if  tttList[byrows][bycols]=='X':
                    countX+=1
                    #if iterations=='rowWise': print('In countX, Rows, cols, and value are: ', byrows, bycols, tttList[byrows][bycols])
                elif tttList[byrows][bycols]=='O':
                    countO+=1
                    #if iterations=='rowWise': print('In countO, Rows, cols, and value are: ', byrows, bycols, tttList[byrows][bycols])
                #if iterations=='diagnal2': print('countX, countO: ', countX, countO) 
                if countX==3 or countO == 3:
                    #if iterations=='rowWise':print('count x, o: ', countX, countO)
                    break
            if countX==3 or countO==3:
                break
            else:
                countO=countX=0

        #print('count x, o: ', countX, countO)
        if countX==3:
            winner='Winner is X'
            break
            #winner=True
        elif countO==3:
            winner='Winner is O'
            break
            #[(winner='Winner is X') if countO==3 else (winner='Winner is O')]
        else:
            winner='Its a draw'
            #print('Its a draw')
    
    #return winner
    print(winner)

tttWinner(tttList)