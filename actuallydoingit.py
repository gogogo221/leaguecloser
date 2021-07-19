import numpy as np
import cv2
import pyautogui
import time
import mss
import keyboard
from urllib import request
src = mss.mss()
pyautogui.PAUSE = 0



req = request.urlopen('https://raw.githubusercontent.com/gogogo221/leaguecloser/main/topbar.png')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
topBar = cv2.imdecode(arr, 1)


w = topBar.shape[1] #set the width and the height of the topbar 
h = topBar.shape[0]


req2 = request.urlopen('https://raw.githubusercontent.com/gogogo221/leaguecloser/main/exit.png')
arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
ofCourse = cv2.imdecode(arr2, 1)




clkw = 103
clkh = 14

ofcw = 50
ofch = 25



while True:
    screen = cv2.imread(src.shot(), 1)

    result = cv2.matchTemplate(screen, topBar, cv2.TM_CCOEFF_NORMED)
    threshhold =.98 #set the threshhold = to a number then if maxVal is greater than threshhold then make coordinates for each match  
    yloc, xloc = np.where(result >= threshhold)

    if len(xloc) > 0:
    
        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        target = rectangles[0]


        clkX = target[0] + clkw
        clkY = target[1] + clkh
    
        pyautogui.moveTo(clkX, clkY)
        pyautogui.click() 


        time.sleep(0.2)

        screen = cv2.imread(src.shot())
        result = cv2.matchTemplate(screen, ofCourse, cv2.TM_CCOEFF_NORMED)

        threshhold =.95 #set the threshhold = to a number then if maxVal is greater than threshhold then make coordinates for each match  
        yloc, xloc = np.where(result >= threshhold)

        if len(xloc) > 0:
            
            rectangles = []
            for (x, y) in zip(xloc, yloc):
                rectangles.append([int(x), int(y), int(w), int(h)])
                rectangles.append([int(x), int(y), int(w), int(h)])

            rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
            target = rectangles[0]


            clkX = target[0] + ofcw
            clkY = target[1] + ofch
        
            pyautogui.moveTo(clkX, clkY)
            pyautogui.click()   
    time.sleep(0.1)

    if keyboard.is_pressed('esc'):
        break
