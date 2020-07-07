## Made by KanuX <3 ##

import pyscreeze as ps
from pynput.mouse import Button, Controller
import keyboard as kb
import pyautogui as py
import mouse
import time
import random

ms = Controller()
posX, posY = py.size()
x, y = 0, 0

safeCPU = False

wait = time.sleep
sec=60

while True:
	x = x + 10
	if x > posX:
		x = 0
		y = y + 3
	if y > posY:
		y = 0
	colour = ps.pixelMatchesColor(x, y, (0, 230, 203))
	if colour == True:
		mouse.move(x, y, True, 0)
		ms.click(Button.left, 1)
		wait(5)
		mouse.move(0, 0, True, 0)
		safeCPU = True
	if safeCPU == True:
		wait(sec*8)
	safeCPU = False
