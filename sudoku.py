import sys
def isRowValid(board, row):
	# Creating a seperate array and storing all encoutered numbers to check for repeat values
	constraint = [False] * 9
	for i in range(9):
		boardValue = board[row][i]
		if(boardValue != 0):
			if(constraint[boardValue - 1]):
				return False
			else:
				constraint[boardValue - 1] = True
	return True

def isColumnValid(board, col):
	# Creating a seperate array and storing all encoutered numbers to check for repeat values
	constraint = [False] * 9
	for i in range(9):
		boardValue = board[i][col]
		if(boardValue != 0):
			if(constraint[boardValue - 1]):
				return False
			else:
				constraint[boardValue - 1] = True
	return True

def isBoxValid(board, row, col):
	constraint = [False] * 9
	colStart = (col % 3) * 3
	rowStart = (row % 3) * 3
	for i in range(3):
		for j in range(3):
			boardValue = board[rowStart + i][colStart + j]
			if(boardValue != 0):
				if(constraint[boardValue - 1]):
					return False
				else:
					constraint[boardValue - 1] = True
	return True

def isBoardValid(board, row, col):
	return isRowValid(board, row) and isColumnValid(board, col) and isBoxValid(board, row, col)

def populateBoard(board):
	return

def initPuzzle():
	# board = [[0] * 9 for i in range(9)]
	# populate(board)

	# for easier puzzle creation
	board = [[7, 0, 9, 0, 0, 0, 0, 6, 4], 
			 [0, 0, 0, 0, 0, 1, 3, 0, 0],
			 [3, 4, 0, 9, 0, 0, 0, 0, 0],
			 [0, 5, 0, 0, 0, 9, 0, 1, 3],
			 [0, 0, 7, 4, 0, 0, 0, 0, 0],
			 [0, 0, 0, 6, 0, 5, 4, 2, 0],
			 [4, 2, 0, 5, 9, 0, 6, 8, 1],
			 [0, 0, 6, 1, 2, 0, 0, 0, 0],
			 [5, 7, 1, 8, 3, 0, 9, 4, 0]]
	return board

def printBoard(board):
	for i in range(len(board)):
		print(board[i])

def validatePuzzle(board):
	valid = True
	for i in range(9):
		if(not isBoardValid(board, i, i)):
			valid = False
			break

	return valid

# solve board using backtracking
def solveBoard(board):
	for i in range(9):
		for j in range(9):
			if(board[i][j] == 0):
				for val in range(1, 10):
					board[i][j] = val
					if(isBoardValid(board, i, j) and solveBoard(board)):
						return True
				board[i][j] = 0
				return False

	return True

def main():
	board = initPuzzle()
	printBoard(board);

	# Ensure starting puzzle piece is a valid puzzle
	if(not validatePuzzle(board)):
		print("Starting Puzzle board is not valid, try again")
		return
	else:
		print("Starting puzzle is good to go")

	solveBoard(board)
	printBoard(board)



if __name__ == '__main__':
	main()