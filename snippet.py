import random

def play():
    
    user = input('What\'s your choice? r for rock, p for paper, s for scissors: ').lower()
    computer = random.choice(['r', 'p', 's'])
   

    if user == computer:
        return 'It\'s a tie!'
    
    if is_win(user, computer):
        return 'You Won!'
    """
    return 'You Lose!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
"""
    while computer != user:
        if (computer == 'r' and user == 's') or (computer == 's' and user == 'p') or (computer == 'p' and user == 'r'):
            print('You Lost!')

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
print(play())