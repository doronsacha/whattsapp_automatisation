import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(3)
position = pt.locateOnScreen("/home/oem/Desktop/test/whattsapp_auto/whattsapp/smylley.png",confidence=.6)
x= position[0]
y = position[1]


def get_message():
    global x,y
    position = pt.locateOnScreen("/home/oem/Desktop/test/whattsapp_auto/whattsapp/smylley.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=0.001)
    pt.moveTo(x+150, y-50, duration=0.001)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,-170)
    pt.click()
    whattsapp_message = pyperclip.paste()
    pt.click()
    return whattsapp_message


def post_response(message):
    position = pt.locateOnScreen("/home/oem/Desktop/test/whattsapp_auto/whattsapp/smylley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y, duration=0.001)
    pt.click()
    pt.typewrite(message,interval=.001)
    pt.typewrite("\n",interval= .001)


a= get_message()

if(a =="Le rishoum ouvre qd ??"):
    post_response("du coup qq t'a repondu...")