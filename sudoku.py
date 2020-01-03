from IPython.display import Markdown, display
from itertools import *

def printmd(string):
	display(Markdown(string))


def sudoku_ok(line):
	return (len(line) == 9 and sum(line) == sum(set(line)))

def check_sudoku(grid):
	bad_rows = [row for row in grid if not sudoku_ok(row)]
	grid = list(zip(*grid))
	bad_cols = [col for col in grid if not sudoku_ok(col)]
	squares = []
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			square = list(chain(row[j:j+3] for row in grid[i:i+3]))
			sqip = []
			for sq in square:
				for s in sq:
					sqip.append(s)
			squares.append(sqip)
	bad_squares = [square for square in squares if not sudoku_ok(square)]
	if not (bad_rows or bad_cols or bad_squares):
		printmd("#### Sudoku is **correct**")
	else:
		printmd("#### Sudoku is **NOT** correct")
	return

def sudoku_print(grid, bold={}):
	print("-"*37)
	for i, row in enumerate(grid):
		if i in bold:
			print(("|" + " {}   {}   {} |"*3 + " <-- swapped").format(*[x if x != 0 else " " for x in row]))
		else:
			print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
		if i == 8:
			print("-"*37)
		elif i % 3 == 2:
			print("|" + "---+"*8 + "---|")

def swap_rows(grid, y1, y2):
	new_grid = list(grid)
	for i in range(0, 9):
		temp = new_grid[y1][i]
		new_grid[y1][i] = new_grid[y2][i]
		new_grid[y2][i] = temp
	return new_grid
