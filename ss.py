import sys
import numpy

print(sys.argv)

f = open(sys.argv[1], "r").read().split()

board = [[None] * 9 for x in range(9)]

for lineNum in range(len(f)):
    for charNum in range(len(f[lineNum])):
        ch = f[lineNum][charNum]
        board[lineNum][charNum] = int(ch) if ch != "." else None

## I'm going to write code between these lines only :p
board = numpy.copy(board)
print(board)
## End


## I will write code between these lines only :p

def cellIsValid(x, y, value):
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

# print(cellIsValid(2, 7, 1))
# print(cellIsValid(8, 0, 2))
print(cellIsValid(1, 2, 1))
##