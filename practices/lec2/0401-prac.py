import pyautogui, time
from itertools import combinations

#practice for Midterm Project

pyautogui.FAILSAFE = True

def click_all_position(pic):
    loc = pyautogui.locateOnScreen(pic)
    #check 20 times, if no pics at all, return none
    for i in range(20): 
        if loc != None: 
            break
        time.sleep(0.1)
    if loc == None:
        return none
    all_pairs_loc = combinations(pyautogui.locateAllOnScreen(pic, confidence = 0.95), 2)
    for pair in all_pairs_loc:
        loc_1, loc_2 = pair
        print(pic, 'is at', loc_1, 'and', loc_2)
        center = pyautogui.center(loc_1)
        pyautogui.click(center)
        center = pyautogui.center(loc_2)
        pyautogui.click(center)

time.sleep(10)
'''
for i in range(10):
    click_all_position('snake.png')
    click_all_position('bird.png')
'''

#task - debug it
import pyautogui, time

color = None

def report():
    loc = pyautogui.position()
    color = pyautogui.screenshot().getpixel(loc)
    print("position is:", loc, "color is", color)
    return color #add this line to debug

while True:
    report()
    time.sleep(0.5)
    if color == (139, 0, 0):
        break
