tttList=[
    ["O", "O", "E"],
    ["X", "E", "E"],
    ["X", "X", "E"]
]

#approach
#use all function to eval true is all items in a row/col are either X or O
# then do a separate one for the two dignals 

def calcTttWinner(matrix):
    for matchItem in "XO":
        for i in range(len(matrix)): 
            if all(matrix[i][j]==matchItem for j in range(len(matrix)) or all(matrix[j][i]==matchItem for j in range(len(matrix)))) or\
               all(matrix[j][j]==matchItem for j in range(len(matrix))) or all(matrix[2-j][j]==matchItem for j in range(len(matrix))):
              return matchItem
    return 'Draw'
   
value=calcTttWinner(tttList)
print('its a draw') if value=='Draw' else print('the winner is: ', value)