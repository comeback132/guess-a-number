"""testing theory"""
# def do_stuff(num=0):
#     try:
#         if num or num == 0:
#             return int(num) + 5
#         else:
#             return 'please enter number'
#     except ValueError as err:
#         return err
'''Testing Exercise'''
import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius')
            return True
    else:
        print('hey bozo, I said 1¬10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1¬10:   '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
