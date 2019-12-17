import pyautogui
#import win32gui
import time
import keyboard
import os, threading

dirpath = os.path.dirname(os.path.abspath(__file__))

def img(imgname): #retruns full imgs path
    imgfolder = dirpath + '\\buttons\\'
    return imgfolder + imgname

def locate(imgname): #locate the given img x,y
    imgfolder = dirpath + '\\buttons\\'
    fullpath = imgfolder + imgname + '.png'
    return pyautogui.locateCenterOnScreen(fullpath)

def ghostclick(imgname): #Does a invisible click
    x,y = locate(imgname)
    mousepos = pyautogui.position()
    pyautogui.click(x,y)
    pyautogui.moveTo(mousepos)

def auto_accept():
    while keyboard.is_pressed('q') == False:
        time.sleep(3)
        im = locate('accept')
        if im:
            pyautogui.click(im)

def selectlane(givenlane):
    time.sleep(0.2)
    while True:
        lane = locate(givenlane)
        if lane:
            pyautogui.click(lane)
            print(givenlane, 'ausgewählt')
            return True

def startgame():
    print('Starte Thread')
    while keyboard.is_pressed('q') == False:
        print('Loop beginnt..')
        
        if locate('mainplay'):
            print('Mainplay wird gedrückt')
            ghostclick('mainplay')
        time.sleep(1.5)
        if locate('quecheck'):
            print('Checkbox wird gedrückt')
            ghostclick('quecheck')
        if locate('quesubmit'):
            print('Beginne Que..')
            ghostclick('quesubmit')
        time.sleep(1)
        if locate('normallabel'):
            print('Normallabel gefunden')
            if locate('laneselect'):
                print('SelectLane wird gedrückt')
                ghostclick('laneselect')
        selectlane('mid')
        time.sleep(1)
        if locate('laneselect'):
            ghostclick('laneselect')
        selectlane('top')
        print('READY FÜRS GAME :)')
    print('Loop beendet..')

startgame()