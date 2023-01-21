import win32api
import win32con
import pyautogui
import time
import keyboard


# using win32api for faster clicks
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # pause to hold the mouse button for valid clicks
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# default - chrome window on left half screen, modify if required
tile2_x, tile2_y = 450, 350
tile3_x, tile3_y = 550, 350
tile4_x, tile4_y = 650, 350
tile1_x, tile1_y = 350, 350

# delay to switch to game window
time.sleep(5)

print("Script Running ....")

# press "e" to end the script
while not keyboard.is_pressed("e"):

    # checking r value from r,g,b as it's black - 0,0,0
    if pyautogui.pixel(tile1_x, tile1_y)[0] == 0:
        click(tile1_x, tile1_y + 15)

    if pyautogui.pixel(tile2_x, tile2_y)[0] == 0:
        click(tile2_x, tile2_y + 15)

    if pyautogui.pixel(tile3_x, tile3_y)[0] == 0:
        click(tile3_x, tile3_y + 15)

    if pyautogui.pixel(tile4_x, tile4_y)[0] == 0:
        click(tile4_x, tile4_y + 15)
