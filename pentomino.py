import copy
from random import randint

def get_best_move(board, piece):
	best_score = 100
	best_move = 0
	for i in range(len(board[0])-len(piece)+1):
		score = get_move_score(board, piece, i)
		if score < best_score:
			best_score = score
			best_move = i
		#if two scores are equal pick one at random for more action
		if score == best_score:
			if randint(0, 1) == 1:
				best_score = score
				best_move = i
	return best_move
	
#get the move score of each possible move
def get_move_score(board, piece, posX):
	#find the y position the piece will be placed at at the current x position
	posY = 0
	while not check_collision(posX, posY+1, piece, board):
		if posY + len(piece[0]) == len(board)-1:
			break
		posY = posY + 1
	temp_board = copy.deepcopy(board) #don't want to place the piece on the actual board
	temp_board = place_piece(posX, posY, piece, temp_board)
	return getHeight(temp_board)

def check_collision(x, y, piece, board):
	for i in range(len(piece)):
		for j in range(len(piece[0])):
			if piece[i][j] == 1 and board[y+j][x+i] == 1:
				return True
	return False

def place_piece(x, y, piece, tboard):
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] == 1:
				tboard[y+j][x+i] = 1
	return tboard
				
#gets the height of the pieces on the board
def getHeight(board):
	height = 0
	for i in board:
		for y in i:
			if y == 1:
				height = height + 1
				break
		
	return height