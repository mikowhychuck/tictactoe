def drukuj_plansze(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def stworz_plansze(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("[ ]")
        board.append(row)
    for i in range(size):
        if i<10:
            board[0][i] = f" {i} "
        else:
            board[0][i] = f" {i}"
    for i in range(size):
        if i<10:
            board[i][0] = f"{i} "
        else:
            board[i][0] = f"{i}"
    board[0][0] = "  "
    return board


def czy_wygrana(board, symbol, n):

    for row in board:
        if ''.join(row).find(symbol * 5) != -1:
            return True

    for col in range(n):
        column = ''.join([row[col] for row in board])
        if column.find(symbol * 5) != -1:
            return True

    diag1 = ''.join([board[i][i] for i in range(n)])
    diag2 = ''.join([board[i][n - i - 1] for i in range(n)])
    if diag1.find(symbol * 5) != -1 or diag2.find(symbol * 5) != -1:
        return True

    for row in range(n - 4):
        for col in range(n - 4):
            if board[row][col] == symbol and board[row + 1][col + 1] == symbol and board[row + 2][col + 2] == symbol and \
                    board[row + 3][col + 3] == symbol and board[row + 4][col + 4] == symbol:
                return True
    for row in range(4, n):
        for col in range(n - 4):
            if board[row][col] == symbol and board[row - 1][col + 1] == symbol and board[row - 2][col + 2] == symbol and \
                    board[row - 3][col + 3] == symbol and board[row - 4][col + 4] == symbol:
                return True

    return False

def ruch_graczaX(board):
    print("Gracz X: ")
    x = int(input("rząd: "))
    y = int(input("kolumna: "))
    if board[x][y] != "[X]" and board[x][y] != "[O]":
        board[x][y] = "[X]"
    else:
        print("Podane pole juz jest zajete")
    return board

def ruch_graczaY(board):
    print("Gracz O: ")
    x = int(input("rząd: "))
    y = int(input("kolumna: "))
    if x != 0 and y != 0:
        if board[x][y] != "[X]" and board[x][y] != "[O]":
            board[x][y] = "[O]"
        else:
            print("Podane pole juz jest zajete")
    return board

def main():
    n = 0
    while n<5 or n>20 :
        n = int(input("Podaj wielkosc planszy "))
        if n<5 or n>20 :
            print("Wpisz liczbe od 5 do 20")
    board = stworz_plansze(n+1)
    drukuj_plansze(board)
    while czy_wygrana(board, '[X]', n+1)==False and czy_wygrana(board, '[O]', n+1)==False:
        ruch_graczaX(board)
        drukuj_plansze(board)
        if czy_wygrana(board, '[X]', n+1)==True:
            print("Wygrana gracza X")
            break
        ruch_graczaY(board)
        if czy_wygrana(board, '[O]', n+1)==True:
            print("Wygrana gracza O")
            break
        drukuj_plansze(board)
        

if __name__ == "__main__":
    main()