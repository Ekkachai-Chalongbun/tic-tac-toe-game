# PROJECT A RAI WA NEARRRR

import os

from random import randrange

from random import choice

# clear screen function
cls = lambda: os.system('cls')

# function to show the board for playing
def show_board():
    # the best tic tac toe board in this fking world
    board = \
    '''
    1  |2  |3
       |   |
       |   |
    -----------
    4  |5  |6
       |   |
       |   |
    -----------
    7  |8  |9
       |   |
       |   |
    '''

    print("\nHere is how the board looks like:\n", board)

# function to get input at the beginning part of game(user and bot side, difficulty level)
def game_begin():
    # input user side
    user_side = input("Choose your side('x' or 'o'):\n")

    if user_side == 'X':
        user_side = 'x'

    elif user_side == 'O':
        user_side = 'o'

    while(user_side != 'x' and user_side !='o'):
        user_side = input("Please choose only 'x' or 'o':\n")

    # define bot side
    if user_side == 'x':
        bot_side = 'o'

    else:
        bot_side = 'x'

    # input bot level
    level = input("\nChoose the bot level! : 0(for noobs) | 1(for normal level) | 999(to fight our supreme god bot system)\n")

    while(level != '0' and level != '1' and level !='999'):
        level = input("\nHey!, choose only our provided level please : 0 | 1 | 999\n")

    if level == '0':
        print("\nNerd bot mode: win = 1 point | tie = 0 point | lose = 0 point")

    elif level == '1':
        print("\nNormal bot mode: win = 2 point | tie = 1 point | lose = 0 point")

    else:
        print("\nGod bot mode: win = 999 point :) | tie = 1 point | lose = 0 point")

    return(user_side, bot_side, level)

# random turn function
def decide_turn():
    print("\nTurn will be provided by random\n.\n.\n.")

    user_turn = randrange(2) + 1

    if user_turn == 1 :
        print ("You go first!")
        bot_turn = 2

    else:
        print ("You go second!")
        bot_turn = 1
        
    return(user_turn, bot_turn)

# function for user play
def user_play(user_side, board_block, user_last_corner):
    user_move = input("Choose an empty block to play(1-9):\n")
    
    check_range = False
    check_empty = False
    
    while not(check_range and check_empty):
        if not user_move.isnumeric():
            check_range = False
            user_move = input("Please pay attention... choose only 1-9!\n")
            
        elif ((int(user_move) > 9) or (int(user_move) < 1)):
            check_range = False
            user_move = input("Please pay attention... choose only 1-9!\n")

        elif (board_block[int(user_move)] != ' '):
            check_range = True
            check_empty = False
            user_move = input("That block is not empty... be serious!, choose new number:\n")

        else:
            check_range = True
            check_empty = True        
    
    if int(user_move) in [1, 3, 7, 9]:
        user_last_corner == user_move
    
    board_block[int(user_move)] = user_side
        
    return(int(user_move))

# function for bot play
def bot_play(level, bot_side, board_block, count_turns, user_side, user_last_corner):    
    # current board
    current_board = list(board_block.values())

    # use only empty blocks
    empty_board = []

    i = 0

    for x in current_board:
        i = i+1
        if x == ' ':
            empty_board.append(i)
   
    if level == '0': #level 0 bot just random move 
        bot_move = choice(empty_board)

    elif level == '1': #level 1 bot use normal move
        # play corner when bot goes first
        if count_turns == 1:
            bot_move = choice([1, 3, 7, 9])

        else:
            # check for winning move
            can_win, bot_move = win_move(current_board, empty_board, bot_side)

            # check for defending move
            if not can_win:    
                can_defend, bot_move = defend_move(current_board, empty_board, user_side)

            # just pick random when can't win nor defend
            if ((not can_win) and (not can_defend)):        
                bot_move = choice(empty_board)   

    else: #level 999 bot use best move
        bot_move = find_best_move(current_board, empty_board, count_turns, bot_side, user_side, user_last_corner)
        
    board_block[bot_move] = bot_side
            
    return(int(bot_move))

