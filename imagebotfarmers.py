import pyautogui
import time
import cv2
import numpy as np
import time



def open_hero_tab():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    time.sleep( 1 )
    # load the image template this (this part is strange, and i'm not sure why.
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\test_center_hero_tab.png' )
    time.sleep( 1 )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( 1 )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( 1 )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def return_to_map():
    pyautogui.moveTo( 736, 166, 1 )  # should close out the hero screen and return to main map
    pyautogui.click( clicks=2, interval=0.25 )

def open_skill_slot():
    # take a screenshot
    screen = np.array( pyautogui.screenshot() )
    time.sleep( 1 )
    # load the image template
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\empty_skill_slot.png' )
    time.sleep( 1 )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( 1 )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( 1 )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


open_hero_tab()
#open_skill_slot()
return_to_map()