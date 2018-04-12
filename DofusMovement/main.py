import windowManager
import buy1xitem
import findObject
from pywinauto.keyboard import SendKeys

characterName = "Milka"
window_size_x = 1100
window_size_y = 900

w = windowManager.WindowMgr()
w.find_window_wildcard(".*" + characterName + "*")
w.set_foreground()
#
rect = w.resize_window(window_size_x, window_size_y)
# buy1xitem.buyXItem(20)
#
# # findObject.findResourcePrice('Flask of draco')
findObject.findPriceOfEveryResource()

