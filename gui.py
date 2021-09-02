import pyautogui
import time

import settings

def take_screenshot():
    pyautogui.screenshot(settings.WORKSPACE_DIR + '/screenshots_temp/screenshot.png')

def change_page():
    size_x, size_y = pyautogui.size()
    pyautogui.click(x=size_x, y=size_y*0.5, clicks=1)