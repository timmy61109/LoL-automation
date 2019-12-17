import pyautogui
import win32gui
from PIL import Image
import time
import keyboard
import os, threading

list = [0,0,0,0]

def changelist():
    global list
    list[2] = 200


print(list)
t = threading.Thread(target=changelist)
t.start()
print(list)
