# PingMote
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images
# Getting Started
Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download the code as a zip and extract. Change into the pingmote directory and run `pingmote.py`.
# Usage
Running `python3 pingmote.py` will bring up the emote picker, closing when you pick an image.

I recommend binding this python command to a global keyboard shortcut (in GNOME: keyboard shortcuts > custom shortcuts > `python3 /abs/path/to/pingmote.py`)
# Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/37674516/107125905-81540c80-687a-11eb-9def-b4e51f2b9d32.gif)

# Configs
- Set `WINDOW_LOCATION` to where you want the top left corner of the emote picker to come up
- Set `IMAGE_PATH` to the path where your resized images are stored (use an absolute path if you want to run this globally)
- Set `AUTO_PASTE` if you want to automatically paste after selecting
- Set `AUTO_ENTER` if you want to automatically hit enter after pasting
- Check the top of `pingmote.py` for a couple additional configs

# Adding Your Own Emotes
- Drop image files in the original directory, then run `image_resizer.py` which will resize all the images and drop them in the resized directory
- https://discordmojis.com/emojis/popular_static is a good source (right click save image)

# Dependencies
These can be installed with `pip3 install -r requirements.txt`

PySimpleGUI

PIL (if using the image_resizer helper program)

## For Mac:
This program uses `xclip` for copying images to clipboard, and `xdotool` for keyboard keys (pasting and hitting enter). I think these can be installed with `homebrew`.

## For Windows:
TODO (if anyone wants to submit a PR that'd be much appreciated)

# Additional Notes
- Since this program relies on pasting resized images as emotes, we can't use inline emotes.
- I can't seem to get gifs working with `xclip` but it's possible that there's a way to paste gifs
- Images have slight padding in discord, so they don't look *exactly* the same as regular emotes

# TODOs
- Show window where mouse is (get mouse pos with PyAutoGUI?)
- Convert keyboard shortcuts to PyAutoGUI?
- Fix mac stuff (GUIs are super weird on mac)
- Use imgur links (GIF support!!)
- Paste on next click?