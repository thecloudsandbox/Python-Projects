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
    #Input Variable
    #player1_choice = 'PLACEHOLDER'
    valid_range = range(1,10)
    input_range = False
    player_1 = ' '
    player_2 = ' '
    #Input validation
    while player_1.isdigit() == False or input_range == False:
        
        #Asking for initial input
        player_1 = input('Choose a position to place your token')
        
        #Check if a number or letter was entered and if not a number print to the screen
        if player_1.isdigit() == False :
            print('Invalid choice, choose between 1 - 9')
            
        #Checking if input is in range between 1-9
        if player_1.isdigit():
            if str(player_1) in valid_range:
                input_range = True
            else:
                print('Number not in range, choose between 1 - 9')
                
        
    print(player_1)

player_input()