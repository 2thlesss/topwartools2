import pyautogui
import time
import random


def skill_farmer1():
    pyautogui.moveTo( 1878, 655, random.uniform( 0.1, 1 ) )  # moves to hero tab
    pyautogui.click()
    pyautogui.moveTo( 961, 392, random.uniform( 0.1, 1 ) )  # moves to the screen to start the scroll
    pyautogui.scroll( -2500 )
    pyautogui.moveTo( 788, 627, random.uniform( 0.1, 1 ) )  # moves to the hero
    pyautogui.click()
    pyautogui.moveTo( 1181, 549, random.uniform( 0.1, 1 ) )  # moves to skill slot 2 (this is for Tywin)
    pyautogui.click()
    pyautogui.moveTo( 1132, 304, random.uniform( 0.1, 1 ) )  # moves to the tab for farming skills
    pyautogui.click()
    pyautogui.moveTo( 810, 566, random.uniform( 0.1, 1 ) )  # sets world gather speed 6
    pyautogui.click()
    pyautogui.moveTo( 1097, 916, random.uniform( 0.1, 1 ) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform( 0.1, 1 ) )  # closes out the screen
    pyautogui.click()
    pyautogui.moveTo( 1176, 618, random.uniform( 0.1, 1 ) )  # moves to slot 3
    pyautogui.click()
    pyautogui.moveTo( 1132, 304, random.uniform( 0.1, 1 ) )  # moves to the tab for farming skills
    pyautogui.click()
    pyautogui.moveTo( 963, 506, random.uniform( 0.1, 1 ) )  # moves to prepare to scroll
    pyautogui.scroll( -2000 )
    pyautogui.moveTo( 914, 521, random.uniform( 0.1, 1 ) )  # food rare 6 equip
    pyautogui.click()
    pyautogui.moveTo( 1097, 916, random.uniform( 0.1, 1 ) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform( 0.1, 1 ) )  # closes out the screen
    pyautogui.click()
    pyautogui.moveTo( 1173, 684, random.uniform( 0.1, 1 ) )  # moves to slot 4
    pyautogui.click()
    pyautogui.moveTo( 952, 505, random.uniform( 0.1, 1 ) )
    pyautogui.scroll( -10000 )
    pyautogui.moveTo( 1119, 507, random.uniform( 0.1, 1 ) )
    pyautogui.click()
    pyautogui.moveTo( 1097, 916, random.uniform( 0.1, 1 ) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform( 0.1, 1 ) )  # closes out the screen
    pyautogui.click()
    pyautogui.moveTo( 1179, 754, random.uniform( 0.1, 1 ) )  # moves to slot 5
    pyautogui.click()
    pyautogui.moveTo( 952, 505, random.uniform( 0.1, 1 ) )  # move to center of screen to set for scroll
    pyautogui.scroll( -12500 )
    pyautogui.moveTo( 817, 554, random.uniform( 0.1, 1 ) )  # moves to skill
    pyautogui.click()
    pyautogui.moveTo( 1097, 916, random.uniform( 0.1, 1 ) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform( 0.1, 1 ) )  # closes out the screen
    pyautogui.click()


skill_farmer1()
time.sleep( random.uniform( 0.1, 1 ) )
