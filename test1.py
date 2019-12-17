import pyautogui
import win32gui
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
    mousepos = pyautogui.position()
    if givenlane == 'MID':
        pyautogui.move(0,-90)
        pyautogui.click()
    if givenlane == 'JNGL':
        pyautogui.move(-70,-75)
        pyautogui.click()
    if givenlane == 'TOP':
        pyautogui.move(-90,0)
        pyautogui.click()
    if givenlane == 'ADC':
        pyautogui.move(70,-75)
        pyautogui.click()
    if givenlane == 'SUPP':
        pyautogui.move(90,0)
        pyautogui.click()

    pyautogui.moveTo(mousepos)

def startgame(firstlane,secondlane):
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
        print('1sec warten')
        time.sleep(1)
        print(locate('normallabel'))
        if locate('normallabel'):
            print('Normallabel gefunden')
            if locate('laneselect'):
                pyautogui.click(locate('laneselect'))
                time.sleep(1)
                selectlane(firstlane)
        print('1sec warten')
        time.sleep(1)
        if locate('laneselect'):
            pyautogui.click(locate('laneselect'))
            time.sleep(1)
            selectlane(secondlane)
        print('READY FÜRS GAME :)')
        print('Starte Game.')
        if locate('quesearch'):
            time.sleep(2)
            pyautogui.click(locate('quesearch'))
            print('Starte Auto Accept..')
            time.sleep(1)
            auto_accept()
    print('Loop beendet..')



def bann_pick(champ1,champ2,champ3=None,bann):
    while keyboard.is_pressed('q') == False:
        if locate('bannchamplabel'):
            if locate('bannsearch'):
                ghostclick('bannsearch')
                pyautogui.wr









window_title = 'League of Legends'
hwnd = win32gui.FindWindow(None, window_title)
win32gui.SetForegroundWindow(hwnd)
