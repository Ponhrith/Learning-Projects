import time
from datetime import datetime
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser

keyboard = Controller()

isStarted = False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == i([1].split(':')[0]) and datetime.now().hour == i([1].split(':')[0]):
                webbrowser.open(i[0])
                isStarted=True
        elif isStarted == True:
            if datetime.now().hour == i([1].split(':')[0]) and datetime.now().hour == i([1].split(':')[0]):
                keyboard.press('x')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted == False
                break
