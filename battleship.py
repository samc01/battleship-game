# VARIABLES
board1 = [[" "] * 10 for i in range(10)]
board2 = [[" "] * 10 for i in range(10)]
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "cdF": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}

def select_len_ship(len):
    if len == 2:
        print("size 2")
    elif len == 3:
        print("size 3")
    elif len == 4:
        print("size 4")
    elif len == 6:
        print("size 6")

select_len_ship(6)