import pyautogui
import time
from pynput import keyboard

# Function to check if the triggerbot should be enabled
def check_triggerbot_enabled():
    # Replace 'image.png' with the name of the image you want to locate
    image_location = pyautogui.locateOnScreen('image.png')
    return image_location is not None

# Function to perform a mouse click at the specified coordinates
def perform_mouse_click(x, y):
    pyautogui.click()

# UI
print("Valorant Color Triggerbot made by Zxre")
print("Please note that this triggerbot is for educational purposes only and may not be suitable for all players. Always make sure to follow the game's rules and guidelines. THIS IS VERY SIMPLE!!!")
print("  ")
print("This simple triggerbot is hopefully a way for Riot Games to develop a way to detect triggerbotters in game")
print(" ")

print("FOR EDUCATIONAL PURPOSES ONLY I AM NOT RESPONSIBLE FOR ANY BANS!!!")
print("  ")

print("Press F1 to toggle the triggerbot")
print("Press Ctrl+C to exit")

# Variables
triggerbot_enabled = False

# Functions
def on_press(key):
    global triggerbot_enabled
    if key == keyboard.Key.f1:
        triggerbot_enabled = not triggerbot_enabled
        print(f"Triggerbot {'enabled' if triggerbot_enabled else 'disabled'}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Main loop
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        if triggerbot_enabled:
            # Get the color of the center of the screen note if you play on a dif resolution change this to yours
            center_color = pyautogui.screenshot().getpixel((1920 // 2, 1080 // 2))

            # Check if the color is close to green (the color of the enemy in Valorant)
            if abs(center_color[0] - 10) < 10 and abs(center_color[1] - 255) < 10 and abs(center_color[2] - 10) < 10:
                pyautogui.click()

        time.sleep(0.01)
