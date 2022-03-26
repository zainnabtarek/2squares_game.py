#two squarers game , by : Zainab Tarek
#make sure to choose two squares in the SAME column and rows in Ascending order



global board
board = [
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"], ]


def player_input():
    global firstrow, firstcolumn, secrow, seccolumn
    while True:
        try:
            firstrow = int(input("enter first row :"))
            firstcolumn = int(input("enter column : "))
            secrow = int(input("enter next row :"))
            seccolumn = int(input("enter next column : "))
            if check_end_game():
                if check_index() == False:
                    break
            else:
                print("Enter Valid Index.")
        except:
            print("Enter Valid Number Please.")

    return (firstrow, firstcolumn, secrow, seccolumn)


def check_end_game():
    if (firstcolumn == seccolumn) and (secrow == firstrow +1):
        return True
    else:
        return False


def change_index():
    board[firstrow][firstcolumn] = "X"
    board[secrow][seccolumn] = "X"


def print_board():
    for row in board:
        print(row)


def check_index():
    if board[firstrow][firstcolumn] == "X" and board[secrow][seccolumn] == "X":
        return True
    else:
        return False


def is_winner():
    if check_end_game() == False:
        print("Player Won")


def check_board():
    counter = 0
    for row in range(0, 3):
        for column in range(0, 4):
            if board[row][column] != "X" and board[row + 1][column] != "X":
                counter += 1
    if counter > 0:
        return True
    elif counter == 0:
        return False


def program():
    while True:

        # Player 1 turn
        print_board()
        print("Player 1 Turn")
        player_input()
        change_index()
        if check_board():
            # player 2 turn
            print_board()
            print("Player 2 Turn")
            player_input()
            change_index()
            if check_board == False:
                print("player 2 won")
                print("Thanks for using my game.")
                break
        else:
            print("player 1 won")
            print("Thanks for using my game.")
            break


program()
