import pyautogui
import time
import random

from pywinauto.keyboard import SendKeys


def buyXItem(number=5):
    i = 0
    n = number
    while i<n:
        i = i+1
        timeToMoveSelect = random.uniform(0.2, 0.3)
        timeToMoveBuy = random.uniform(0.2, 0.3)
        xSelect = random.randint(449, 533)
        ySelect = random.randint(362, 386)
        pyautogui.moveTo(xSelect,ySelect, timeToMoveSelect)
        pyautogui.click()

        xBuy = random.randint(506, 648)
        yBuy = random.randint(643, 659)
        pyautogui.moveTo(xBuy,yBuy, timeToMoveBuy)

        pyautogui.click()

        SendKeys('{ENTER}')
        time.sleep(0.1)