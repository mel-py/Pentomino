def get_best_score(board, piece):
	best_score = 0
	best_move = 0
	for i in range(len(board[0])):
		print(i);
		#score = get_move_score(board, piece, posX)
		#if score > best_score:
		#	best_score = score
		#	best_move = i
	return best_move
	
def get_move_score(board, piece, posX):
	posY = 0
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] == 1:
				if board[posX+i][posY+j] == 1:
					return -1
				if board[posX+i][posY+j+1] == 1:
					board = place_piece(posX, j, piece, board)
					return (getHeight(board))
					
def place_piece(x, y, piece, board):
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] == 1:
				board[y+j][x+i] = 1
	return board
					
#gets the height of the pieces on the board
def getHeight(board):
	height = 0
	for i in board:
		for y in i:
			if y == 1:
				height = height + 1
				break
		
	return height