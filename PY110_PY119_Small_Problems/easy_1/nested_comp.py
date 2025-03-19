import random

PLAYER_SYMBOLS = ['X', 'O']
MAX_ROUNDS = 5

def prompt(text):
    print(f"=> {text}")


def initialize_board():
    ttt_board = [ 
    ["_","_","_"], 
    ["_","_","_"], 
    ["_","_","_"]
]
    return ttt_board

def display(b):
    for row in b:
        print("| " + " | ".join(row) + " |")
    print("-" * 13)

def available_spaces(b):
    available = []

    for row in range(3):
        for column in range(3):
            if b[row][column] == '_':
                # Convert 2D index to 1D position (1-9) / "flatten"
                position = row * 3 + column + 1
                available.append(str(position))
    return available

def join_or(options_list, separator = ', ', connector = 'or'):
    if not options_list:
        return ''
    
    lst = options_list[:-1]
    last_element = str(options_list[-1])
    result = ''

    if len(options_list) == 1:
        return str(options_list[0])
    elif len(options_list) == 2:
        return f"{options_list[0]} {connector} {options_list[1]}"
    else:
        for option in lst:
            result += str(option) + separator
        return f"{result}{connector} {last_element}" 

def convert_to_2d(position):
    row = position // 3 # integer division to get the row
    column = position % 3 # modulo to get the column

    return row, column
           

def check_for_threats(b):
    #check rows

    for row in range(3):
        if b[row].count('X') == 2 and '_' in b[row]:
            empty_position = b[row].index('_')
            return row, empty_position
        
    #check columns
    for column in range(3):
        column_values = [b[row][column] for row in range(3)]
        if column_values.count('X') == 2 and '_' in column_values:
            empty_position = column_values.index('_')
            return  empty_position, column
    
    #check main diagonal
    main_diagonal = [b[i][i] for i in range(3)]
    if main_diagonal.count('X') == 2 and '_' in main_diagonal:
        empty_position = main_diagonal.index('_')
        return empty_position, empty_position

    #check anti-diagonal
    anti_diagonal = [b[i][2-i] for i in range(3)]
    if anti_diagonal.count('X') == 2 and '_' in anti_diagonal:
        empty_position = anti_diagonal.index('_')
        return empty_position, 2 - empty_position

    #if no threat is found
    return None
        
def computer_turn(b):
    computer_choice = random.choice(available_spaces(b))

    computer_choice = int(computer_choice) - 1 
    row, column = convert_to_2d(computer_choice)
    
    b[row][column] = 'O'

board = [ 
    ["_","_","_"], 
    ["_","X","_"], 
    ["X","_","_"]
]

coord_1, coord_2 = check_for_threats(board)

board[coord_1][coord_2] = 'O'
print(board)