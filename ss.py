import sys

print(sys.argv)

f = open(sys.argv[1], "r").read().split()

board = [[None] * 9 for x in range(9)]

for lineNum in range(len(f)):
    for charNum in range(len(f[lineNum])):
        ch = f[lineNum][charNum]
        board[lineNum][charNum] = ch if ch != "." else None

for line in board:
    print(line)

# for line in f:
#     line = line.strip()
#     for ch in line:
#         board[][] = ch



f.close()