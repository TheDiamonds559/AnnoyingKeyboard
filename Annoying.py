from tkinter import *
import threading as t
import keyboard as k
import random as r
import time

keys = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

window = Tk()
window.geometry('400x400')

Text(window).pack()

def key(name):
    upper = r.randint(0, 1)
    rand = r.randint(1, 26)
    if(upper == 0):
        k.press_and_release('shift+' + keys[rand])
    else:
        k.press_and_release(keys[rand])
    time.sleep(0.1)
    key(name)

x = t.Thread(target=key, args=(1,))
x1 = t.Thread(target=key, args=(1,))

x.start()
time.sleep(1)
x1.start()
t.Thread(target=key, args=(1,)).start()

window.mainloop()
quit()


