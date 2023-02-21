import pyautogui
import cv2
import numpy as np
import time
import random


def open_hero_tab():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\test_center_hero_tab2.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def return_to_map():
    pyautogui.moveTo( 736, 166, 1 )  # should close out the hero screen and return to main map
    pyautogui.click( clicks=2, interval=0.25 )


def center_of_screen_for_scroll_skills():
    pyautogui.moveTo( 961, 392, random.uniform(0.1,0.5) )  # moves to the screen to start the scroll


def center_of_screen_for_scroll_skills1500():
    pyautogui.moveTo( 961, 392, random.uniform(0.1,0.5) )  # moves to the screen to start the scroll
    pyautogui.scroll( -1500 )
    time.sleep( random.uniform(0.1,0.5) )


def center_of_screen_for_scroll_skills_10000():
    pyautogui.moveTo( 961, 392, random.uniform(0.1,0.5) )  # moves to the screen to start the scroll
    pyautogui.scroll( -10000 )
    time.sleep( random.uniform(0.1,0.5) )


def go_to_farming_skill_tab():
    pyautogui.moveTo( 1132, 304, random.uniform(0.1,0.5) )  # moves to the tab for farming skills
    pyautogui.click()


def skill_slot_2_SSR():
    pyautogui.moveTo( 1181, 549, random.uniform(0.1,0.5) )  # moves to skill slot 2 (this is for SSR farmer)
    pyautogui.click()


def skill_slot_3_SSR():
    pyautogui.moveTo( 1176, 618, random.uniform(0.1,0.5) )  # moves to slot 3
    pyautogui.click()


def skill_slot_4_SSR():
    pyautogui.moveTo( 1173, 684, random.uniform(0.1,0.5) )  # moves to slot 4
    pyautogui.click()


def skill_slot_5_SSR():
    pyautogui.moveTo( 1179, 754, random.uniform(0.1,0.5) )  # moves to slot 5
    pyautogui.click()


def go_to_equip_and_close():
    pyautogui.moveTo( 1097, 916, random.uniform(0.1,0.5) )  # moves to equip
    pyautogui.click()
    pyautogui.moveTo( 1164, 238, random.uniform(0.1,0.5) )  # closes out the screen
    pyautogui.click()


def open_tywin():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\tywin.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def ganzo_farm_skills():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\ganzo.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def lvl_6_world_speed():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_6_rss_landmark.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def level_6_food():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_6_food.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def level_6_common_RSS():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_6_rss_common.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def lvl_6_food_common():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_6_food_common.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )

def open_flora():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\flora.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )

def open_smector():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    screen_array = np.array( screen )
    cv2.imshow( 'Screenshot', screen_array )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\ricardo.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )

def lvl_5_rare_rss():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_5_RSS.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )

def lvl_5_rare_food():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\level_5_food.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def lvl_5_common_rss():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_5_rss_common.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )


def lvl_5_common_food():
    # take a screenshot(this should be the whole ass screen, regardless of resolution)
    screen = np.array( pyautogui.screenshot() )
    # screen_array = np.array( screen )
    # cv2.imshow( 'Screenshot', screen_array )
    # cv2.waitKey( 0 )
    # cv2.destroyAllWindows()
    time.sleep( random.uniform(0.1,0.5) )
    # load the image template this (this part is strange, and i'm not sure why.)
    # I have to SS a much larger area than i would have wanted to in order to get it to recognize the image
    template = cv2.imread( 'C:\\Users\\warsh\\PycharmProjects\\farmerautomation\\lvl_5_food_common.png' )
    time.sleep( random.uniform(0.1,0.5) )
    # find the template in the screenshot
    res = cv2.matchTemplate( screen, template, cv2.TM_CCOEFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )
    time.sleep( random.uniform(0.1,0.5) )
    # get the coordinates of the top-left corner of the template
    x, y = max_loc
    time.sleep( random.uniform(0.1,0.5) )
    print( max_loc )
    # click on the center of the template
    pyautogui.click( x + template.shape[1] / 2, y + template.shape[0] / 2 )



#sr heros uses ssr 2-5 for skill slots.
open_hero_tab()
center_of_screen_for_scroll_skills()
pyautogui.scroll( -55000  )
pyautogui.scroll (-10000)
time.sleep( random.uniform(0.1,0.5) )
open_smector()
skill_slot_2_SSR()
go_to_farming_skill_tab()
lvl_5_rare_rss()
go_to_equip_and_close()
skill_slot_3_SSR()
go_to_farming_skill_tab()
center_of_screen_for_scroll_skills1500()
lvl_5_common_food()
go_to_equip_and_close()
skill_slot_4_SSR()
go_to_farming_skill_tab()
center_of_screen_for_scroll_skills_10000()
lvl_5_common_rss()
go_to_equip_and_close()
skill_slot_5_SSR()
center_of_screen_for_scroll_skills_10000()
lvl_5_common_food()
go_to_equip_and_close()
return_to_map()




