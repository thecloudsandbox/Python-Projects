board = ['0','1','2','3','4','5','6','7','8','9']

def display_board(board):

    print('\n')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(board[1],board[2],board[3]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(board[4],board[5],board[6]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(board[7],board[8],board[9]))
    print('\t     |     |')
   

   

def player_input():
    marker = ''
    input_choices = ['1','2']
    #Input validation
    while marker not in input_choices:
        marker = input('Please enter 1 for "X" or 2 for "O": ')
        if marker not in input_choices:
            print('Invalid choice, please enter 1 for "X" or 2 for "O"')
        elif marker == '1':
            return ('X','O')
        elif marker == '2':
            return ('O','X')
        
def place_marker(board,marker,position):
    board[position] = marker
    
    
place_marker(board,'X',5)
print(display_board(board))
#player_input()