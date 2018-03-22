import subprocess
import time
from datetime import datetime

def refresh():
    freeze_screen() # "Freeze" the screen
    subprocess.run(["xdotool", "key", "F5"]) # Refresh
    time.sleep(9) # Sleep for a bit, wait for the browser to refresh
    unfreeze_screen() # "Unfreeze" the screen

def freeze_screen():
    subprocess.run(["scrot", "freezescreen.png"]) # Take screenshot
    subprocess.Popen(["feh", "-F", "freezescreen.png"]) # Show the image fullscreen (and leave the process running, hence `Popen` and not `run`)
    time.sleep(1) # Wait for feh to "freeze" the screen

def unfreeze_screen():
    subprocess.run(["xdotool", "key", "Escape"]) # Exit out of feh

while True:
    refresh()
    time.sleep(10)