# function to check for winning move  
def win_move(current_board, empty_board, bot_side):
    can_win = False

    bot_move = 404
    
    # horizontal win
    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+1] == bot_side:
            if (i+3) in empty_board:
                bot_move = i+3

                can_win = True

    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+2] == bot_side:
            if (i+2) in empty_board:
                bot_move = i+2

                can_win = True

    for i in [1, 4, 7]:
        if current_board[i] == current_board[i+1] == bot_side:
            if (i) in empty_board:
                bot_move = i

                can_win = True
    
    # vertical win
    for i in [0, 1, 2]:
        if current_board[i] == current_board[i+3] == bot_side:
            if (i+7) in empty_board:
                bot_move = i+7

                can_win = True

    for i in [0, 1, 2]:
        if current_board[i] == current_board[i+6] == bot_side:
            if (i+4) in empty_board:
                bot_move = i+4

                can_win = True

    for i in [3, 4, 5]:
        if current_board[i] == current_board[i+3] == bot_side:
            if (i-2) in empty_board:
                bot_move = i-2

                can_win = True
    
    # diagonal win
    for i in [0, 2]:
        if current_board[i] == current_board[4] == bot_side:
            if (9-i) in empty_board:
                bot_move = 9-i

                can_win = True

    for i in [0, 2]:
        if current_board[4] == current_board[8-i] == bot_side:
            if (i+1) in empty_board:
                bot_move = i+1

                can_win = True

    for i in [0, 2]:
        if current_board[i] == current_board[8-i] == bot_side:
            if (5) in empty_board:
                bot_move = 5

                can_win = True

    return(can_win, bot_move)
    
# function to check for defending move
def defend_move(current_board, empty_board, user_side):            
    can_defend = False

    bot_move = 404
    
    # horizontal defend
    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+1] == user_side:
            if (i+3) in empty_board:
                bot_move = i+3

                can_defend = True

    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+2] == user_side:
            if (i+2) in empty_board:
                bot_move = i+2

                can_defend = True

    for i in [1, 4, 7]:
        if current_board[i] == current_board[i+1] == user_side:
            if (i) in empty_board:
                bot_move = i

                can_defend = True
    
    # vertical defend
    for i in [0, 1, 2]:
        if current_board[i] == current_board[i+3] == user_side:
            if (i+7) in empty_board:
                bot_move = i+7

                can_defend = True

    for i in [0, 1, 2]:
        if current_board[i] == current_board[i+6] == user_side:
            if (i+4) in empty_board:
                bot_move = i+4

                can_defend = True

    for i in [3, 4, 5]:
        if current_board[i] == current_board[i+3] == user_side:
            if (i-2) in empty_board:
                bot_move = i-2

                can_defend = True
    
    # diagonal defend
    for i in [0, 2]:
        if current_board[i] == current_board[4] == user_side:
            if (9-i) in empty_board:
                bot_move = 9-i

                can_defend = True

    for i in [0, 2]:
        if current_board[4] == current_board[8-i] == user_side:
            if (i+1) in empty_board:
                bot_move = i+1

                can_defend = True

    for i in [0, 2]:
        if current_board[i] == current_board[8-i] == user_side:
            if (5) in empty_board:
                bot_move = 5

                can_defend = True
        
    return (can_defend, bot_move)
  
# function to find free corner    
def free_corner(current_board):
    free_list = []
    
    for i in [0, 2, 6, 8]:
        if current_board[i] == ' ':
            free_list.append(i)
            
    if not free_list: # no possible corner
        return 404

    else: # play one corner from all possible
        return choice(free_list)+1

# function to find free edge
def free_edge(current_board):
    free_list = []
    
    for i in [1, 3, 5, 7]:
        if current_board[i] == ' ':
            free_list.append(i)   
            
    if not free_list: # no possible edge
        return 404

    else: # play one corner from all possible
        return choice(free_list)+1

# function to find free space
def free_space(current_board):
    free_list = []
    
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if current_board[i] == ' ':
            free_list.append(i)   
            
    if not free_list: # no possible space?
        return 404

    else: # play one corner from all possible
        return choice(free_list)+1

# function to check if user has opposite corners
def user_opposite_corners(current_board, user_side):
    opposite = False
    
    if current_board[0] == current_board[8] == user_side:
        opposite = True

    if current_board[2] == current_board[6] == user_side:
        opposite = True
            
    return opposite

