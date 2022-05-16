
def print_board(board2print):
    for row in board2print:
        for col in row:
            print(col, end='')
        print()

board_size = 10

print("board 1")

board1 = [[' . ']*board_size]*board_size

print(board1)
print(len(board1))




corrdis = [[0,1],[2,3],[4,5]]

for x,y in corrdis:
    board1[x][y] = ' x '


print_board(board1)
print()
print("board 2")

board2 = [[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . '],
            [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']]

print(board2)
print(len(board2))

for x,y in corrdis:
    board2[x][y] = ' x '

print_board(board2)