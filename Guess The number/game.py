import random
import cowsay


def main():
    x,y = get_the_range()
    guessing_game(x,y)
def get_the_range():
    while True:
        try:
            lower = int(input('Enter minimum: '))
            higher= int(input('Enter maximum: '))
        except ValueError:
            print('Please insert an integer')
            continue
        else:
            return lower,higher

def guessing_game(x,y):
    print(f'You have to guess the number between {x} and {y} inclusively\nLet\'s Start Now')
    limit = 0
    rand_numb= random.randint(x,y)
    while limit < 3:
        try:
            guess= int(input('Guess: '))
        except ValueError:
            print('Please insert an integer')
            limit += 1
            continue
        else:
            if rand_numb > guess:
                print(f'The number is higher than {guess}')
                limit += 1
                if limit == 3:
                    cowsay.cow('Game Over')
                    break
            elif rand_numb < guess:
                print(f'The number is lower than {guess}')
                limit += 1
                if limit == 3:
                    cowsay.cow(f'Game Over')
                    break
            else:
                cowsay.trex('You guessed right man')
                break


if __name__ == '__main__':
    main()







