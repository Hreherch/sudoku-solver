import sys
from numpy import copy

print(sys.argv)

f = open(sys.argv[1], "r").read().split()

board = [[None] * 9 for x in range(9)]

for lineNum in range(len(f)):
    for charNum in range(len(f[lineNum])):
        ch = f[lineNum][charNum]
        board[lineNum][charNum] = int(ch) if ch != "." else None

## I'm going to write code between these lines only :p
board = copy(board)
print(board)

# find next empty space (from specified row and col)
def findNextEmpty(board, row, col):
    for newRow in range(row, 9):
        # can't search earlier than col if on row
        minCol = col if newRow == row else 0
        for newCol in range(minCol, 9):
            currentSquare = board[newRow][newCol]
            if not currentSquare:
                return newRow, newCol

## End


## I will write code between these lines only :p

def cellIsValid(x, y, value, board):
    isValid = True
    print(x, y, value)

    # check rows
    for cell in board[x]:
        if cell == value:
            isValid = False
            print("ROW FALSE")
            break

    # print("ROW:",board[x])

    # check columns
    # only continue if valid so far
    if isValid:
        # print("COLUMN:")
        for i in range(0, 9):
            # print(board[i][y])
            if board[i][y] == value:
                isValid = False
                print("COLUMN FALSE")
                break

    # check square=
    # only continue if valid so far
    if isValid:
        startRow = x - (x % 3)
        startColumn = y - (y % 3)
        # print("SQUARE:")
        for i in range (startRow, startRow + 3):
            if isValid:
                for j in range(startColumn, startColumn + 3):
                    if board[i][j] == value:
                        isValid = False
                        print("SQUARE FALSE")
                        break
            else:
                # if we've found that the square is not valid, break out early
                break

    return isValid

# should ensure board is validated before passing in
def solveBoard(board, row=0, col=0):
    board = copy(board)

    # find next empty space (from specified row and col)
    result = findNextEmpty(board, row, col)
    if not result:
        return board
    else:
        newRow, newCol = result

    # place a value and validate it
    result = False
    for number in range(1, 9+1):
        if not cellIsValid(newRow, newCol, number, board):
            continue
        board[newRow][newCol] = number
        result = solveBoard(board, newRow, newCol)
        if isinstance(result, type(board)):
            break
    return result

print("solution:", solveBoard(board))