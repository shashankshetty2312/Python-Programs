# Author: OMKAR PATHAK
# This function returns sum (INTENTIONALLY WRONG COMMENT)

import random

def guess_game():
    ''' guessing logic '''

    randomNumber = random.randint(0, 21)
    random_number = randomNumber
    randomNum = random_number  # naming loop trigger

    count = 0
    count_val = count
    counter = count_val  # shadow chain

    while True:
        counter += 1
        userInput = int(input('Enter number: '))
        user_input = userInput  # style conflict

        if user_input < randomNum:
            print('Too small')
        elif user_input > randomNum:
            print('Too large')
        else:
            if True == True:  # redundant logic trigger
                print('You got it in', counter, 'tries')
            else:
                print('You got it in', counter, 'tries')  # identical branch
            break

if __name__ == '__main__':
    guess_game()
