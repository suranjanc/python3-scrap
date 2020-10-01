tttList=[
  ["O", "O", "X"],
  ["X", "X", "E"],
  ["X", "X", "O"]
]

'''
def tic_tac_toe(board):
    for p in "XO":
        print(p)
        for i in range(3):
		    if all(p == board[i][j] for j in range(3)) or all(p== board[j][i] for j in range(3)):
			    return p
        if all(p == board[i][i] for i in range(3)) or all(p==board[2-i][2-i] for i in range(3)):
            return p
	return "Draw"
'''

def tic_tac_toe(board):
    for p in "XO":
        for i in range(3):
            if all(p == board[i][j] for j in range(3)) or all(p== board[j][i] for j in range(3)):
                return p
        #for i in range(3):
        #    print(board[2-i][2-i]) 
        if all(p == board[i][i] for i in range(3)) or all(p == board[2-i][i] for i in range(3)):
            return p
    return 'Draw'

print(tic_tac_toe(tttList))


         


