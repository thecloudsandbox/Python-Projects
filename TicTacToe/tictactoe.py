import random

def display_board(board):

    print('\n'*100)
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
    
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[7] == mark and board[8] == mark and board[8] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))
    
def choose_first():
    player_choser = random.randint(1,2)
    
    if player_choser == 1:
        return player1
    else:
        return player2

def space_check(board, position):
    if board[position] != ' ':
        return False
    else:
        return position

def full_board_check(board):
    for b in board:
        if b == 'X' or b == 'O':
            return True
        else:
            return False 

def player_choice(board):
    #Ask for player position
    position = int(input('Choose a position between 1 - 9'))
    
    #Check if position is available
    check = space_check(board,position)
    
    return check

def replay():
    play = 0 
    
    while play == 0:
        play_again = input('Press 1 to play again')
        if play_again == 1:
            return True
        else:
            break


print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn,' will go first')
    
    game_on = True

    while game_on:
        #Player 1 Turn
        if turn == player1:
            
            display_board(board)
            print('Player 1')
            position = player_choice(board)
            place_marker(board,player1,position)
            
            if win_check(board,player1):
                display_board(board)
                print('Player 1 won the game')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('There were no victors!')
                    break
                else:
                    turn = player2
        else:
        
        # Player2's turn.
            display_board(board)
            print('Player 2')
            position = player_choice(board)
            place_marker(board,player2,position)
            
            if win_check(board,player2):
                display_board(board)
                print('Player 2 won the game')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('There were no victors!')
                    break
                else:
                    turn = player1 

    if not replay():
        break