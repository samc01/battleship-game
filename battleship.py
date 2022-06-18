# MODULES

import random

# VARIABLES

board1 = [["| |"] * 10 for i in range(10)]
board2 = [["| |"] * 10 for i in range(10)]
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
ships_lengths = [2, 3, 4, 6]

# FUNCTIONS

def setup_board(board):
    number = 0
    for lst in board:
        number += 1
        if number < 10:
            lst.insert(0, str(number) + " ")
        else:
            lst.insert(0, str(number))

    board.append(["  ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J "])

def print_board(board):
    for i in board:
        print("".join(i))

def position_ship_player(start_pos, finish_pos):
    if (len(start_pos) > 3 or len(finish_pos) > 3):
        print("Max 3 characters for each position")
    else: 
        if (letters_to_numbers.get(start_pos[0].upper(), "not found") == "not found" or 
        letters_to_numbers.get(finish_pos[0].upper(), "not found") == "not found"):
            print("One of the columns you are trying to select doesn't exist")
        else: 
            if (int(start_pos[1:]) > 10 or int(finish_pos[1:]) > 10):
                print("You are selecting rows that doesn't exist")
            else:
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
                        board1[i][column_start] = "|O|"
                    
                elif row_start == row_finish:
                    for i in range(column_start, column_finish + 1, 1):
                        board1[row_start][i] = "|O|"

def position_ship_computer(ship_size):
    row_start = random.randint(0, 9)
    column_start = random.randint(1, 10)
    
    while row_start + ship_size > 9:
        row_start = random.randint(0, 9)
        if row_start + ship_size <= 9:
            break
    while column_start + ship_size > 10:
        column_start = random.randint(1, 10)
        if column_start + ship_size <= 10:
            break
    
    direction = random.randint(0, 1)
    # COLUMN = 0 | ROW = 1
    if direction == 0:
        for i in range(row_start, row_start + ship_size, 1):
            board2[i][column_start] = "|O|"
    elif direction == 1:
        for i in range(column_start, column_start + ship_size, 1):
            board2[row_start][i] = "|O|"   

def run_game():
    print("Welcome to the battleship game!")
    print("Ready to start playing? (Y/N)")
    answer = input()
    if answer == "Y":
        print("Awesome")
        print("Let's start by setting your ships!")
        print("You have 4 ships, their sizes in blocks are 2, 3, 4 and 6! Set them out the best you can!")
        print("In order to setup a ship you will need to pass the start block and the end block!")
        print("Here is how the board will look like so you have an idea!")
        setup_board(board1)
        print_board(board1)
        
        # SETUP PLAYER BOARD

    elif answer == "N":
        print("You are missing out!")
    else:
        print("Can't process that my friend!")

position_ship_computer(2)
position_ship_computer(3)
position_ship_computer(4)
position_ship_computer(6)

setup_board(board2)
print_board(board2)
