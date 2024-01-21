import pyautogui
import time
import tkinter
from tkinter import *


def click():    
    time.sleep(1)
    for i in range(50):
        pyautogui.click()

def fun(event):
    print(event.keysym, event.keysym=='r')
    if (event.keysym=='r'):
        click()

base= Tk()

def trigger():
    base.bind("<KeyRelease>", fun)

Label(base,text="Auto Clicker").grid(row=0,column=0,sticky=NSEW)
Button(base,text="R - Start",command=trigger).grid(row=0,column=1,sticky=NSEW)

mainloop()

