import random

###creates a viewer friendly minesweeper board###
def flatten(board):
    flat = []
    for row in board:
        for column in board[row]:
            flat.append(board[row][column])
    return flat

###function for board creation & size adjustment####
def board(BOARD_SIZE):
    """creates a playing board while adjusting the board size as the imput
    """
    return {y+1:{x+1:{'bomb': False}
            for x in range(BOARD_SIZE)}
            for y in range(BOARD_SIZE)}

###creates full board seen  with all spaces visible on screen###

def show_bombs(board):
    data = flatten(bomb(board))
    symbol_data = []
    for cell in data:
        if cell['bomb'] == True:
            symbol_data.append('*')
        else:
            symbol_data.append(' ')
    return symbol_data

def show_board(symbol_data):
    """prints the board in the game interface"""
    return("""
_|12345678
1|{}{}{}{}{}{}{}{}
2|{}{}{}{}{}{}{}{}
3|{}{}{}{}{}{}{}{}
4|{}{}{}{}{}{}{}{}
5|{}{}{}{}{}{}{}{}
6|{}{}{}{}{}{}{}{}
7|{}{}{}{}{}{}{}{}
8|{}{}{}{}{}{}{}{}
""".format(*symbol_data))

###uses probability in random to add bombs to the board###

def bomb(board):
    bomb_count = 0
    while bomb_count < 10:  
        for row in board:
            for column in board[row]:                        
                if random.random() < 0.05 and board[row][column]['bomb'] == False and bomb_count < 10 :
                    board[row][column]['bomb'] = True
                    bomb_count += 1
    return board

###Makes sure that the 2 input variables after the help message prompt are valid###

def check_choice(choice):
    """ensures choice follows proper format

       choice format is: (1,1)

    """
    if not choice.startswith('('):
        print("Coordinate should start with '('")
    numbers = choice[1:-1]
    print(numbers)        
    input_list = numbers.split(',')
    input_list = [int(a) for a in input_list]
    x = input_list[0]
    y = input_list[1]
    print(x)
    print(y)
