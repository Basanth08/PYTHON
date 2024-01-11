
NAME_TO_TABLE = {'t': [[1,1,1],[0,1,0]], 
                 'T': [[1,1,1],[0,1,0],[0,1,0]], 
                 'z': [[1,1,0],[0,1,1]],
                 'c': [[1,1],[1,0],[1,1]],
                 'f': [[1,1],[1,0],[1,1], [1,0]],
                 'L': [[1,0,0],[1,1,1]],
                 'l':[[1,0], [1,1]]}
EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'

def transpose(Matrix):
    return [[ Matrix[col][row] for col in range(len(Matrix))] for row in range(len(Matrix[0]))]

def reverse_rows(Matrix):
    return Matrix[::-1]

def reverse_columns(Matrix):
    return [Matrix[row][::-1] for row in range(len(Matrix)) ]

def help_message():
    print("- 'help' to display commands")
    print("- 'quit' to quit the game" )
    print("- 'a <piece name> <row> <col>' to add a piece to the board at the position ") 
    print("- 'r <piece name>' to remove a piece")
    
class Shape:
    __slots__ = ['__table', '__position'] 
    
    def __init__(self, table,):
        self.__table = table
        self.__position = None        
    
    def __repr__(self):
        table_string = str(self.__table)
        position_string = str(self.__position)
        return "Table: " + table_string + ", Position: " + position_string

    def __eq__(self, other):
        try:
            return self.__table == other.__table
        except AttributeError:
            return False
    
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.__table))
        
    def fit(self, board, position):
        r, c = position
        for i in range(len(self.__table)):
            for j in range(len(self.__table[0])):
                if self.__table[i][j] == 1:
                    if board[r+i][c+j] != '-': 
                        return False
        return True

    def add(self, board, position, symbol):
        row, col = position  
        self.__position = position
        for i in range(len(self.__table)):
            for j in range(len(self.__table[0])): 
                if self.__table[i][j] == 1:
                    board[row+i][col+j] = symbol

    def remove(self, board):
        if self.__position:
            row, col = self.__position
            for i in range(len(self.__table)):
                for j in range(len(self.__table[0])):
                    if self.__table[i][j] == 1:
                        board[row+i][col+j] = '-'

    def get_table(self):
        return self.__table      
class Piece:
    def __init__(self, name):
        self.__name = name
        self.__shapes = [Shape(table) for table in  
                         [NAME_TO_TABLE[name], transpose(NAME_TO_TABLE[name]), 
                          reverse_rows(NAME_TO_TABLE[name]), reverse_columns(NAME_TO_TABLE[name])]]
        
        self.__current_shape = None
        self.__fit_shapes = []
        self.__last_fit_shape_index = -1
        
    def get_name(self):
        return self.__name
    
    def get_current_shape(self):
        return self.__current_shape
    
    def set_fit_shapes(self, board, position):
        self.__fit_shapes.clear()
        for shape in self.__shapes:
            if shape.fit(board, position):
                self.__fit_shapes.append(shape)
                
    def get_fit_shapes(self):
        return self.__fit_shapes
    
    def get_fit_shape(self):
        if not self.__fit_shapes:
            return None
        self.__last_fit_shape_index = (self.__last_fit_shape_index + 1) % len(self.__fit_shapes) 
        return self.__fit_shapes[self.__last_fit_shape_index]
    
    def add(self, board, shape, position): 
        self.__current_shape = shape
        shape.add(board, position, self.__name[0])
        
    def remove(self, board):
        if self.__current_shape:
            self.__current_shape.remove(board)
            self.__current_shape = None

class Puzzle:
    __slots__ = ['__board', '__pieces', '__pieces_on_board', '__game_over']
    
    def __init__(self, blockers):
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        for r, c in blockers:
            self.__board[r][c] = BLOCKER_SPOT
               
    def play(self):
        print(self)
        while True:
            response = input("Enter a command or 'help': ")
            if response == "quit":
                print("Bye!")
                break
            elif response == "help":
                help_message()
            else:
                pass

    def add(self, name, r, c):
        piece = self.__pieces[name]
        piece.set_fit_shapes(self.__board, (r, c))
        shape = piece.get_fit_shape()
        if shape is None:
            print("No shapes fit for this piece at that position")
            return
        while shape in self.__pieces_on_board.values(): 
            print(name + " is already on the board")
            shape = piece.get_fit_shape() 
            if shape is None:
                return
        piece.add(self.__board, shape, (r, c))
        self.__pieces_on_board[name] = shape
        print(self)

    def remove(self, name):
        if name not in self.__pieces_on_board:
            print(name + " is not on the board")
            return  
        piece = self.__pieces[name]
        shape = self.__pieces_on_board[name]
        piece.remove(self.__board) 
        del self.__pieces_on_board[name]
        print(self)

    def __str__(self):
        s = '    0 1 2 3 4 5\n'
        s +='   ------------\n'
        for index in range(len(self.__board)):
            s += str(index) + " | "
            for el in self.__board[index]:
                s += el + " "
            s += "\n"
        return s
     
def main(): 
    blocker_locations1 = ((0,1), (0,5), (2,0), (5,1), (5,4))
    blocker_locations2 = ((0,0), (0,1), (3,4), (4,0), (5,5))
    blocker_locations3 = ((0,1), (0,3), (4,3), (5,3), (5,5)) 
    # a_puzzle = Puzzle(blocker_locations1)
    # a_puzzle.play()
    a_puzzle = Puzzle(blocker_locations2)
    a_puzzle.play()
    # a_puzzle = Puzzle(blocker_locations3)
    # a_puzzle.play()
if __name__ == '__main__':
   main()
