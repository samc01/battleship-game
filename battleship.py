import random
from tabnanny import check


board_player = [["| |"] * 8 for i in range(8)]
board_computer_hidden = [["| |"] * 8 for i in range(8)]
board_computer_displayed = [["| |"] * 8 for i in range(8)]
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
ships_lengths = [2, 3, 4, 5]


def setup_board(board):
    number = 0
    for lst in board:
        number += 1
        lst.insert(0, str(number) + " ")
        
    board.append(["  ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "])

setup_board(board_player)
setup_board(board_computer_hidden)
setup_board(board_computer_displayed)


def print_board(board):
    for i in board:
        print("".join(i))


def position_ship_computer(ship_size):
    row_start = random.randint(0, 7)
    column_start = random.randint(1, 8)
    
    while row_start > 7 - ship_size + 1 or column_start > 8 - ship_size + 1:
        row_start = random.randint(0, 7)
        column_start = random.randint(1, 8)
        if row_start <= 7 - ship_size + 1 or column_start <= 8 - ship_size + 1:
            break
    
    if row_start <= 7 - ship_size + 1 and column_start <= 8 - ship_size + 1:
        direction = random.randint(0, 1)
        # COLUMN = 0 | ROW = 1
        if direction == 0:
            for i in range(row_start, row_start + ship_size, 1):
                board_computer_hidden[i][column_start] = "|O|"
        elif direction == 1:
            for i in range(column_start, column_start + ship_size, 1):
                board_computer_hidden[row_start][i] = "|O|"  
    elif column_start > row_start:
        for i in range(row_start, row_start + ship_size, 1):
            board_computer_hidden[i][column_start] = "|O|"
    elif row_start > column_start:
        for i in range(column_start, column_start + ship_size, 1):
            board_computer_hidden[row_start][i] = "|O|"
    
    print(row_start, column_start)

def setup_computer_board():
    position_ship_computer(2)
    position_ship_computer(3)
    position_ship_computer(4)
    position_ship_computer(5)

def computer_shoots():
    row = random.randint(0, 7)
    column = random.randint(1, 8)

    while board_player[row][column] == "|-|":
        row = random.randint(0, 7)
        column = random.randint(1, 8)

    if board_player[row][column] == "|O|":
        board_player[row][column] = "|X|"
    elif board_player[row][column] == "|X|":
        board_player[row][column] = "|X|"
    else:
        board_player[row][column] = "|-|"

def check_computer():
    blocks_left_computer = 0
    for square in board_computer_hidden:
        for sub_square in square:
            if sub_square == "|O|":
                blocks_left_computer += 1
    
    return blocks_left_computer


def position_ship_player(start_pos, finish_pos):
    # START
    letter_start = start_pos[0].upper()
    number_start = start_pos[1:]
    row_start = int("".join(number_start)) - 1
    column_start = letters_to_numbers[letter_start] + 1

    # FINISH
    letter_finish = finish_pos[0].upper()
    number_finish = finish_pos[1:]
    row_finish = int("".join(number_finish)) - 1
    column_finish = letters_to_numbers[letter_finish] + 1

    if letter_start == letter_finish:
        for i in range(row_start, row_finish + 1, 1):
            board_player[i][column_start] = "|O|"
        
    elif row_start == row_finish:
        for i in range(column_start, column_finish + 1, 1):
            board_player[row_start][i] = "|O|"

def setup_player_board():
    print("Let's start by setting your ships!")
    print("You have 4 ships, their sizes in blocks are 2, 3, 4 and 5! Set them out the best you can!")
    print("In order to setup a ship you will need to pass the start block and the end block!")
    print("Here is how the board will look like so you have an idea!")
    print_board(board_player)
        
    for length in ships_lengths:
        print("Let's set up the " + str(length) +" block long ship, type to starting block!")
        starting_block = input()
        print("Great work, type the finishing block!")
        finishing_block = input()
        print(str(length) + " block ship position -> " + starting_block + ":" + finishing_block)
        position_ship_player(str(starting_block), str(finishing_block))

def player_shoots(position):
    letter = position[0].upper()
    number = position[1:]
    row = int("".join(number)) - 1
    column = letters_to_numbers[letter] + 1

    if board_computer_hidden[row][column] == "|O|":
        board_computer_hidden[row][column] = "|X|"
        board_computer_displayed[row][column] = "|X|"
    elif board_computer_hidden[row][column] == "|X|":
        board_computer_hidden[row][column] = "|X|"
        board_computer_displayed[row][column] = "|X|"
    else:
        board_computer_hidden[row][column] = "|-|"
        board_computer_displayed[row][column] = "|-|"

def check_player():
    blocks_left_player = 0
    for square in board_player:
        for sub_square in square:
            if sub_square == "|O|":
                blocks_left_player += 1
    
    return blocks_left_player


def run_game():
    print("Welcome to the battleship game!")
    print("Ready to start playing? (Y/N)")
    answer = input()
    if answer == "Y":
        print("Awesome")

        setup_player_board()
        setup_computer_board()

        print_board(board_computer_displayed)
        print(" -  -  -  -  -  -  -  -  -")
        print_board(board_player)

        print("Let's start shooting!")

        while check_computer() != 0 or check_player() != 0:
            print("Type where you want to shoot, for example: A1")
            square_to_be_shot = input()
            player_shoots(square_to_be_shot)
            computer_shoots()

            print_board(board_computer_displayed)
            print(" -  -  -  -  -  -  -  -  -")
            print_board(board_player)

            if check_computer() == 0:
                print("You have won!")
                exit()
                break
            elif check_player() == 0:
                print("The computer has won!")
                exit()
                break

    elif answer == "N":
        print("You are missing out!")
    else:
        print("Can't process that my friend!")


run_game()

