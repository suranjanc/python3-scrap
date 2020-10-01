tttList=[
  ["O", "O", "E"],
  ["X", "O", "E"],
  ["X", "X", "X"]
]

def tic_tac_toe(board):
    diag1 = [board[pos][pos] for pos in range(len(board))]
    #print(diag1)
    diag2 = get_diag2(board)	
    #print(diag2)
    hori = [row for row in board]
    #print(hori)
    vert = [[board[col_num][row_num] for col_num in range(len(board))] for row_num in range(len(board))]
    #print(vert)

    win_conditions = [diag1, diag2]
    [win_conditions.append(row) for row in hori]
    [win_conditions.append(col) for col in vert]
    #print(win_conditions)

    for win_c in win_conditions:
        winner = tuple(set(win_c))
        if len(winner) == 1:
            if winner[0] != 'E':
                return winner[0]
    return 'Draw'	
	
def get_diag2(board):
	pos1 = [b for b in range(len(board) - 1, -1, -1)]
	#print(pos1)
	pos2 = [b for b in range(len(board))]
	#print(pos2)
	return[board[p1][p2] for p1, p2 in zip(pos1, pos2)]

print('The winner is: ', tic_tac_toe(tttList))
