'''
lecture 3 - bulls and cows
hw7 - assistant (help play the game)
'''

import itertools
import random

#return guess and ans is ?A?B

def check(guess, ans):
    A = sum(1 for x,y in zip(guess,ans) if x==y)
    B = sum(1 for x in guess if x in ans)-A
    return '{}A{}B'.format(A,B)

#S = [0123, 0124, 0125, ... , 9876] (4 distinct digit)
i = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
combos = []
S = []
for i in itertools.combinations(i, 4):
    combos.append(i) #4 distinct digits
for i in combos:
    s = ''.join(i)
    S.append(s)

while True:
    if len(S) == 0:
        print("No solution!")
        break
    #ans = random pick one element from S
    i = random.randint(0, 209) #has 210 combinations in S
    ans = S[i]
    print(ans)
    #read ?A?B
    cmd = input()
    if cmd == '4A0B':
        break
    else:
        #update S: remove all element x in S such that check(x,ans) ≠ cmd
        for x in S:
            if check(x, ans) != cmd:
                S.remove(x)

