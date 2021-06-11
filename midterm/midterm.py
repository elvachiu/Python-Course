'''
Python Application - Midterm Project
0713462 IMF11
'''

import pyautogui, snp, time
from time import sleep
from itertools import combinations
pyautogui.FAILSAFE = True

def skip_ad(pic): #check if there is the skip-ad button
    loc = snp.locateOnScreen(pic)
    for i in range(5):
        if loc != None:
            return True
        sleep(0.1)
    if loc == None:
        return False

def clickbtn(pic):
    loc = snp.locateOnScreen(pic)
    #check 3 times, if no pics at all, return none
    for i in range(3): 
        if loc != None: 
            break
        sleep(0.1)
    if loc == None:
        return None
    center = pyautogui.center(loc)
    pyautogui.click(center)

def eliminate_locs(locs): #try to eliminate the locations within the same pic
    n = len(locs)
    locs.sort()
    for i in range(n-1):
        index = []
        for j in range(i+1, n):
            if abs(locs[j][0]-locs[i][0])<=20:
                if abs(locs[j][1]-locs[i][1])<=20:
                    index.append(j)
            elif abs(locs[j][1]-locs[i][1])<=20:
                if abs(locs[j][0]-locs[i][0])<=20:
                    index.append(j)
            else: break
        index.sort(reverse = True)
        for k in index:
            locs.remove(locs[k])
        n = len(locs)
    return locs

def click_all_position(pic):
    loc = snp.locateOnScreen(pic)
    #check 3 times, if no pics at all, return none
    for i in range(3): 
        if loc != None: 
            break
        sleep(0.1)
    if loc == None:
        return None
    all_locs = [] #put in all the locs of the matching pics
    for item in snp.locateAllOnScreen(pic):
        all_locs.append(item)
    eliminate_locs(all_locs)
    all_pairs_loc = combinations(all_locs, 2)
    for pair in all_pairs_loc:
        loc_1, loc_2 = pair
        center = pyautogui.center(loc_1)
        pyautogui.click(center)
        center = pyautogui.center(loc_2)
        pyautogui.click(center)

#open up the web page
#pyautogui.press('shift') #delete '#' to change the keyboard
pyautogui.hotkey('win')
sleep(0.5)
pyautogui.typewrite('chrome')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.hotkey('win', 'up')
sleep(0.5)
pyautogui.click(300, 80)
sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
#pyautogui.press('shift') #delete '#' to change the keyboard
pyautogui.typewrite('https://html5games.com/Game/Onet-Connect-Classic/d6173a60-1b41-4b34-b4c3-aa4c5fc9ce35')
pyautogui.press('enter')
sleep(3)
pyautogui.click(950, 700) #click ok to agree
sleep(2)
clickbtn('playbtn.png') #click the play button (pyautogui.click(950, 850))
sleep(3)
clickbtn('startbtn.png') #click the green button (pyautogui.click(950, 730))
sleep(7)
clickbtn('ad.png') #skip the ad (pyautogui.click(1750, 930))
sleep(2)
pyautogui.click(950, 700) #click to start the game
sleep(2)
pyautogui.click(700, 700) #choose the animal one
sleep(2)

#start playing the game
start = time.perf_counter()
for i in range(5): 
    click_all_position('bear.png')
    click_all_position('bird.png')
    click_all_position('cat.png')
    click_all_position('crab.png')
    click_all_position('elephant.png')
    click_all_position('fox.png')
    click_all_position('frog.png')
    click_all_position('giraffe.png')
    click_all_position('koala.png')
    click_all_position('monkey.png')
    click_all_position('octopus.png')
    click_all_position('owl.png')
    click_all_position('panda.png')
    click_all_position('parrot.png')
    click_all_position('pig.png')
    click_all_position('pinky.png')
    click_all_position('rabbit.png')
    click_all_position('seal.png')
    click_all_position('snake.png')
    click_all_position('whale.png')
    end = time.perf_counter()
    if end - start >= 300.00: #play the game for over 5 mins
        break
sleep(7)
if(skip_ad('ad.png')):
    clickbtn('ad.png') #skip the ad
