# PingMote
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images
# Usage
Running `python3 pingmote.py` will bring up the emote picker, closing when you pick an image.
# Demo

# Configs
- Set `WINDOW_LOCATION` to where you want the top left corner of the emote picker to come up
- Set `IMAGE_PATH` to the path where your resized images are stored (use an absolute path if you want to run this globally)
- Set `AUTO_PASTE` if you want to automatically paste after selecting
- Set `AUTO_ENTER` if you want to automatically hit enter after pasting

# Dependencies
These can be installed with `pip3 install -r requirements.txt`

PySimpleGUI

PIL (if using the image_resizer helper program)

## For Mac:
This program uses `xclip` for copying images to clipboard, and `xdotool` for keyboard keys (pasting and hitting enter). I think these can be installed with `homebrew`.

## For Windows:
TODO (if anyone wants to submit a PR that'd be much appreciated)