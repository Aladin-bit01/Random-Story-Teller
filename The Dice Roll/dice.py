import random



#The argument of this function is the amount of times the function should roll the dice
def dice_roller(amount):
    if amount <= 0:
        raise ValueError
    else:
        dices= []
        while len(dices) < amount:
            r= random.randint(1,6)
            dices.append(r)
        return dices

def main():
    while True:
        try:
            user = input('How many rolls of the dice do you want me to do? ')
            if user.lower() == 'exit':
                print('Thanks for playing')
                break
            x = dice_roller(int(user))
        except ValueError:
            print('please enter a valid number')
            continue

        else:
            print(*x, sep= ', ')
            print('total:', sum(x))



if __name__ == '__main__':
    main()