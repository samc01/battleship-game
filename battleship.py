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

def position_ship(start_pos, finish_pos):
    
    # START
    letter_start = start_pos[0]
    start_pos_lst = start_pos[1:]
    number_start = int("".join(start_pos_lst)) - 1
    letter_start_number = letters_to_numbers[letter_start] + 1

    # FINISH
    letter_finish = finish_pos[0]
    finish_pos_lst = finish_pos[1:]
    number_finish = int("".join(finish_pos_lst)) - 1
    letter_finish_number = letters_to_numbers[letter_finish] + 1

    if letter_start == letter_finish:
        for i in range(number_start, number_finish + 1, 1):
            board1[i][letter_start_number] = "|O|"
        
    elif number_start == number_finish:
        for i in range(letter_start_number, letter_finish_number + 1, 1):
            board1[number_start][i] = "|O|"

# GAME
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
    
    for length in ships_lengths:
        print("Let's set up the " + str(length) +" block long ship, type to starting block!")
        starting_block = input()
        print("Great work, type the finishing block!")
        finishing_block = input()
        print(str(length) + " block ship position -> " + starting_block + ":" + finishing_block)
        position_ship(str(starting_block), str(finishing_block))
    
    print_board(board1)

elif answer == "N":
    print("You are missing out!")
else:
    print("Can't process that my friend!")
