import pyautogui, time


def select_oval():
    pyautogui.moveTo(421, 66, 0.1)
    pyautogui.click()
    pyautogui.click()


def draw_oval(top, left, height, width):
    select_oval()
    pyautogui.moveTo(left, top,0.1)
    pyautogui.dragRel(width, height, 0.2)


def select_rect():
    pyautogui.moveTo(442, 64)
    pyautogui.click()
    pyautogui.click()


def draw_rect(top, left, height, width):
    select_rect()
    pyautogui.moveTo(left, top, 0.1)
    pyautogui.dragRel(width, height)


def draw_ichimon(top, left):
    draw_oval(top, left, 100, 100)
    draw_rect(top+30, left+30, 40, 40)



pyautogui.hotkey('win', 'r')
pyautogui.typewrite('mspaint')
pyautogui.press('shift')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')
time.sleep(1)
## 小畫家開好後才可以動作的
for t in [200, 320]:
    for l in [100, 220, 340]:
        draw_ichimon(t, l)
