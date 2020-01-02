from IPython.display import Markdown, display

def printmd(string):
    display(Markdown(string))


def sudoku_ok(line):
    return (len(line) == 9 and sum(line) == sum(set(line)))

def check_sudoku(grid):
    bad_rows = [row for row in grid if not sudoku_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    squares = []
    for i in range(9, 3):
        for j in range(9, 3):
            square = list(itertools.chain(row[j:j+3] for row in grid[i:i+3]))
            squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square)]
    if not (bad_rows or bad_cols or bad_squares):
        printmd("#### Sudoku is **correct**")
    else:
        printmd("#### Sudoku is **NOT** correct")
    return

def sudoku_print(grid):
    print("-"*37)
    for i, row in enumerate(grid):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")