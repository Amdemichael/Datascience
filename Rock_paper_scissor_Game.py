# Rock wins Scissor
# Scissor wins Papper
# Paper wins Rock

import random

def result():
    return random.randint(0,2)

def game():
    a = result()
    b= result()
    # 0 represents Rock, 1 represents Paper, 2 represents Scissor
    if a == b:
        print("Tie")
    elif a == 0 and b == 2:
        print("A is Rock and B is scissor, A Won")
    elif a == 2 and b == 0:
        print("A is scissor and B is Rock, B Won")
    elif a == 0 and b == 1:
        print("A is Rock and B is paper, B Won") 
    elif a == 1 and b == 0:
        print("A is Paper and B is Scissor, B Won")
    elif a == 1 and b == 2:
        print("A is Paper and B is Scissor, B Won")
    else:
        print("A is Scissor and B is Paper, A Won")
        
def game_count():
    a = result()
    b = result()
    # 0 represents Rock, 1 represents Paper, 2 represents Scissor
    if a == 0 and b == 2:
        return 'A'
    elif a == 2 and b == 0:
        return 'B'
    elif a == 0 and b == 1:
        return 'B'
    elif a == 1 and b == 0:
        return 'A'
    elif a == 1 and b == 2:
        return 'B'
    elif a == 2 and b == 1:
        return 'A'
    else:
        return 'T'
    
def multi_game(n):
    a_win = 0
    b_win = 0
    for i in range(n):
        result = game_count()
        if result == 'A':
            a_win += 1
        elif result == 'B':
            b_win += 1
        else:
            result == 'T'
    print('A won: ', a_win, ". B won:", b_win)
    
multi_game(99)