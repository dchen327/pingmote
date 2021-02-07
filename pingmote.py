'''
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images

Author: David Chen
'''
import PySimpleGUI as sg
import subprocess
from pathlib import Path
from time import sleep

# CONFIGS
GUI_BG_COLOR = '#36393F'  # copied from discord colors
# top left corner of emote picker, (0, 0) is screen top left
WINDOW_LOCATION = (200, 800)
NUM_COLS = 12  # max number of images per row in picker
# absolute path necessary here if running the program globally
IMAGE_PATH = Path('/home/dchen327/coding/projects/pingmote/assets/resized')
# IMAGE_PATH = Path('.') / 'assets/resized'
AUTO_PASTE = True  # if True, automatically pastes the image after selection
# if True and AUTO_PASTE is True, hits enter after pasting (useful in Discord)
AUTO_ENTER = True
# if pasting or enter isn't working, add a short delay (in seconds)
SLEEP_TIME = 0


def copy_to_clipboard(img_path):
    """ Given an an image path, copy the image to clipboard """
    command = f'xclip -sel clip -t image/png {img_path.absolute()}'
    subprocess.run(command.split())


sg.theme('LightBrown1')  # Use this as base theme
# Set location for where the window opens, (0, 0) is top left
sg.SetOptions(button_color=(GUI_BG_COLOR, GUI_BG_COLOR), background_color=GUI_BG_COLOR,
              text_element_background_color=GUI_BG_COLOR, text_color='white', border_width=0, window_location=WINDOW_LOCATION)


# layout the window
layout = []
curr_row = []
# print(len(list(image_path.iterdir())))  # print number of images
for idx, img in enumerate(IMAGE_PATH.iterdir(), start=1):  # add images to layout
    # print(convert_to_bytes(str(img)))
    curr_row.append(
        sg.Button('', key=img, image_filename=img, image_subsample=1))
    if idx % NUM_COLS == 0:  # start new row
        layout.append(curr_row)
        curr_row = []
layout.append(curr_row)

# create the window
window = sg.Window('Emote Picker', layout)
# event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # X clicked
        break
    window.close()
    copy_to_clipboard(event)  # copy clicked image to clipboard

    if AUTO_PASTE:
        sleep(SLEEP_TIME)  # wait a bit for copy operation before pasting
        paste_cmd = 'xdotool key ctrl+v'
        subprocess.run(paste_cmd.split())
        if AUTO_ENTER:
            sleep(SLEEP_TIME)
            enter_cmd = 'xdotool key Return'  # in Discord
            subprocess.run(enter_cmd.split())
