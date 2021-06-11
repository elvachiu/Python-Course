#lecture 3 practices 0415

from random import randint

# Read an integer which is in {0,...,9}
def read_a_digit():
    ret = -1
    while True:
        try:
            ret = int(input('Input a digit(0~9): '))
        except ValueError:
            print('Not an integer')
            continue
        if ret >= 0 and ret <= 9:
            return ret
        print(ret,'is not in {0,...,9}.')

ans = randint(0,9)
guess = read_a_digit()
while guess != ans:
    print(guess,'is not the answer')
    guess = read_a_digit()
print('Congrats! The answer is',ans)
