import PySimpleGUI as sg
import subprocess
from pathlib import Path


def copy_to_clipboard(img_path):
    """ Given an an image path, copy the image to clipboard """
    print(img_path.absolute())
    command = f'xclip -sel clip -t image/png {img_path.absolute()}'
    subprocess.run(command.split())


sg.theme('LightBrown1')  # Use this as base theme
bg_color = '#2C2F33'  # copied from discord colors
sg.SetOptions(button_color=(bg_color, bg_color), background_color=bg_color,
              text_element_background_color=bg_color, text_color='white', border_width=0)

image_path = Path('.') / 'assets'

# layout the window
layout = [[sg.Text('Pick an emote!')]]
for img in image_path.iterdir():
    layout.append(
        [sg.Button('', key=img, image_filename=img, image_subsample=2)])

# Create the Window
window = sg.Window('Emote Picker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event)

window.close()
