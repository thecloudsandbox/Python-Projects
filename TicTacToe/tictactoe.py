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
    #List to hold playing tokens to choose from
    token_choice = ['X','O']
    marker = ''
    
    #Input validation
    while marker not in token_choice:
        #Error handling for input
        player_input = input('Please enter 1 for "X" or 2 for "O": ').upper()
        try:
            marker = int(player_input)
        except ValueError:
            print('You entered an invalid character: ',player_input)
        
        #Assigning tokens to players
        if marker == 1:
            return ('X','O')
        else:
            return ('O','X')
        
def place_marker(board,marker,position):
    board[position] = marker
    
    
place_marker(board,'X',5)
print(display_board(board))
#player_input()