# function to find best move 
def find_best_move(current_board, empty_board, count_turns, bot_side, user_side, user_last_corner):
    # IF BOT GOES FIRST(focus on winning)

    # turn1 play 1 because it's powerful
    if count_turns == 1:
        bot_move = 1

    # turn3 play 9 or 3 to make connection to 1
    if count_turns == 3:
        if 9 in empty_board:
            bot_move = 9

        else:
            bot_move = 3    

    # turn5 and turn7 check all possible conditions to win if can, defend if can't      
    if (count_turns == 5) or (count_turns == 7):
        can_win, bot_move = win_move(current_board, empty_board, bot_side)

        if not can_win:
            can_defend, bot_move = defend_move(current_board, empty_board, user_side)

            if (not can_win) and (not can_defend):
                corner = free_corner(current_board)

                if (corner != 404):
                    bot_move = corner

                    if (not can_win) and (not can_defend) and (corner == 404):
                        space = free_space(current_board)

                        bot_move = space

    # turn9 have only a space left
    if count_turns == 9:
        space = free_space(current_board)

        bot_move = space
        
    # IF BOT GOES SECOND(focus on defending)

    # turn2 play 5. if can't, hold free corner
    if count_turns == 2:
        if current_board[4] == ' ':
            bot_move = 5

        else:
            corner = free_corner(current_board)

            bot_move = corner

    # turn4 check all conditions to defend only because bot can lose next turn if bot try to win first  
    if count_turns == 4:
        can_defend, bot_move = defend_move(current_board, empty_board, user_side)

        if (not can_defend):
            opposite = user_opposite_corners(current_board)

            if opposite:
                bot_move = free_edge(current_board)

        if ((not can_defend) and (not opposite)):
            if (user_last_corner != 404):
                corner = 10 - user_last_corner

                if (corner in empty_board):
                    bot_move = corner

        if ((not can_defend) and (not opposite) and ((user_last_corner == 404) or ((10-user_last_corner)not in empty_board))):
            corner = free_corner(current_board)

            bot_move = corner

    # turn6 and turn8 now bot can check all conditions to win if can, still defend if can't
    if (count_turns == 6) or (count_turns == 8):
        can_win, bot_move = win_move(current_board, empty_board, bot_side)

        if (not can_win):
            can_defend, bot_move = defend_move(current_board, empty_board, user_side)

            if ((not can_win) and (not can_defend)):
                corner = free_corner(current_board)

                bot_move = corner

                if ((not can_win) and (not can_defend) and (corner==404)):
                    space = free_space(current_board)

                    bot_move = space
    
    return bot_move

# function to show updated board  
def show_updated_board(board_block):
    print ('''
           {}  |{}  |{}  
              |   |
              |   |   
           -----------
           {}  |{}  |{}  
              |   |
              |   |   
           -----------
           {}  |{}  |{}  
              |   |
              |   |   
           '''.format(board_block[1], board_block[2], board_block[3], 
           board_block[4], board_block[5], board_block[6], 
           board_block[7], board_block[8], board_block[9]))

# function to check when the board is fulled
def check_full(board_block):   
    full = True
    
    for i in board_block :
        if board_block[i] == ' ':
            full = False

    return full

# function to check result of game
def check_win(board_block, user_side, level, full):   
    x_win = False

    o_win = False

    win = False

    score = 0
    
    for letter in ['x', 'o']:
        # check horizontal win
        for i in [1, 4, 7]:
            if (board_block[i] == board_block[i+1] == board_block[i+2] == letter):
                win = True
                if letter == 'x':
                    x_win = True

                else:
                    o_win = True
                
        # check vertical win
        for i in [1, 2, 3]:
            if (board_block[i] == board_block[i+3] == board_block[i+6] == letter):
                win = True
                if letter == 'x':
                    x_win = True

                else:
                    o_win = True
                    
        # check diagonal win
        for i in [1, 3]:     
            if (board_block[i] == board_block[5] == board_block[10-i] == letter):
                win = True
                if letter == 'x':
                    x_win = True

                else:
                    o_win = True
                   
    if x_win:
        if user_side == 'x':
            print("\n~~~~~~ Congratulations! you have won this game!!! ~~~~~~\n")

            if level == '0':
                print("\n~~~~~~ You got 1 point(s)!! ~~~~~~\n")

                score += 1

            elif level == '1':
                print("\n~~~~~~ You got 2 point(s)!! ~~~~~~\n")

                score += 2

        else:
            print("\n~~~~~~ Unlucky! you have lost this game... ~~~~~~\n")

            print("\n~~~~~~ You got 0 point(s).. ~~~~~~\n")

    elif o_win:
        if user_side == 'o':
            print("\n~~~~~~ Congratulations! you have won this game!!! ~~~~~~\n")

            if level == '0':
                print("\n~~~~~~ You got 1 point(s)!! ~~~~~~\n")

                score += 1
            
            if level == '1':
                print("\n~~~~~~ You got 2 point(s)!! ~~~~~~\n")

                score += 2

        else:
            print("\n~~~~~~ Unlucky! you have lost this game... ~~~~~~\n")

            print("\n~~~~~~ You got 0 point(s).. ~~~~~~\n")

    elif full and (not win):
        print("\n~~~~~~ Ahhhhh! the result is tie. ~~~~~~\n")

        if level == '0':
                print("\n~~~~~~ You got 0 point(s).. ~~~~~~\n")

        elif level == '1' or level == '2':
                print("\n~~~~~~ You got 1 point(s)!! ~~~~~~\n")

                score += 1
        
    return (win, score)

