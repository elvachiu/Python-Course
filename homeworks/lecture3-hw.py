'''
lecture 3 - bulls and cows
sample code - main
'''

from random import sample
from itertools import combinations

# Check whether a input is valid
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

# Read string which has four distinct digits
def read_four_distinct_digits():
    while True:
        ret = input('Input four distinct digits: ')
        if valid(ret):
            return ret
        print(ret,'is not valid.')

ans = ''.join(sample('0123456789',4))
#print(f'answer: {ans}')

guess = read_four_distinct_digits()
while guess != ans:
    A = sum(1 for x,y in zip(guess,ans) if x==y)
    B = sum(1 for x in guess if x in ans)-A
    print(guess,'is {}A{}B.'.format(A,B))
    guess = read_four_distinct_digits()

print('Congrats! The answer is',ans)
