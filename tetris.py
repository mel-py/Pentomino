from random import randrange as random
import pygame
import pentomino

frame = 0

cols, rows = 10, 21

pieces = [[[1, 1, 1, 1]],
			[[1, 0, 0], [1, 1, 1]],
			[[0, 0, 1], [1, 1, 1]],
			[[1, 1], [1, 1]],
			[[0, 1, 1], [1, 1, 0]],
			[[0, 1, 0], [1, 1, 1]],
			[[1, 1, 0], [0, 1, 1]]]
	
def draw_board():
	for i in range(0, len(board)):
		for j in range(0, len(board[i])):
			if board[i][j] == 1:
				pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(j*20, i*20, 20, 20))
				
def place_piece(x, y, piece, board):
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] == 1:
				board[y+j][x+i] = 1
	return board
	
#check if the piece moves in the desired direction if it causes a collision			
def check_collision(x, y, piece, board):
	for i in range(len(piece)):
		for j in range(len(piece[0])):
			if piece[i][j] == 1 and board[y+j][x+i] == 1:
				return True
	return False
	
def rotate_piece(piece):
	rotated = []
	temp = []
	for j in range(len(piece[0])):
		for i in range(len(piece)-1, -1, -1):	
			temp.append(piece[i][j])
		rotated.append(temp)
		temp = []
	return rotated
	
def cleared_row(board):
	for i in range(len(board)):
		found = True
		for j in board[i]:
			if j == 0:
				found = False
		if found:
			del board[i]
			board.insert(0,[0 for _ in range(cols)])
			
def make_move(board, piece):
	return pentomino.get_best_score(board, piece)
	
pygame.init()
screen = pygame.display.set_mode((200,400))
done = False

cur_piece = pieces[random(len(pieces))]
x, y = 4, 0
board = [[0 for y in range(cols)] for x in range(rows)]

#game loop
while not done:
	screen.fill((0, 0, 0))
	cleared_row(board)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and x+len(cur_piece) < 10:
				if not check_collision(x+1, y, cur_piece, board):
					x = x + 1
			if event.key == pygame.K_LEFT and x > 0 and board[x-1][y] is not 1:
				if not check_collision(x-1, y, cur_piece, board):
					x = x - 1
			if event.key == pygame.K_UP:
				cur_piece = rotate_piece(cur_piece)
	#draw the board and current piece
	for i in range(0, len(cur_piece)):
		for j in range(0, len(cur_piece[i])):
			if cur_piece[i][j] == 1:
				pygame.draw.rect(screen, (0, 128, 255), pygame.Rect((x*20)+(i*20), (y*20)+(j*20), 20, 20))
	
	draw_board()
	pygame.display.flip()
	frame = frame+1
	if y+len(cur_piece[0]) == 20 or check_collision(x, y+1, cur_piece, board):
		board = place_piece(x, y, cur_piece, board)
		cur_piece = pieces[random(len(pieces))]
		make_move(board, cur_piece)
		x, y, = 4, 0
	if frame == 2000:
		y += 1
		frame = 0