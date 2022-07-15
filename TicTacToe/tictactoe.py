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
    token_choice = ['X','O']
    
    #List of values to use for input validaton
    input_validation_list = [1,2]
    selection = 0
    input_valid_range = range(3)
    #Input validation
    while selection not in input_validation_list and input_valid_range:
        #Error handling for input
        player_input = input('Please enter 1 for "X" or 2 for "O": ')
        try:
            selection = int(player_input)
        except ValueError:
            print('You entered an invalid character: ',player_input)
        
        #Assigning tokens to players
        if selection == 1:
            player1 = token_choice[0]
            if player1 == token_choice[0]:
                player2 = token_choice[1]
        elif selection == 2:
            player1 = token_choice[1]
            if player1 == token_choice[1]:
                player2 = token_choice[0]
                
    print(player1,player2)

player_input()