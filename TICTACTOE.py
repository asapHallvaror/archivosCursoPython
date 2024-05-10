import random

def display_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("     |     |")

def enter_move(board):
    while True:
        move = int(input("Ingresa tu movimiento (1-9): "))
        row = (move - 1) // 3
        col = (move - 1) % 3
        if move < 1 or move > 9:
            print("Número inválido. Por favor, ingresa un número entre 1 y 9.")
            continue
        if board[row][col] != ' ':
            print("Esa casilla ya está ocupada. Por favor, elige otra.")
            continue
        board[row][col] = 'O'
        break

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    board[1][1] = 'X'  # La máquina inicia con una 'X' en el centro
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("¡Felicidades! ¡Has ganado!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("¡Es un empate!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("¡La máquina ha ganado!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("¡Es un empate!")
            break

if __name__ == "__main__":
    main()
