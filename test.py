import pyautogui
import win32gui
from PIL import Image
import time
import keyboard
import os, threading

def GetScreens():
    while True:
        imageTitle = str(input('Screen Title : '))
        print("Waiting for Key event..")
        while True:
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    theim = screenshot('League of Legends')
                    print("Screen Taken from:", imageTitle)
                    theim.save(r"E:\Users\petri\Documents\PyProjects\LoL\Images\{}.png".format(str(imageTitle)))
                    break  # finishing the loop
            except:
                break


def createdirlist():
    path = 'E:\\Users\\petri\\Documents\\PyProjects\\LoL\\Images\\'
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(os.path.join(r, file))

def scanningclient():
    predict = ''
    lowestdiff = 100
    while True:
        for CompImage in files:
            try:
                LiveClient = screenshot('League of Legends')
                im1 = Image.open(str(CompImage))
                os.system('cls')
                print("CompImage", CompImage[-12:])
                print('Prediction: {}\nDifference: {}'.format(predict,lowestdiff))
                if compare(LiveClient, im1) < lowestdiff:
                    predict = CompImage[-12:]
                    lowestdiff = compare(LiveClient, im1)
            except Exception as e:
                os.system('cls')
                print('Failed to see Client..')
                print(e)
                time.sleep(1)

files = []
createdirlist()
DiffList = []
ThreadList = []
ActivThreads = True
LiveClient = pyautogui.screenshot()

def GetLive():
    global LiveClient
    global ActivThreads
    print('GetLiveClient Thread started..')
    while ActivThreads:
        try:
            window_title = 'League of Legends'
            if window_title:
                hwnd = win32gui.FindWindow(None, window_title)
                if hwnd:
                    win32gui.SetForegroundWindow(hwnd)
                    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                    x, y = win32gui.ClientToScreen(hwnd, (x, y))
                    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                    im = pyautogui.screenshot(region=(x, y, x1, y1))
                    #print('Screen Taken!')
                    #print(DiffList)
                    LiveClient = im
                else:
                    print('Window not found!')
            else:
                im = pyautogui.screenshot()
                LiveClient = im
        except Exception as e:
            print('Live Fehler')


def GetClientState(dir_):
    global LiveClient
    global DiffList
    global files
    global ActivThreads
    global Image
    myindex = files.index(dir_)
    im1 = Image.open(str(dir_))
    print("Thread Started with Listindex " + str(myindex) + '\n' + 'And Picture:{}'.format(dir_[-12:]))
    while ActivThreads:
        try:
            i1 = LiveClient
            i2 = im1
            assert i1.mode == i2.mode, "Different kinds of images."
            assert i1.size == i2.size, "Different sizes."

            pairs = zip(i1.getdata(), i2.getdata())
            if len(i1.getbands()) == 1:
                # for gray-scale jpegs
                dif = sum(abs(p1-p2) for p1,p2 in pairs)
            else:
                dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

            ncomponents = i1.size[0] * i1.size[1] * 3

            DiffList[myindex] = ((dif / 255.0 * 100) / ncomponents)
        except Exception as e:
            print(e)

def KillThreads():
    global ActivThreads
    global keyboard
    while True:
        if keyboard.is_pressed('q'):
            ActivThreads=False
            print('Threads wurden beendet')
            break

killer = threading.Thread(target=KillThreads)
killer.start()
yy = threading.Thread(target=GetLive)
yy.start()
time.sleep(1)
for CompImage in files:
    t = threading.Thread(target=GetClientState,args=[CompImage])
    DiffList.append(0)
    t.start()
    ThreadList.append(t)
print('All Threads Started!\nStarting Info loop..')

while ActivThreads:
    os.system('cls')
    print(str(files[DiffList.index(min(DiffList))])[-12:])


ActivThreads=False
