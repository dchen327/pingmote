'''
A Python GUI for selecting and inserting local images

Author: David Chen
'''

import PySimpleGUI as sg
import subprocess
from pathlib import Path


def copy_to_clipboard(img_path):
    """ Given an an image path, copy the image to clipboard """
    # command = f'xclip -sel clip -t image/png {img_path.absolute()}'
    command = f'xclip -sel clip -t image/png {img_path.absolute()}'
    subprocess.run(command.split())


sg.theme('LightBrown1')  # Use this as base theme
BG_COLOR = '#36393F'  # copied from discord colors
# Set location for where the window opens, (0, 0) is top left
WINDOW_LOCATION = (1250, 750)
sg.SetOptions(button_color=(BG_COLOR, BG_COLOR), background_color=BG_COLOR,
              text_element_background_color=BG_COLOR, text_color='white', border_width=0, window_location=WINDOW_LOCATION)

image_path = Path('.') / 'assets' / 'resized'

# layout the window\
NUM_COLS = 10  # max number of images per row
layout = []
curr_row = []
print(len(list(image_path.iterdir())))
for idx, img in enumerate(image_path.iterdir(), start=1):  # add images to layout
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
    copy_to_clipboard(event)  # copy clicked image to clipboard

window.close()
