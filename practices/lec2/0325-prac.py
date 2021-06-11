#lecture2
#practice 0325
import pyautogui, time, snp

#印出1~20的質數
def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

for i in range(1, 21):
    if is_prime(i):
        print(i)

#Open your eyes! sample code 1
#取得滑鼠位置的座標及顏色
def report():
    pos = pyautogui.position()
    color = pyautogui.screenshot().getpixel(pos)
    print("Mouse position:", pos, "Color:", color)

while True:
    report()
    time.sleep(1)

#螢幕截圖
def min_all_windows():
    pyautogui.hotkey('win', 'd')
def desktop_screenshot():
    min_all_windows()
    return pyautogui.screenshot()
desktop_screenshot().save('desktop.png')

#hw6 (in-class assignment)
##先在網頁開好此測驗表單(https://docs.google.com/forms/d/e/1FAIpQLSdEgD2ifUPCXxRYxcwXQAKks3trS-wmbN0FOmXdfMK0KwOt5g/viewform?c=0&w=1)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')

pyautogui.FAILSAFE = True

def clickBoxes():
    #偵測螢幕上是否有與 box.png 相同的圖片
    #若有 loc 將會被指派相同於圖片的地方的位置，若沒有 loc 會被指派為 None
    loc = snp.locateOnScreen('box.png')
    #如果 loc 是 None / 如果有找到，會直接跳過這個迴圈
    while loc == None:                              
        time.sleep(0.1) #停 0.1 秒
        loc = snp.locateOnScreen('box.png') #再找一次
    ret = 0
    for loc_i in snp.locateAllOnScreen('box.png'):
        ret = ret + 1
        print(loc_i)
        center = pyautogui.center(loc_i)
        pyautogui.click(center)
    return ret

count = 0
while count < 60:
    count = count + clickBoxes()
    pyautogui.press('pagedown')
print(count)

#issues on screenshot
def report_time():
    t = time.time()
    left, top, width, height = 5, 66, 77, 8
    pyautogui.screenshot(region=(left,top,width,height))
    print(time.time()-t)

for i in range(100):
    report_time()
