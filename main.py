
# rules
# 1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
# 2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
# 3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
# 4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.



board = [
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    ]

def print_board(b, age):
    print('AGE: ' + str(age))
    for i in b:
        print(i)
    print('---------------')

def next_state(board):
    SIZE = len(board)
    new_board = [[0 for i in range(0, SIZE)] for j in range(0, SIZE)]
    count_of_neighbours = [[0 for i in range(0, SIZE)] for j in range(0, SIZE)]
    # [(i-1, j-1), (i-1, j), (i-1, j+1)]
    # [(i, j-1),   (i,j),    (i, j+1)]
    # [(i+1, j-1), (i+1, j), (i+1, j+1)]

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            count_alive_neighbours = 0

            if i - 1 >= 0:
                if board[i-1][j] == 1: # сосед сверху
                    count_alive_neighbours = count_alive_neighbours + 1
                if j + 1 <= SIZE - 1:
                    if board[i-1][j+1] == 1: # сосед сверху справа
                        count_alive_neighbours = count_alive_neighbours + 1 
            if j + 1 <= SIZE - 1:
                if board[i][j+1] == 1: # сосед справа
                    count_alive_neighbours = count_alive_neighbours + 1
                if i + 1 <= SIZE - 1:
                    if board[i+1][j+1] == 1: # сосед справа внизу
                        count_alive_neighbours = count_alive_neighbours + 1

            if i + 1 <= SIZE - 1:
                if board[i+1][j] == 1: #сосед внизу
                    count_alive_neighbours = count_alive_neighbours + 1
                if j-1 >= SIZE - 1:
                    if board[i+1][j-1] == 1: # сосед внизу слева
                        count_alive_neighbours = count_alive_neighbours + 1
            if j-1 <= SIZE - 1:
                if board[i][j-1] == 1: # сосед слева
                    count_alive_neighbours = count_alive_neighbours + 1
                if i-1 <= SIZE - 1:
                    if board[i-1][j-1] == 1: # сосед слева вверху
                        count_alive_neighbours = count_alive_neighbours + 1
            
            count_of_neighbours[i][j] = count_alive_neighbours

    for i, row in enumerate(count_of_neighbours):
        for j, count in enumerate(row):
            if board[i][j] == 1: # если клетка живая
                if count < 2: # 1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
                    new_board[i][j] = 0
                if 2 <= count <= 3: # 2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
                    new_board[i][j] = 1
                if count > 3: # 3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
                    new_board[i][j] = 0
            else:
                if count == 3: # 4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.
                    new_board[i][j] = 1

    return new_board

# current_age = board
# print_board(current_age, 0)
# for i in range(10):
#     current_age = next_state(current_age)
#     print_board(current_age, i+1)


