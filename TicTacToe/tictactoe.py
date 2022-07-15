def display_board(board):
    #Using pa to represent play area here
    pa = [' ','1','2','3','4','5','6','7','8','9']
    print('\n')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(pa[1],pa[2],pa[3]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(pa[4],pa[5],pa[6]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t   {} |  {}  |  {} '.format(pa[7],pa[8],pa[9]))
    print('\t     |     |')

def player_input():
    #Initial Variables
    
    #Dictionary to hold playing tokens to choose from
    token_choice_store = {'X':'','O':''}
    
    #List of values to use for input validaton
    input_validation_list = [1,2]
    
    #Ask for token choice X or O
    #Idea for update is to personalize this with formatting
    selection = int(input('Please enter 1 for "X" or 2 for "O": '))
    
    #Player variables
    player1 = ' '
    player2 = ' '
    default_player = player1
    
    #Input validation
    while selection not in input_validation_list:
        selection = int(input('Please enter 1 for "X" or 2 for "O": '))
        #Check if player selection is valid
        if selection not in input_validation_list:
            print('Invalid choice, please enter 1 for "X" or 2 for "O": ')
        elif selection == 1:
            token_choice_store['X'] = player1
            if default_player == player1:
                token_choice_store['O'] = player2
            else:
                token_choice_store['O'] = player1
                            
    print(player1)

player_input()