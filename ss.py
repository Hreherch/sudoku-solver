import sys
import numpy

print(sys.argv)

f = open(sys.argv[1], "r").read().split()

board = [[None] * 9 for x in range(9)]

for lineNum in range(len(f)):
    for charNum in range(len(f[lineNum])):
        ch = f[lineNum][charNum]
        board[lineNum][charNum] = ch if ch != "." else None

for line in board:
    print(line)

## I'm going to write code between these lines only :p
board = numpy.copy(board)
print(board)
## End
