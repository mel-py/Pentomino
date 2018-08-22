def get_move_score(board):
	return getHeight(board)

#gets the height of the pieces on the board
def getHeight(board):
	height = 0
	
	for i in board:
		for y in i:
			if y == 1:
				height = height + 1
				break
		
	return height