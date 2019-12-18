import pyautogui
#import win32gui
import time
import keyboard
import os, threading

dirpath = os.path.dirname(os.path.abspath(__file__))
champselected = False

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
            
    print('Loop beendet..')



def bann_pick(bann,champ1,champ2=None,champ3=None):
    while keyboard.is_pressed('q') == False:
        time.sleep(1)
        print("Search for Banning..")
        if locate('bannchamplabel'):
            print("Found Bann Label, search textbox..")
            if locate('bannsearch'):
                print("Found Textbox, start banning..")
                pyautogui.click(locate('bannsearch'))
                pyautogui.write(bann)
                pyautogui.move(-440,50)
                pyautogui.click()           #Need to add 'Submit the bann'
                time.sleep(1)
                print('Champion Selected!')
        

        print("Search for Picking..")
        if locate('selectchamplabel'):
            print("Found Pick Label, search textbox..")
            if locate('champsearch'):               #champsearch is transparent, need another image
                print("Found Textbox, start picking..")
                pyautogui.click(locate('champsearch'))
                time.sleep(1)
                pyautogui.write(champ1)
                time.sleep(1)
                pyautogui.move(-440,50)
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                print('Champion Selected!')
                champselected = True
        if locate('selectchamp'):
            ghostclick('selectchamp')







lane1 = input('Erste Lane: ')
lane2 = input('Zweite Lane: ')
champ1 = input('Erster Champion: ')
champ2 = input('Zweiter Champion: ')
bann = input('Bann Champion: ')

window_title = 'League of Legends'
#hwnd = win32gui.FindWindow(None, window_title)
#win32gui.SetForegroundWindow(hwnd)

t1 = threading.Thread(target=auto_accept)
t2 = threading.Thread(target=startgame,args=(lane1,lane2))
t3 = threading.Thread(target=bann_pick,args=(bann,champ1,champ2))

t1.start()
t2.start()
t3.start()