# playing loops
def user_loop(user_side, board_block, user_last_corner, level):
    print ("\n\nUser's turn:")

    block = user_play(user_side, board_block, user_last_corner)

    show_updated_board(board_block)

    print("You played at block[%d]" %block)

    full = check_full(board_block)

    win, score = check_win(board_block, user_side, level, full)
    
    return(full, win, score)

def bot_loop(level, user_side, bot_side, board_block, count_turns, user_last_corner):
    print ("\n\nBot's turn:")

    block = bot_play(level, bot_side, board_block, count_turns, user_side, user_last_corner)

    show_updated_board(board_block)

    print("Bot played at block[%d]" %block)

    full = check_full(board_block)

    win, score = check_win(board_block, user_side, level, full)
    
    return (full, win, score)

# function to check if user want to play again or not
def play_again():
    play_again = input("This is so much fun right? ^___^ I'm so happy playing with you.\nDo you want to play again? ('y' for yes, 'n' for no):\n")

    while ((play_again != 'Y' and play_again !='y') and (play_again !='N' and play_again!='n')):
        play_again = input("Erghhhhh, Please please please pick our provided letter!(y or n):\n")
    
    if play_again == 'Y' or play_again == 'y':
        cls()
        again = True

    elif play_again == 'N' or play_again == 'n':
        again = False
    
    return again

# The main game section
def main():
    cls()

    new_game = True

    global_score = 0

    while new_game:
        print("\tTic Tac Toe Time!!!")
  
        # showing board for playing
        show_board()

        # make new board empty
        board_block = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

        # get each side and difficulty level at the beginning part
        user_side, bot_side, level = game_begin()

        # decide turn
        user_turn, bot_turn = decide_turn()
        
        # re-declare used values
        count_turns = 0

        user_last_corner = 404

        if user_turn == 1: # let user play first if their turn is 1
            count_turns += 1

            full, win, score = user_loop(user_side, board_block, user_last_corner, level)

            global_score += score

        while True: # then play the bot
            count_turns += 1

            full, win, score = bot_loop(level, user_side, bot_side, board_block, count_turns, user_last_corner)

            global_score += score

            if full or win:
                again = play_again()

                if again:
                    print("Your score now: %d\n" %global_score)

                    print("~~~~~~  New game started!!!  ~~~~~~\n")

                else:
                    print("\n~~~~~~ Thank you for playing our game! ~~~~~~\n")

                    print("-------------------------\n|\t\t\t|")
                    print("| Your final score is %d |" %global_score)
                    print("|\t\t\t|\n-------------------------\n")

                    new_game = False

                break

            count_turns += 1

            full, win, score = user_loop(user_side, board_block, user_last_corner, level)

            global_score += score

            if full or win:
                again = play_again()

                if again:
                    print("Your score now: %d\n" %global_score)

                    print("~~~~~~  New game started!!!  ~~~~~~\n")

                else:
                    print("\n~~~~~~ Thank you for playing our game! ~~~~~~\n")

                    print("-------------------------\n|\t\t\t|")
                    print("| Your final score is %d |" %global_score)
                    print("|\t\t\t|\n-------------------------\n")

                    new_game = False

                break
    return global_score


if __name__ == '__main__':
    main()
