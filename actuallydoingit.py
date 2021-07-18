import numpy as np
import cv2
import pyautogui
import time
import mss
import keyboard
src = mss.mss()
pyautogui.PAUSE = 0

keyboard.wait("d","i","c")

topBar = cv2.imread("projects\\league auto closer\\topbar.png")
w = topBar.shape[1] #set the width and the height of the topbar 
h = topBar.shape[0]
ofCourse = cv2.imread("projects\\league auto closer\\exit.png")

clkw = 103
clkh = 14

ofcw = 50
ofch = 25



while True:
    screen = cv2.imread(src.shot())

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
    time.sleep(0.1)

    result = cv2.matchTemplate(screen, ofCourse, cv2.TM_CCOEFF_NORMED)

    threshhold =.98 #set the threshhold = to a number then if maxVal is greater than threshhold then make coordinates for each match  
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

    if keyboard.is_pressed('esc'):
        break


