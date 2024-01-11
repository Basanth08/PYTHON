import math 
import random
import timing

def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

def make_puzzle(N):
        #This creates the sudoku board
        board = [[0] * N for _ in range(N)]
        numbers = list(range(1, N+1))
        #initializing
        for _ in range(N):
            row = random.randint(0, N-1)
            col = random.randint(0, N-1)
            num = random.randint(1,N)
            board[row][col] = num
            numbers = list(set(numbers))

        n = int(math.sqrt(N))

        row_sets = [set() for _ in range(N)]
        col_sets = [set() for _ in range(N)]
        reg_sets = [[set() for _ in range(n)] for _ in range(n)]

        for row in range(N):
            for column in range(N):
                if board[row][column] != 0:
                    val = board[row][column]
                    row_sets[row].add(val)
                    col_sets[column].add(val)
                    reg_row = row // n
                    reg_col = column // n
                    reg_sets[reg_row][reg_col].add(val)
#gives the puzzle data
        puzzle = {
            'board': board,
            'row_sets': row_sets,
            'col_sets': col_sets,
            'reg_sets': reg_sets
        }
        return puzzle

def get_square(puzzle, row, col):
    #assigning a value
    value = puzzle['board'][row][col]
    row_set = puzzle['row_sets'][row]  
    col_set = puzzle['col_sets'][col]
    n = int(math.sqrt(len(puzzle['board'])))
    reg_set = puzzle['reg_sets'][row//n][col//n]

    square = {
        'value': value,
        'row_set': row_set,
        'col_set': col_set,
        'reg_set': reg_set
    }
    return square   

def move(puzzle, row, col, new_value):
    square = get_square(puzzle, row, col)
    if square['value'] == 0 and new_value not in square['row_set'] and new_value not in square['col_set'] and new_value not in square['reg_set']:
            puzzle['board'][row][col] = new_value
            puzzle['row_sets'][row].add(new_value)
            puzzle['col_sets'][col].add(new_value)
            n = int(math.sqrt(len(puzzle['board'])))
            reg_row = row // n
            reg_col = col // n
            puzzle['reg_sets'][reg_row][reg_col].add(new_value)
            return True
    elif square['value'] !=0:
        return False
    else:
        return False
    # Time complexity: O(1)
def fill_puzzle(puzzle):
  board = puzzle['board']
  attempts = 0
  filled = 0
  while filled < len(board) ** 2 and attempts < len(board) ** 4:
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    if board[row][col] == 0:
      random_num = random.randint(1, len(board))
      if move(puzzle, row, col, random_num):
        filled += 1  
    attempts += 1  
  # Time complexity is O(N^4) 
  # In worst case tries up to N^4 random moves
def main():
    N = 16
    print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    print("Initial puzzle:")
    print(puzzle)
    print("Initial board:")
    print_board(puzzle['board'])
    fill_puzzle(puzzle)
    print("\nFinal puzzle:")
    print(puzzle)
    print("Final board:")
    print_board(puzzle['board'])
    timing.time_function(fill_puzzle,puzzle)
if __name__ =="__main__": 
    main()
