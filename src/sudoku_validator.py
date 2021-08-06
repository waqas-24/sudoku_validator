
valid_board = [
    [ 5  ,  3  , None, None,  7  , None, None, None, None],
    [ 6  , None, None,  1  ,  9  ,  5  , None, None, None],
    [None,  9  ,  8  , None, None, None, None,  6  , None],
    [ 8  , None, None, None,  6  , None, None, None,  3  ],
    [ 4  , None, None,  8  , None,  3  , None, None,  1  ],
    [ 7  , None, None, None,  2  , None, None, None,  6  ],
    [None,  6  , None, None, None, None,  2  ,  8  , None],
    [None, None, None,  4  ,  1  ,  9  , None, None,  5  ],
    [None, None, None, None,  8  , None, None,  7  ,  9  ]
]

invalid_board = [
    [ 8  ,  3  , None, None,  7  , None, None, None, None],
    [ 6  , None, None,  1  ,  9  ,  5  , None, None, None],
    [None,  9  ,  8  , None, None, None, None,  6  , None],
    [ 8  , None, None, None,  6  , None, None, None,  3  ],
    [ 4  , None, None,  8  , None,  3  , None, None,  1  ],
    [ 7  , None, None, None,  2  , None, None, None,  6  ],
    [None,  6  , None, None, None, None,  2  ,  8  , None],
    [None, None, None,  4  ,  1  ,  9  , None, None,  5  ],
    [None, None, None, None,  8  , None, None,  7  ,  9  ]
]


def check_sudoku(board):
    
# Check size of the board
    board_length=len(board)    
    for i in board:
        if len(i)!=board_length:
            return False
    

# Checking repitition for rows
    for rows in board:
        rep_check=set()
        for element in rows:                      
            if element in rep_check and element != None:                
                return False
            else:
                rep_check.add(element)

# checking repitition in columns using index
# looping through column by column 

    for i in range(board_length): 
        rep_check=set()
        for j in range(board_length):    
            element= board[j][i]            
            if element in rep_check and element != None:                           
                return False
            else:
                rep_check.add(element)
# Checking nine 3x3 sub-grids contains the digits 1-9 without repetition

# First creating 3x3 matrices

    sub_grids =[]
    rep_check=set()  
    for i in range(0,board_length-2,3):
        for j in range(0,board_length-2,3):         
            sub_grids.append([board[i][j:3+j],
                             board[i+1][j:3+j],
                             board[i+2][j:3+j]])


# now checking for repitition in each 3x3 sub-grid
         
    for matrix in sub_grids:
        rep_check=set()
        for rows in matrix:            
            for element in rows:
                if element in rep_check and element != None:
                    print("found repitition in 3x3 sub-grid")               
                    return False
                else:
                    rep_check.add(element)

    return True

if __name__ == "__main__":
    print(check_sudoku(valid_board))