import random

minimum = 1
maximum = 100
TOO_HIGH = 'TOO HIGH'
TOO_LOW = 'TOO LOW'
CORRECT = 'CORRECT'
GAME_OVER = 'GAME OVER'
YOU_WIN = 'YOU WIN'



def secret_number(seed):
    random.seed(seed)
    return  random.randint(minimum,maximum)

def check_guess(n,a):
    if (a < n) :
        return TOO_LOW
    if (a == n):
        return CORRECT
    if (a > n):
     return TOO_HIGH
    
def prompt_for_guess(s,i):
    print(i)
    print(check_guess(s,i))
    return check_guess(s,i)

def game():
    se = int(input('Enter seed  '))
    s = secret_number(se)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    i = int(input('Enter a value    '))
    if prompt_for_guess(s,i) == CORRECT:
        return print(YOU_WIN)
    
    return print('The number is ',s,GAME_OVER)


def main():
    game()
    a = input('Do you want to play again (y/n): ')
    assert a == 'y' or a == 'n' , 'enter only y or n'
    if a == 'y':
        game()
    
if __name__ == '__main__':
    main()