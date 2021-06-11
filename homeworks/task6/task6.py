import pyautogui, time, snp

pyautogui.FAILSAFE = True


def click_all_boxes():
    loc = snp.locateOnScreen('box.png')       # 偵測螢幕上是否有與 box.png 相同的圖片，若有 loc 將會被指派相同於圖片的地方的位置，若沒有 loc 會被指派為 None

    while loc == None:                              # 如果 loc 是 None (剛剛螢幕上沒找到相同的圖片) / 如果有找到，會直接跳過這個迴圈
        time.sleep(0.1)                             # 停 0.1 秒
        loc = snp.locateOnScreen('box.png')   # 再找一次

    ret = 0 # 紀錄這次點到多少個 boxes

    for loc_i in snp.locateAllOnScreen('box.png'):
        ret = ret + 1
        print(loc_i)
        center = pyautogui.center(loc_i)
        pyautogui.click(center)

    return ret


count = 0
while count < 60:
    count = count + click_all_boxes()
    pyautogui.press('pagedown')
