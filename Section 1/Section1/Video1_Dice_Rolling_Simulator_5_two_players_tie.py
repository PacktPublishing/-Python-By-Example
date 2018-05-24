'''
Created on Mar 29, 2018

@author: Burkhard A. Meier
'''




''' Two players using functions '''
from random import randint   

def dice_game(player=1, num_of_rolls=100):
    dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    total_score = 0
    
    for _roll in range(num_of_rolls):
        number_rolled = randint(1, 6)           
        dice_dict[number_rolled] += 1
        total_score += number_rolled
    
    lines = '=' * 9    
    print('\n{}\nPlayer {}:\n{} \n{}'.format(lines, player, lines, dice_dict))        
    print('\nTotal Score: {} \n{}'.format(total_score, '=' * 16))  
    
    return total_score


def print_result(score_1, score_2):
    lines_result = '=' * 21
    print('\nResult:\n' + lines_result)
    
    if score_1 > score_2:
        print('*** Player 1 won! ***')
    elif score_1 < score_2:
        print('*** Player 2 won! ***')
    else:
        print('*** Tie! ***')
        
    print(lines_result)  


def play_one_game():
    score_1 = dice_game(player=1) 
    score_2 = dice_game(player=2)
    print_result(score_1, score_2)
    return score_1, score_2

# ---------------------------------
# play_one_game() 


''' Play the game in a loop until Tie! '''   
def play_until_tie(max_games=100):                          # default games limit to 100
    games_played = 0                                        # create variable
    tie = False
    while (not tie) and (games_played < max_games): 
        games_played +=1                                    # increase variable
        print('\n\n*** Dice Game:', games_played, '***')
        score_1, score_2 = play_one_game() 
        
        if score_1 == score_2:
            tie = True
    #---------------------------
    if games_played < max_games:
        print('\n*** It took {} Dice games to reach a tie ***'.format(games_played))
    else:
        print('\n*** No tie after {} games of Dice ***'.format(games_played))
    
# ---------------------------------
play_until_tie()
# play_until_tie(20)      # limit games to 20
