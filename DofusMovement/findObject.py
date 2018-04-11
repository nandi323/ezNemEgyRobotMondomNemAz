import cv2
import numpy as np
import pyautogui
import pytesseract
from pathlib import Path
import random
from PIL import ImageGrab, Image, ImageEnhance, ImageFilter

from pywinauto.keyboard import SendKeys

src_path = 'C:/Users/balint.nandor/PycharmProjects/DofusMovement/analyze/'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def findResourcePrice(itemName=''):
        searchFiedX, searchFiedY = pyautogui.locateCenterOnScreen('searchField.PNG')
        searchFiedX = searchFiedX + random.randint(50, 75)
        searchFiedY = searchFiedY - random.randint(12, 21)
        pyautogui.moveTo(searchFiedX, searchFiedY, 0.2)
        pyautogui.click()
        pyautogui.typewrite(itemName, 0.1)
        firstResultX, firstResultY = pyautogui.locateCenterOnScreen('shopName.PNG')
        firstResultY = firstResultY + random.randint(80, 100)
        pyautogui.moveTo(firstResultX, firstResultY, 0.1)
        pyautogui.click()
        deleteButtonX, deleteButtonY = pyautogui.locateCenterOnScreen('deleteSearch.PNG')
        pyautogui.moveTo(deleteButtonX, deleteButtonY, 0.2)
        pyautogui.click()
        oneItemX, oneItemY =pyautogui.locateCenterOnScreen('1xitem.PNG')
        oneItemXSmall = oneItemX - 45
        oneItemXBig = oneItemX + 45
        oneItemYsmall = oneItemY + 21
        oneItemYBig = oneItemY + 47
        imageOfResult = ImageGrab.grab(bbox=(oneItemXSmall,oneItemYsmall,oneItemXBig,oneItemYBig))
        imageOfResult.save(src_path + itemName + "screenShot.png", "PNG")
        img = cv2.imread(src_path + itemName +  "screenShot.png", 0)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        # Write image after removed noise
        cv2.imwrite( src_path + itemName +  'removed_noise.jpg', img)

        img = (255 - img)
        cv2.imwrite(src_path + itemName +  'reverse.jpg', img)

        #  Apply threshold to get image with only black and white
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

        # Write the image after apply opencv to do some ...
        # cv2.imwrite(src_path + itemName +  'thres.jpg', img)

def findPriceOfEveryResource():
        with open("onlyFirstResources.txt", 'r') as inFile:
                for line in inFile.read().splitlines():
                        itemName = line
                        myFile = Path(src_path + itemName + "screenShot.png")
                        if myFile.is_file():
                                continue
                        searchFiedX, searchFiedY = pyautogui.locateCenterOnScreen('searchField.PNG')
                        searchFiedX = searchFiedX + random.randint(50, 75)
                        searchFiedY = searchFiedY - random.randint(12, 21)
                        pyautogui.moveTo(searchFiedX, searchFiedY, 0.2)
                        pyautogui.click()
                        pyautogui.typewrite(itemName, 0.1)
                        firstResultX, firstResultY = pyautogui.locateCenterOnScreen('shopName.PNG')
                        firstResultY = firstResultY + random.randint(80, 100)
                        pyautogui.moveTo(firstResultX, firstResultY, 0.1)
                        pyautogui.click()
                        deleteButtonX, deleteButtonY = pyautogui.locateCenterOnScreen('deleteSearch.PNG')
                        deleteButtonY = deleteButtonY + random.randint(-3,3)
                        deleteButtonX = deleteButtonX + random.randint(-4,4)
                        pyautogui.moveTo(deleteButtonX, deleteButtonY, 0.2)
                        pyautogui.click()
                        try:
                                oneItemX, oneItemY = pyautogui.locateCenterOnScreen('1xitem.PNG')
                                oneItemXSmall = oneItemX - 45
                                oneItemXBig = oneItemX + 45
                                oneItemYsmall = oneItemY + 29
                                oneItemYBig = oneItemY + 45
                                imageOfResult = ImageGrab.grab(bbox=(oneItemXSmall, oneItemYsmall, oneItemXBig, oneItemYBig))
                                imageOfResult.save(src_path + itemName + "screenShot.png", "PNG")
                                img = cv2.imread(src_path + itemName + "screenShot.png", 0)
                                kernel = np.ones((1, 1), np.uint8)
                                img = cv2.dilate(img, kernel, iterations=1)
                                img = cv2.erode(img, kernel, iterations=1)

                                # Write image after removed noise
                                cv2.imwrite(src_path + itemName + 'removed_noise.jpg', img)

                                img = (255 - img)
                                cv2.imwrite(src_path + itemName + 'reverse.jpg', img)
                        except TypeError:
                                print(itemName + 'not exists')
                                imageOfResult = ImageGrab.grab(
                                        bbox=(500, 500, 510, 510))
                                imageOfResult.save(src_path + itemName + "screenShot.png", 0)
                                imageOfResult.save(src_path + itemName + "NOT_EXISTS", 0)
                        except FileNotFoundError:
                                print(itemName +' bugos')


