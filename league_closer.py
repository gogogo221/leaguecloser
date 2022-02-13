import numpy as np
import cv2
import pyautogui
import time
import mss
import keyboard
from urllib import request
src = mss.mss()
pyautogui.PAUSE = 0

threshhold =.98 

#get picture from link to github
def urlPic(url):
    req = request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv2.imdecode(arr, 1)


#get picture of the X button and the EXIT button
topBar = urlPic('https://raw.githubusercontent.com/gogogo221/leaguecloser/main/topbar.png')
ofCourse = urlPic('https://raw.githubusercontent.com/gogogo221/leaguecloser/main/exit.png')



#width and height added to coordinates to matching template to click
clkw = 103
clkh = 14
ofcw = 50
ofch = 25


#repeat
while True:
    #take and save a screenshot
    screen = cv2.imread(src.shot(), 1)

    #compare the X template to the screenshot to find any matches
    result = cv2.matchTemplate(screen, topBar, cv2.TM_CCOEFF_NORMED)

    #if match is greater than threshhold then make coordinates for the x and y location of the match

    yloc, xloc = np.where(result >= threshhold)

    if len(xloc) > 0:
    
        #make coordinates for where to click then click
        clkX = xloc + clkw
        clkY = yloc + clkh
        pyautogui.moveTo(clkX, clkY)
        pyautogui.click() 


        time.sleep(0.2)


        screen = cv2.imread(src.shot())
        result = cv2.matchTemplate(screen, ofCourse, cv2.TM_CCOEFF_NORMED)


        yloc, xloc = np.where(result >= threshhold)

        if len(xloc) > 0:
            
            clkX = xloc + ofcw
            clkY = yloc + ofch
            pyautogui.moveTo(clkX, clkY)
            pyautogui.click()   

    time.sleep(0.1)

    if keyboard.is_pressed('esc'):
        break
