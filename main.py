import pyautogui
import time

def stripskillhero1():
    pyautogui.moveTo (1878,655, 1)#moves to hero tab
    pyautogui.click()
    pyautogui.moveTo(903,650,1) #moves to hero
    pyautogui.click()
    pyautogui.moveTo(1179,554,1) #moves to skill slot 1
    pyautogui.click()
    pyautogui.moveTo(872,769,1) #clicks unequip all
    pyautogui.click()
    pyautogui.moveTo(1064,726,1) #confirms unequip all
    pyautogui.click()

def skillstriphero2():
    pyautogui.moveTo(736,166,1)  #moves to the button to return to hero screen
    pyautogui.click()
    pyautogui.moveTo( 1016,641, 1 )  # moves to hero 2 of 3
    pyautogui.click()
    pyautogui.moveTo( 1179, 554, 1 )  # moves to skill slot 1
    pyautogui.click()
    pyautogui.moveTo( 872, 769, 1 )  # clicks unequip all
    pyautogui.click()
    pyautogui.moveTo( 1064, 726, 1 )  # confirms unequip all
    pyautogui.click()

def skillstriphero3():
    pyautogui.moveTo( 736, 166, 1 )  # moves to the button to return to hero screen
    pyautogui.click()
    pyautogui.moveTo( 1146,648, 1 )  # moves to hero 3 of 3
    pyautogui.click()
    pyautogui.moveTo( 1179, 554, 1 )  # moves to skill slot 1
    pyautogui.click()
    pyautogui.moveTo( 872, 769, 1 )  # clicks unequip all
    pyautogui.click()
    pyautogui.moveTo( 1064, 726, 1 )  # confirms unequip all
    pyautogui.click()
    pyautogui.moveTo( 736, 166, 1 )  # should close out the hero screen and return to main map
    pyautogui.click(clicks = 2, interval =0.25)





stripskillhero1()
time.sleep(2)
skillstriphero2()
time.sleep(2)
skillstriphero3()

