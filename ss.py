import sys
from numpy import copy

"""
Find next empty space in board (from specified row and col).
"""
def findNextEmpty(board, row, col):
    for newRow in range(row, 9):
        # can't search earlier than col if on row
        minCol = col if newRow == row else 0
        for newCol in range(minCol, 9):
            currentSquare = board[newRow][newCol]
            if not currentSquare:
                return newRow, newCol

"""
Check if cell with specified value in board at [x, y] is valid.

Checks if the value has already been seen in any row, column, or square of the board.
"""
def isCellValid(board, x, y, value):
    isValid = True

    # check rows
    for cell in board[x]:
        if cell == value:
            isValid = False
            break

    # check columns
    # only continue if valid so far (row is valid)
    if isValid:
        for i in range(0, 9):
            if board[i][y] == value:
                isValid = False
                break

    # check square=
    # only continue if valid so far (row and column are valid)
    if isValid:
        startRow = x - (x % 3)
        startColumn = y - (y % 3)
        for i in range (startRow, startRow + 3):
            if isValid:
                for j in range(startColumn, startColumn + 3):
                    if board[i][j] == value:
                        isValid = False
                        break
            else:
                # if we've found that the square is not valid, break out early
                break

    return isValid
"""
Solves the board through backtracking method.
"""
def solveBoard(board, row = 0, col = 0):
    board = copy(board)

    # find next empty space (from specified row and col)
    result = findNextEmpty(board, row, col)
    if not result:
        return board
    else:
        newRow, newCol = result

    # place a value and validate it
    result = False
    for number in range(1, 10):
        if not isCellValid(board, newRow, newCol, number):
            continue
        board[newRow][newCol] = number
        result = solveBoard(board, newRow, newCol)
        if isinstance(result, type(board)):
            break
    return result

def transposeBoard(board, reflectX, reflectY):
    boardCopy = copy(board)
    for i in range(len(board)):
        tempRow = copy(board[i])
        if reflectX:
            for j in range(len(board[i])):
                tempRow[len(board[i]) - j - 1] = board[i][j]
        if reflectY:
            boardCopy[len(board) - i - 1] = tempRow
        else:
            boardCopy[i] = tempRow

    return boardCopy

def main():
    if len(sys.argv) > 2:
        print("Expects one argument: filename")
        return

    try:
        f = open(sys.argv[1], "r").read().split()
    except:
        print("Could not open file. Check your file path and name.")
        return

    board = [[None] * 9 for x in range(9)]

    clueCount = [0] * 4
    for lineNum in range(len(f)):
        for charNum in range(len(f[lineNum])):
            ch = f[lineNum][charNum]
            if ch != ".":
                if lineNum <= 4:
                    if charNum <= 4:
                        clueCount[0] += 1
                    if charNum >=4:
                        clueCount[1] += 1
                if lineNum >= 4:
                    if charNum <= 4:
                        clueCount[2] += 1
                    if charNum >=4:
                        clueCount[3] += 1
            board[lineNum][charNum] = int(ch) if ch != "." else None

    maxIndex = clueCount.index(max(clueCount))

    reflectX = False if maxIndex % 2 == 0 else True
    reflectY = False if maxIndex // 2 == 0 else True
    board = transposeBoard(board, reflectX, reflectY)

    solution = solveBoard(board)

    print("SOLUTION:\n", transposeBoard(solution, reflectX, reflectY))

if __name__ == "__main__":
    main()