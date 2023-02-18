import pyautogui
import time
import random


def return_to_map():
    pyautogui.moveTo( 736, 166, 1 )  # should close out the hero screen and return to main map
    pyautogui.click( clicks=2, interval=0.25 )


def go_to_farming_skill_tab():
    pyautogui.moveTo( 1132, 304, random.uniform( 0.1, 1 ) )  # moves to the tab for farming skills
    pyautogui.click()


def go_to_hero_tab():
    pyautogui.moveTo( 1878, 655, random.uniform( 0.1, 1 ) )  # moves to hero tab
    pyautogui.click()


def go_to_equip_and_close():
    pyautogui.moveTo( 1097, 916, random.uniform( 0.1, 1 ) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform( 0.1, 1 ) )  # closes out the screen
    pyautogui.click()


def center_of_screen_for_scroll():
    pyautogui.moveTo( 961, 392, random.uniform( 0.1, 1 ) )  # moves to the screen to start the scroll


def skill_farmer1():
    go_to_hero_tab()
    center_of_screen_for_scroll()
    pyautogui.scroll( -2500 )
    pyautogui.moveTo( 788, 627, random.uniform( 0.1, 1 ) )  # moves to the hero
    pyautogui.click()
    pyautogui.moveTo( 1181, 549, random.uniform( 0.1, 1 ) )  # moves to skill slot 2 (this is for Tywin)
    pyautogui.click()
    go_to_farming_skill_tab()
    pyautogui.moveTo( 810, 566, random.uniform( 0.1, 1 ) )  # sets world gather speed 6
    pyautogui.click()
    go_to_equip_and_close()
    pyautogui.moveTo( 1176, 618, random.uniform( 0.1, 1 ) )  # moves to slot 3
    pyautogui.click()
    go_to_farming_skill_tab()
    center_of_screen_for_scroll()
    pyautogui.scroll( -2000 )
    pyautogui.moveTo( 914, 521, random.uniform( 0.1, 1 ) )  # food rare 6 equip
    pyautogui.click()
    go_to_equip_and_close()
    pyautogui.moveTo( 1173, 684, random.uniform( 0.1, 1 ) )  # moves to slot 4
    pyautogui.click()
    pyautogui.moveTo( 952, 505, random.uniform( 0.1, 1 ) )
    pyautogui.scroll( -10000 )
    pyautogui.moveTo( 1119, 507, random.uniform( 0.1, 1 ) )
    pyautogui.click()
    go_to_equip_and_close()
    pyautogui.moveTo( 1179, 754, random.uniform( 0.1, 1 ) )  # moves to slot 5
    pyautogui.click()
    center_of_screen_for_scroll()
    pyautogui.scroll( -12500 )
    pyautogui.moveTo( 817, 554, random.uniform( 0.1, 1 ) )  # moves to skill
    pyautogui.click()
    go_to_equip_and_close()
    return_to_map()


skill_farmer1()
time.sleep( random.uniform( 0.1, 1 ) )
