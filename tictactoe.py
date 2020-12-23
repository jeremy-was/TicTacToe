p1_name = ''
p2_name = ''
continue_game = True
actual_moves = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1_turn = True
p2_turn = False

def game_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def players():

    global p1_name 
    global p2_name 
    global p1_turn
    global p2_turn

    p1_turn = True
    p2_turn = False

    print('\n'*30)
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Welcome to a crappy version of Tic Tac Toe!, created by Mukas')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('\n'*3)

    p1_name = input("Player 1, enter your name: ")
    print(f"\nHello {p1_name}, you will be playing first as O")

    p2_name = input("\nPlayer 2, enter your name: ")
    print(f"\nHello {p2_name}, you will be playing second as X")

    game_board(actual_moves)

# from IPython.display import clear_output

def game_play(p1_name,p2_name):
    p1_piece = 'O'
    p2_piece = 'X'
    global p1_turn
    global p2_turn
    global continue_game
    moves = 0

    while p1_turn and continue_game and moves < 9:
        p1_move = (input(f"\n{p1_name}, Enter your move (1-9) "))
        
        if p1_move == 'q' or p1_move == 'Q':
            p1_turn = True
            p2_turn = False
            quit_game()
        
        elif p1_move.isdigit() == False:
            print('\n'*30)
            game_board(actual_moves)
            print("\nEnter digits only")  
            
        elif int(p1_move) not in range(1,10):
            print('\n'*30)
            game_board(actual_moves)
            print("\nMust be in range 1-9")
            
        elif actual_moves[int(p1_move)] != ' ':
            print('\n'*30)
            game_board(actual_moves)
            print("\nAlready taken. Choose another number")
        
        else:
            actual_moves[int(p1_move)] = p1_piece
            # clear_output()
            print('\n'*30)
            game_board(actual_moves)
            p1_turn = False
            p2_turn = True
            moves += 1
            winner_check_p1()
            
        while p2_turn and continue_game and moves < 9:
            p2_move = (input(f"\n{p2_name}, Enter your move (1-9) "))
            
            if p2_move == 'q' or p2_move == 'Q':
                p2_turn = True
                p1_turn = False
                quit_game()

            elif p2_move.isdigit() == False:
                print('\n'*30)
                game_board(actual_moves)
                print("\nEnter digits only")  

            elif int(p2_move) not in range(1,10):
                print('\n'*30)
                game_board(actual_moves)
                print("\nMust be in range 1-9")

            elif actual_moves[int(p2_move)] != ' ':
                print('\n'*30)
                game_board(actual_moves)
                print("\nAlready taken. Choose another number")

            else:
                actual_moves[int(p2_move)] = p2_piece
                # clear_output()
                print('\n'*30)
                game_board(actual_moves)
                p1_turn = True
                p2_turn = False
                moves += 1
                winner_check_p2()

def winner_check_p1():

    if actual_moves[1]=='O' and actual_moves[2]=='O' and actual_moves[3]=='O':
        winner_output_p1()
    elif actual_moves[4]=='O' and actual_moves[5]=='O' and actual_moves[6]=='O':
        winner_output_p1()
    elif actual_moves[7]=='O' and actual_moves[8]=='O' and actual_moves[9]=='O':
        winner_output_p1()
    elif actual_moves[7]=='O' and actual_moves[4]=='O' and actual_moves[1]=='O':
        winner_output_p1()
    elif actual_moves[8]=='O' and actual_moves[5]=='O' and actual_moves[2]=='O':
        winner_output_p1()
    elif actual_moves[9]=='O' and actual_moves[6]=='O' and actual_moves[3]=='O':
        winner_output_p1()
    elif actual_moves[1]=='O' and actual_moves[5]=='O' and actual_moves[9]=='O':
        winner_output_p1()
    elif actual_moves[7]=='O' and actual_moves[5]=='O' and actual_moves[3]=='O':
        winner_output_p1()
    elif ' ' not in actual_moves:
        draw_output()
        
def winner_output_p1():
    print(f'\n{p1_name} is the winner! Well done!')
    global p1_turn
    p1_turn = False
    global p2_turn
    p2_turn = False
    play_again()

def winner_check_p2():
    if actual_moves[1]=='X' and actual_moves[2]=='X' and actual_moves[3]=='X':
        winner_output_p2()
    elif actual_moves[4]=='X' and actual_moves[5]=='X' and actual_moves[6]=='X':
        winner_output_p2()
    elif actual_moves[7]=='X' and actual_moves[8]=='X' and actual_moves[9]=='X':
        winner_output_p2()
    elif actual_moves[7]=='X' and actual_moves[4]=='X' and actual_moves[1]=='X':
        winner_output_p2()
    elif actual_moves[8]=='X' and actual_moves[5]=='X' and actual_moves[2]=='X':
        winner_output_p2()
    elif actual_moves[9]=='X' and actual_moves[6]=='X' and actual_moves[3]=='X':
        winner_output_p2()
    elif actual_moves[1]=='X' and actual_moves[5]=='X' and actual_moves[9]=='X':
        winner_output_p2()
    elif actual_moves[7]=='X' and actual_moves[5]=='X' and actual_moves[3]=='X':
        winner_output_p2()
    elif ' ' not in actual_moves:
        draw_output()
        
def winner_output_p2():
    print(f'\n{p2_name} is the winner! Well done!')
    global p1_turn
    p1_turn = False
    global p2_turn
    p2_turn = False
    play_again()

def draw_output():
    print(f"\nIt's a draw! Well done {p1_name} and {p2_name}!")
    global p1_turn
    p1_turn = False
    global p2_turn
    p2_turn = False
    play_again()

def quit_game():
    
    quit_me = True
    global continue_game
    
    while quit_me:
        
        leave = (input('\nDo you want to quit the game? y/n: '))
        if leave != 'y' and leave != 'Y' and leave != 'N' and leave != 'n':
            print('\nPlease enter y or n')
            quit_me = True
        elif leave == 'n' or leave == 'N':
            game_play(p1_name,p2_name)
            quit_me = False
        elif leave == 'y' or leave == 'Y':
            quit_me = False
            continue_game = False
            print('\n'*30)
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            print('\nSorry to see you quit. Thanks for playing Tic Tac Toe, from Mukas\n')
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

def play_again():

    play_true = True
    global actual_moves
    
    while play_true:
        play = (input('\nDo you want to play again? y/n: '))
        if play != 'y' and play != 'Y' and play != 'N' and play != 'n':
            print('\nPlease enter y or n')
            play_true = True
        elif play == 'y' or play == 'Y':
            switch_players()
            play_true = False
        elif play == 'n' or play == 'N':
            print('\n'*30)
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            print('\nThanks for playing Tic Tac Toe, from Mukas\n')
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            play_true = False
            pass

def switch_players():
    
    switch_true = True
    global actual_moves
    global p1_turn
    global p2_turn
    
    while switch_true:
        switch = (input('\nDo you want to switch players? y/n: '))
        if switch != 'y' and switch != 'Y' and switch != 'N' and switch != 'n':
            print('\nPlease enter y or n')
            switch_true = True
        elif switch == 'y' or switch == 'Y':
            switch_true = False
            actual_moves = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            game_board(actual_moves)
            players()
            game_play(p1_name,p2_name)
        elif switch == 'n' or switch == 'N':
            switch_true = False
            actual_moves = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            p1_turn = True
            p2_turn = False
            print('\n'*30)
            game_board(actual_moves)
            game_play(p1_name,p2_name)

# game_board(actual_moves)
players()
game_play(p1_name,p2_name)