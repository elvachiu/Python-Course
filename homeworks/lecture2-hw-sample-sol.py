#lecture2 hw4 sample solution
#在背景開好小畫家放至最大

import pyautogui, time

def select_oval():
    pyautogui.moveTo(600, 90, 0.1)
    pyautogui.click()
    #pyautogui.click()

def draw_oval(left, top, height, width):
    select_oval()
    pyautogui.moveTo(left, top, 0.1)
    pyautogui.dragRel(width, height, 0.2)

def select_rect():
    pyautogui.moveTo(440, 65, 0.1)
    pyautogui.click()
    #pyautogui.click()

def draw_rect(left, top, height, width):
    select_rect()
    pyautogui.moveTo(left, top, 0.1)
    pyautogui.dragRel(width, height, 0.2)

def draw_ichimon(left, top):
    draw_oval(top, left, 100, 100)
    draw_rect(top+30, left+30, 40, 40)
pyautogui.position()
'''
for t in [200, 320]:
    for l in [100, 220, 340]:
        draw_ichimon(l, t)
'''
