board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(brd):
	for row in range(len(brd)):
		if row%3 == 0 and row != 0:
			print("- - - - - - - - - - - -")
		for col in range(len(brd[row])):
			if col%3 == 0 and col != 0:
				print(" | ", end="")
			if col == 8:
				print(brd[row][col])
			else:
				print(str(brd[row][col]) + " ", end="")

def empty(brd):
	for row in range(len(brd)):
		for col in range(len(brd[row])):
			if brd[row][col] == 0:
				return (row,col)
	return




print_board(board)
print(empty(board))
#solve(board)
#print("___________________")
#print(board_sol)